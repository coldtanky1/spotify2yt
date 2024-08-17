''' This is the script that will fetch the links of the songs and add them to a playlist. '''

from ytmusicapi import YTMusic
from utils.dl_video import download_videos

YTMusic = YTMusic('./secret/oauth.json')

def get_link_and_add_to_playlist(query: str, playlistId: str, allow_dups: bool = False, download: bool = False,
    dl_path: str = ''):

    # Get the videoIds.
    search_results = YTMusic.search(query)
    video_id = search_results[0]['videoId']

    # Add to playlist first
    try:
        response = YTMusic.add_playlist_items(playlistId, [video_id], duplicates=allow_dups)
        print(response.get('status'))

        if response.get('status') == 'STATUS_SUCCEEDED' or 'STATUS SUCCEEDED':
            # Download only if playlist addition is successful
            if download:
                download_videos(path=dl_path, videoId=video_id)
        else:
            print("Error adding to playlist:", response.get('error', 'Unknown error'))
    except Exception as e:
        print("Error: ", e)
