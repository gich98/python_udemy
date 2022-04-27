from bs4 import BeautifulSoup
import requests
import json

TOP_100_URL = "https://www.billboard.com/charts/hot-100/"
SPOTIFY_USER_ID = "MY_USER_ID"
SPOTIFY_TOKEN = "GENERATE TOKEN FROM HERE -> https://developer.spotify.com/console/get-current-user-playlists/"
SPOTIFY_TRACK_ENDPOINT = "https://api.spotify.com/v1/tracks/"
SPOTIFY_SEARCH_ENDPOINT = "https://api.spotify.com/v1/search?"
SPOTIFY_PLAYLIST_ENDPOINT = F"https://api.spotify.com/v1/users/{SPOTIFY_USER_ID}/playlists"
date = ""


def clear_songs_artist(songs_artist_):
    """
    Remove all \n and \t
    :param songs_artist_: list of artists' name
    :return: list of artists' name without \n and \t
    """
    result = []
    for _ in songs_artist_:
        try:
            int(_.getText().replace("\n", "").replace("\t", ""))
        except ValueError:
            artist = _.getText().replace("\n", "").replace("\t", "")
            if artist != "-":
                result.append(artist)
    return result


def create_url():
    """
    Ask input from user for the date
    :return: URL with the date inserted by the user
    """
    date_to_travel = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
    global date
    date = date_to_travel
    return TOP_100_URL + date_to_travel


def scrap_top_100_songs(url_):
    """
    Scrap top 100 songs from https://www.billboard.com/
    :param url_: The URL generated from the create_url()
    :return: List of Dict with the top 100 songs' title and artist
    """
    response = requests.get(url=url_)
    soup = BeautifulSoup(response.text, "html.parser")
    songs_title = [title.getText().replace("\n", "").replace("\t", "")
                   for title in soup.select(selector="div ul li ul li h3")]
    songs_artist = clear_songs_artist(soup.select(selector="div ul li ul li span"))
    result = []
    for _ in range(0, len(songs_title)):
        result.append({
            "artist": songs_artist[_],
            "title": songs_title[_],
        })
    return result


def top_100_songs_with_ids(top_100_songs_):
    """
    Re-create the top_100_songs with the id of the songs
    :param top_100_songs_: The list of songs generated from scrap_top_100_songs(url_)
    :return: List of Dict with the top 100 songs' title, artist and his Spotify ID
    """
    result = []
    for song in top_100_songs_:
        title = song["title"].replace("'", "")
        artist = song["artist"].replace("'", "")
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {SPOTIFY_TOKEN}",
        }
        try:
            params = {
                "q": f"track:{title} artist:{artist}",
                "type": "track",
            }
            r = requests.get(SPOTIFY_SEARCH_ENDPOINT,
                             params=params,
                             headers=headers)
            r.raise_for_status()
            result.append({
                "artist": artist,
                "title": title,
                "song_id": r.json()['tracks']['items'][0]['id']
            })
        except IndexError:
            params = {
                "q": f"track:{title}",
                "type": "track",
            }
            r = requests.get(SPOTIFY_SEARCH_ENDPOINT,
                             params=params,
                             headers=headers)
            result.append({
                "artist": artist,
                "title": title,
                "song_id": r.json()['tracks']['items'][0]['id']
            })
    return result


def create_playlist():
    """
    Create a playlist on your Spotify's profile
    :return: ID of the playlist created
    """
    request_body = json.dumps({
        "name": f"{date} Billboard 100",
        "description": "My first programmatic playlist, yooo!",
        "public": False,
    })
    r = requests.post(url=SPOTIFY_PLAYLIST_ENDPOINT,
                      data=request_body,
                      headers={
                          "Content-Type": "application/json",
                          "Authorization": f"Bearer {SPOTIFY_TOKEN}",
                      })
    r.raise_for_status()
    return r.json()["id"]


def add_top_100_songs_to_playlist(playlist_id_, top_100_songs_):
    """
    Add the top 100 songs in the playlist created from create_playlist()
    :param playlist_id_: ID of the playlist generated
    :param top_100_songs_: List of Dict of the top 100 songs
    :return: Response's Status Code
    """
    endpoint_url = f"https://api.spotify.com/v1/playlists/{playlist_id_}/tracks"
    uris = ["spotify:track:"+str(song["song_id"]) for song in top_100_songs_]
    request_body = json.dumps({
        "uris": uris
    })
    r = requests.post(url=endpoint_url,
                      data=request_body,
                      headers={
                          "Content-Type": "application/json",
                          "Authorization": f"Bearer {SPOTIFY_TOKEN}"
                      })
    r.raise_for_status()
    return r.status_code


url = create_url()
top_100_songs = scrap_top_100_songs(url)
top_100_songs = top_100_songs_with_ids(top_100_songs)
playlist_id = create_playlist()
status = add_top_100_songs_to_playlist(playlist_id, top_100_songs)
if status == "201":
    print("Playlist Created correctly")
else:
    print("Error during the creation of the Playlist")
