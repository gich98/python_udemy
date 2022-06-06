import requests
from bs4 import BeautifulSoup
from anime import Anime
import urllib.request
from pathlib import Path


AF_URL = 'https://www.animeforce.it/lista-anime/'
NUMBER_ANIME_PER_PAGE = 10


class AnimeManager:

    def __init__(self):
        self.anime_list = self.create_anime_list()
        self.total_pages = len(self.anime_list) - 1
        self.current_page = 0
        self.current_anime = None
        self.current_anime_chunk = self.anime_list[self.current_page]
        self.response_text = ""

    @staticmethod
    def create_anime_list():
        """
        Creates the list of anime from https://www.animeforce.it/lista-anime/ as a list of sublist.
        Each sublist is composed by 10 anime and each anime is composed by its title and link to the anime page.
        :return: The complete list of anime
        """
        result = []
        response = requests.get(url=AF_URL)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        sections_anime = soup.find_all('div', class_='letter-section animeforce')

        for section_anime in sections_anime:
            a_section = section_anime.find_all('a')
            for a in a_section:
                if a.get('title'):
                    result.append({
                        'title': a.get('title'),
                        'link': a.get('href')
                    })

        chunked_anime_list = [result[i:i + NUMBER_ANIME_PER_PAGE]
                              for i in range(0, len(result), NUMBER_ANIME_PER_PAGE)]
        return chunked_anime_list

    def set_current_anime(self, anime_id):
        anime_link = self.current_anime_chunk[anime_id].get('link')
        response = requests.get(url=anime_link)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        info_divs = soup.find_all(name='div', class_='col-md-12')
        episodes_div = soup.find('div', {"id": "nav-tabContent"})
        title = soup.find('div', {'class': 'anime-title'}).text
        info_anime = {}
        # Creates a dictionary called info_anime that will contain all the information of the anime selected
        for info in info_divs:
            info_text = [_ for _ in info.text.split('\n') if _ != '']
            # if the length of the list is equal to 1 that means that
            if 'Descrizione:' in info_text[0]:
                info_text_temp = info_text[0].split(':')
                info_anime[info_text_temp[0]] = ':'.join(info_text_temp[1:])
            elif len(info_text) > 1:
                info_anime[info_text[0]] = info_text[1:]
        self.current_anime = Anime(_title=title,
                                   _status=info_anime.get('Stato')[0],
                                   _genre=info_anime.get('Genere'),
                                   _typology=info_anime.get('Tipologia'),
                                   _season=info_anime.get('Stagione')[0]
                                   if info_anime.get('Stagione') is not None else '',
                                   _num_episodes=info_anime.get('Numero Episodi:'),
                                   _description=info_anime.get('Descrizione'),
                                   _episodes_content=episodes_div)

    def anime_page(self):
        print(f"====================================================================================================\n"
              f"ANIME SELECTED:\n"
              f"  - Title: {self.current_anime.get_title()}\n"
              f"  - Typologies: {', '.join(self.current_anime.get_typology())}\n"
              f"  - Genre: {', '.join(self.current_anime.get_genre())}\n"
              f"  - Season: {self.current_anime.get_season()}\n"
              f"  - Status: {self.current_anime.get_status()}\n"
              f"  - Number of Episodes: {', '.join(self.current_anime.get_num_episodes())}\n"
              f"  - Description: {self.current_anime.get_description()}\n"
              f"====================================================================================================\n")

    @staticmethod
    def ask_download():
        keep_ask = True
        choice = ''
        while keep_ask:
            print("------------------------------------------------------------------\n")
            choice = input("Do you want to download the episodes for this anime?\n"
                           "Enter 'y' if you want to download\n"
                           "Enter 'n' to go to the previous page\n"
                           "- ")
            if choice == 'y' or choice == 'n':
                keep_ask = False
            else:
                print(f"[ANIME-MANAGER 101] Command Error!!! Command {choice} not recognized!")
        return choice

    def ask_typology(self):
        keep_ask = True
        choice = -1
        while keep_ask:
            print("------------------------------------------------------------------\n")
            print("What Typology do you want to download?")
            for index, typology in enumerate(self.current_anime.get_typology()):
                print(f"{index}) {typology}")
            try:
                choice = int(input("Enter the ID of the Typology you want to download\n"
                                   "Enter '-1' to Cancel the operation\n"
                                   "- "))
                if -1 <= choice <= len(self.current_anime.get_typology()) - 1:
                    keep_ask = False
                else:
                    print("[ANIME-MANAGER 118] Error! Invalid Typology ID!")
            except ValueError as e:
                print("[ANIME-MANAGER 120] Error! Invalid input! You must enter a number not a word/letter.\n"
                      f"Technical Error: {e}")
        return choice

    def download_anime_episodes(self, anime_typology):
        anime_episodes_to_download = self.current_anime.get_episodes_by_typology(anime_typology)
        for episode in anime_episodes_to_download:
            episode_link = episode.get_link()
            episode_link_split = episode_link.split('/')
            episode_name = episode_link_split[-1]
            episode_folder = episode_link_split[-2]
            if 'vvvvid' not in episode_link:
                Path(episode_folder).mkdir(parents=True, exist_ok=True)
                print(f"Downloading {episode_name}...")
                # urllib.request.urlretrieve(episode_link, f'{episode_folder}/{episode_name}')
                print(f"Download for {episode_name} complete!")
            else:
                print(f"[ANIME-MANAGER 137] Error Download!!! The link {episode_link} is not valid!")
            print("------------------------------------------------------------------\n")
        input(f"Download for the anime {self.current_anime.get_title()}, "
              f"type {self.current_anime.get_typology()[anime_typology]} complete!\n"
              f"Press Enter to continue...")

    def next_page(self):
        if self.current_page != self.total_pages:
            self.current_page += 1
            self.current_anime_chunk = self.anime_list[self.current_page]

    def previous_page(self):
        if self.current_page != 0:
            self.current_page -= 1
            self.current_anime_chunk = self.anime_list[self.current_page]

    def exit(self):
        self.current_page = -1
