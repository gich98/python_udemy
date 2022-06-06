from episode import Episode


class Anime:

    # soup.select('div[#nav-tabContent]')
    def __init__(self, _title, _status, _season, _typology, _genre, _num_episodes, _description, _episodes_content):
        self._title = _title
        self._status = _status
        self._season = _season
        self._genre = _genre
        self._typology = _typology
        self._num_episodes = _num_episodes
        self._description = _description
        self._episodes = self.__set_episodes(_episodes_content)

    def __set_episodes(self, episodes_content):
        """
        Creates the list of all the episodes for the selected anime
        :param episodes_content: HTML's tag section that contains the list of the episodes
        :return: Dictionary that contains the episodes (values) grouped by the type (key)
        """
        episodes = {}
        # For each typology select the HTML's tag section that contains the list of episodes of that type
        # and then create a new pair (key, value) in the episodes Dictionary
        for t in self._typology:
            episodes_by_tag = []
            if t == 'TV':
                episodes_by_tag = episodes_content.find('div', {'id': 'nav-streaming'})
            elif t == 'OAV':
                episodes_by_tag = episodes_content.find('div', {'id': 'nav-OAV'})
            elif t == 'Special':
                episodes_by_tag = episodes_content.find('div', {'id': 'nav-Special'})
            elif t == 'Movie':
                episodes_by_tag = episodes_content.find('div', {'id': 'nav-Movie'})

            episodes[t] = [Episode(_title=episode.text, _episode_link=episode.get('href'), _type=t)
                           for episode in episodes_by_tag.find_all(name='a') if 'http' in episode.get('href')]

        return episodes

    def all_episodes_str(self):
        """
        Get all the episodes as a string
        :return: String that contains the concatenation of the episode.__str__()
        """
        result = ""
        for key in self._episodes:
            result += f"TYPOLOGY: {key}\n"
            for episode in self._episodes.get(key):
                result += episode.__str__()
            result += "----------------------------------------------------------------------------------------------\n"
        return result

    def get_episodes_by_typology(self, typology_id):
        typology = self._typology[typology_id]
        episodes_by_typology = self._episodes.get(typology)
        return episodes_by_typology

    def get_title(self):
        return self._title

    def get_season(self):
        return self._season

    def get_typology(self):
        return self._typology

    def get_status(self):
        return self._status

    def get_description(self):
        return self._description

    def get_num_episodes(self):
        return self._num_episodes

    def get_genre(self):
        return self._genre

    def __str__(self):
        return "Anime info:\n" \
               f"- Title: {self._title}\n" \
               f"- Status: {self._status}\n" \
               f"- Season: {self._season}\n" \
               f"- Genre: {self._genre}\n" \
               f"- Typologies: {self._typology}\n" \
               f"- Number episodes: {self._num_episodes}\n" \
               f"- Description: {self._description}\n" \
               f"- Episodes:\n{self.all_episodes_str()}"
