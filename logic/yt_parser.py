from __future__ import unicode_literals
from googleapiclient.discovery import build
from settings import yt_api_key, output_dir
from ffmpeg import run, input, output
from isodate import parse_duration
from pytube import YouTube
from os import remove


def get_videos_by_name(name, max_results):
    # initialize youtube api
    with build('youtube', 'v3', developerKey=yt_api_key) as service:
        # getting videos by requesting youtube api key
        videos = service.search().list(part="snippet", q=name, maxResults=max_results)
        data = []   # list to save videos ids, titles and
        for item in videos.execute()['items']:
            # skip if got not youtube#video
            if item['id']['kind'] != 'youtube#video':
                continue

            # getting data from api response
            video_title = item['snippet']['title']
            video_id = item['id']['videoId']
            video_details = service.videos().list(part="contentDetails", id=video_id).execute()
            video_duration = parse_duration(video_details["items"][0]["contentDetails"]["duration"])

            data.append({'title': video_title, 'id': video_id, 'duration':video_duration})  # saving data to list
        service.close()     # closing api connection
    return data


def download_audio(video_id):
    yt = YouTube(f'https://www.youtube.com/watch?v={video_id["id"]}')  # constructing url to download
    # downloading video
    stream = yt.streams.first()
    stream.download()

    # setting file names
    mp4 = stream.default_filename
    mp3 = ''.join((output_dir, mp4.replace('.mp4', '.mp3')))

    # converting mp4 to mp3
    audio = input(mp4).audio
    run(output(audio, mp3))

    # removing mp4
    remove(mp4)
    return mp3


def del_files(*files):
    for file in files:
        remove(file)