''' This is the script that will fetch the spotify playlist and add the tracks to a text file. '''

from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
REDIRECT_URL = os.getenv('REDIRECT_URL')

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URL,
                                               scope="playlist-read-private"))

def fetch_sp_pl(link: str):
    playlist_url = link
    playlist = sp.playlist(playlist_url)
    song_data = []

    for name in playlist['tracks']['items']:
        song_name = name['track']['name']
        artist = name['track']['artists'][0]['name']
        song_data.append(f"{song_name} {artist}\n")

    try:
        os.mkdir(os.getcwd() + '/results/')
    except FileExistsError:
        pass

    with open(os.getcwd() + '/results/sp_result.txt', 'w') as f:
        f.writelines(song_data)
     
