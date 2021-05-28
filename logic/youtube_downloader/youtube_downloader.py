from moviepy.editor import *
from pytube import YouTube
import os


def download_from_youtube(link: str, download_type: str = 'only_audio', output_dir: str ='.') -> tuple:
    def convert_to_mp3(mp4_path: str) -> str:
        mp3_path = mp4_path.replace('.mp4', '.mp3')
        video = VideoFileClip(mp4_path)

        audio = video.audio
        audio.write_audiofile(mp3_path)

        audio.close()
        video.close()
        return mp3_path

    def download_audio():
        mp4_path = os.path.join(output_dir, stream.default_filename)
        mp3_path = convert_to_mp3(mp4_path)
        os.remove(mp4_path)
        return mp3_path, None

    def download_video():
        mp4_path = os.path.join(output_dir, stream.default_filename)
        return mp4_path, None

    def download_both():
        mp4_path = os.path.join(output_dir, stream.default_filename)
        mp3_path = convert_to_mp3(mp4_path)
        return mp3_path, mp4_path


    download_types = {
        'only_audio': download_audio,
        'only_video': download_video,
        'both': download_both
    }

    yt = YouTube(link)

    stream = yt.streams.filter().first()
    stream.download(output_dir)

    return download_types[download_type]()


if __name__ == '__main__':
    download_from_youtube('https://www.youtube.com/watch?v=9L8Sgvx-b5Q', output_dir='../')