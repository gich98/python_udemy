import requests
from bs4 import BeautifulSoup


class Episode:

    def __init__(self, _title, _episode_link, _type):
        self._title = _title
        self._link = self.get_download_link(_episode_link)
        self._type = _type

    @staticmethod
    def get_download_link(episode_link):
        response = requests.get(url=episode_link)
        soup = BeautifulSoup(response.text, 'html.parser')
        try:
            download_link = soup.find('a', class_='btn-block').get('data-href')
        except AttributeError:
            print("Internal Error! Can't get the links for the downloads.")
            return None
        return download_link

    def get_title(self):
        return self._title

    def get_link(self):
        return self._link

    def get_type(self):
        return self._type

    def set_title(self, _title):
        self._title = _title

    def set_link(self, _link):
        self._link = _link

    def set_type(self, _type):
        self._type = _type

    def __str__(self):
        return "Episode info:\n" \
               f"    - Title: {self._title}\n" \
               f"    - Link: {self._link}\n" \
               f"    - Type: {self._type}\n"
