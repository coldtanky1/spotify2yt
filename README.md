# Spotify2YT
A tool written in Python designed to convert a Spotify playlist into a Youtube Music playlist.

# Requirements
- ytmusicapi
- yt-dlp
- spotipy API
- python-dotenv
- spotify developer account (visit https://developers.spotify.com/)

Once you have created a developer account for spotify, create a new app and get the CLIENT ID and SECRET.
Easy to follow tutorial can be found [here](https://www.youtube.com/watch?v=kaBVN8uP358).


# Setup
Step 1:
```bash
pip install -r requirements.txt
```

Step 2:
run:
```bash
cd src/secret && ytmusicapi oauth
```
Follow the instructions and press "Enter" after you're done. This should create a "oauth.json" file.

Step 3:
place the "CLIENT_ID", "CLIENT_SECRET" and "REDIRECT_URL" into the .env file in src/.

Step 4:
run the spotify2yt.py file like so:
```bash
python spotify2yt.py -l [SPOTIFY_PLAYLIST_LINK_HERE] -i [YOUTUBE_PLAYLIST_ID]
```
(Add a '-a' flag at the end if you wish to allow duplicates)
