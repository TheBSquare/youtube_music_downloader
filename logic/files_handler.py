from ffmpeg import run, input, output
from settings import output_mp3, output_mp4
from os import remove


def convert_to_mp3(mp4):
    # constructing mp3 name
    mp3 = mp4.replace('.mp4', '.mp3').replace(output_mp4, output_mp3)

    # converting mp4 to mp3
    audio = input(mp4).audio
    run(output(audio, mp3))

    return mp3


def del_files(*files):
    for file in files:
        remove(file)
