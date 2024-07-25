''' This is the script that will fetch the links of the songs and add them to a playlist. '''

import os
from ytmusicapi import YTMusic

YTMusic = YTMusic("./secret/oauth.json")

def get_link_and_add_to_playlist(*query: str):
    # Get the videoIds.
    query = ''.join(query)
    search_results = YTMusic.search(query)

    # Add to playlist.
    try:
        playlistId = 'PLxGl884G91ds9qHzrQBruECBMAglLzz0R'
        response = YTMusic.add_playlist_items(playlistId, [search_results[0]['videoId']])
        print({response.get('status')})
    except Exception as e:
        print("Error: ", e)

# Goes through all the tracks from spotify result text file.
with open(os.getcwd() + '/results/sp_result.txt') as q:
    for line in q:
        query = line.strip()
        get_link_and_add_to_playlist(query)


''' Optional threading for those who want it. This massively speeds up the process. '''
# import threading.
# threads = []
# with open('sp_result.txt') as q:
#     for line in q:
#         query = line.strip()
#         t = threading.Thread(target=get_link_and_add_to_playlist, args=(query,))
#         threads.append(t)
#         t.start()

# # Wait for all threads to complete
# for t in threads:
#     t.join()
