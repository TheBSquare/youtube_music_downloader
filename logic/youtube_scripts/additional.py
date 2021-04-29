from pytube import YouTube
from settings import output_mp4


def download_video(video):
    # constructing url to download
    yt = YouTube(video['link'])

    # downloading video
    stream = yt.streams.first()
    stream.download(output_mp4)

    # return the name of the downloaded file
    return ''.join((output_mp4, stream.default_filename))
