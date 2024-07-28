''' This is the script that will fetch the links of the songs and add them to a playlist. '''

import os
from ytmusicapi import YTMusic

YTMusic = YTMusic("./secret/oauth.json")

def get_link_and_add_to_playlist(query: str, playlistId: str):
    # Get the videoIds.
    search_results = YTMusic.search(query)

    # Add to playlist.
    try:
        response = YTMusic.add_playlist_items(playlistId, [search_results[0]['videoId']])
        print({response.get('status')})
    except Exception as e:
        print("Error: ", e)