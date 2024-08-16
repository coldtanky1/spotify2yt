#!/usr/bin/env python

import sys
import os
from utils.yt_playlist import get_link_and_add_to_playlist
from utils.fetch_playlist import fetch_sp_pl

sp_link = None
playlistId = None
allow_duplicate = False

try:
    sp_link = sys.argv[2]
    playlistId = sys.argv[4]
    allow_duplicate = sys.argv[5]
except IndexError:
    if '-l' not in sys.argv[1]:
        print("'-l' is a required argument.")
        sys.exit()
    elif '-i' not in sys.argv[3]:
        print("'-i' is a required argument.")
        sys.exit()
    elif '-a' not in sys.argv[5]:
        pass
    elif sp_link is None:
        print("Spotify playlist link is required.")
        sys.exit()
    elif playlistId is None:
        print("Youtube playlist ID is required.")
        sys.exit()

print("Fetching spotify playlist...")
fetch_sp_pl(sp_link)
print("Done fetching spotify link.")

print("Adding to YTMusic playlist.")

# Goes through all the tracks from spotify result text file.
with open(os.getcwd() + '/results/sp_result.txt') as q:
    if allow_duplicate is False:
        pass
    else:
        print("If the status appears as 'STATUS FAILED' it maybe because there are duplicates.")
    for line in q:
        query = line.strip()
        get_link_and_add_to_playlist(query=query, playlistId=playlistId, allow_dups=allow_duplicate)
    
    print("Done adding to YTMusic playlist.")
