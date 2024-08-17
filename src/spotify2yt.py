#!/usr/bin/env python

import argparse
import os
from utils.dl_video import download_videos
from utils.yt_playlist import get_link_and_add_to_playlist
from utils.fetch_playlist import fetch_sp_pl

parser = argparse.ArgumentParser(description="Convert Spotify playlist to YouTube playlist")
parser.add_argument("-l", "--spotify_link", required=True, help="Spotify playlist link")
parser.add_argument("-i", "--youtube_id", required=True, help="YouTube playlist ID")
parser.add_argument("-a", "--allow_duplicate", action="store_true", help="Allow duplicate tracks")

args = parser.parse_args()

spotify_link = args.spotify_link
playlist_id = args.youtube_id
allow_duplicate = args.allow_duplicate

# Prompt the user.
dl_input = input("Would you like to download the video? (Y/N)\n").lower()
download = False
path = ''

match dl_input.lower():
    case "y" | "yes":
        download = True
        try:
            with open('path.txt', 'r') as pr:
                same_file = input(f"Would you like to download into '{pr.read()}'? (Y/N)\n")
                match same_file.lower():
                    case "y" | "yes":
                        path = pr.read()
                    case "n" | "no":
                        path = input("Specify a path to where you would like to download the videos:\n")
        except FileNotFoundError:
            path = input("Specify a path to where you would like to download the videos:\n")
            with open('path.txt', 'w') as p:
                p.write(path)

    case "n" | "no":
        pass

print("Fetching spotify playlist...")
fetch_sp_pl(spotify_link)
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
        get_link_and_add_to_playlist(query=query, playlistId=playlist_id, allow_dups=allow_duplicate,
            download=download, dl_path=path)

    print("Done adding to YTMusic playlist.")
