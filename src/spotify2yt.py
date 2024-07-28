import sys
import os
from yt_playlist import get_link_and_add_to_playlist
from fetch_playlist import fetch_sp_pl

try:
    sp_link = sys.argv[1]
    playlistId = sys.argv[2]
except IndexError:
    if sp_link is None:
        print("Spotify playlist link is required.")
        sys.exit()
    else:
        print("Youtube Playlist ID is required.")
        sys.exit()


print("Fetching spotify playlist...")
fetch_sp_pl(sp_link)
print("Done fetching spotify link.")

print("Adding to YTMusic playlist.")
# Goes through all the tracks from spotify result text file.
with open(os.getcwd() + '/results/sp_result.txt') as q:
    print("If the status appears as 'STATUS FAILED' it maybe because there are duplicates.")
    for line in q:
        query = line.strip()
        get_link_and_add_to_playlist(query, playlistId)
    
    print("Done adding to YTMusic playlist.")


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