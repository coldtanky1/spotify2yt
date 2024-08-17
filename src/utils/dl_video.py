''' This is the script that will download the videos. '''

from __future__ import unicode_literals
import yt_dlp as youtube_dl
import os

def download_videos(path: str, videoId: str) -> None:

    def my_hook(d):
        if d['status'] == 'finished':
            print('Done downloading, now post-processing ...')


    ydl_opts = {
        'extract_audio': True,
        'format': 'bestaudio',
        'outtmpl': os.path.join(path, '%(title)s.mp3'),
        'progress_hooks': [my_hook],
    }
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([f'https://www.youtube.com/watch?v={videoId}'])
    except Exception as e:
           print("Error: ", e)
