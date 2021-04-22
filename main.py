#!/usr/bin/env python3
from argparse import ArgumentParser
from logic.yt_parser import get_videos_by_name, download_audio, del_files
from logic.play_music import play
from threading import Thread
from sys import exit


def main():
    # creating arg parser
    args_parser = ArgumentParser(description='')
    args_parser.add_argument('video_name', type=str, help='Enter the name of the youtube video')
    args_parser.add_argument('-m', type=int, default=5, help='Enter the number of results')

    # getting args
    args = args_parser.parse_args()

    # getting videos by args (video_name, max_results)
    videos = get_videos_by_name(args.video_name, args.m)
    test(videos)


def test(videos):
    # printing videos data
    for video in videos:
        print(f'{videos.index(video) + 1}. {video["title"]}, duration={video["duration"]}')

    # asking user to choose video number
    video_number = int(input("Enter the video number:")) - 1

    # download video
    path = download_audio(videos[video_number])
    print(f'The path to file is "{path}"')

    if input('Enter yY to play it: ') in 'yY':
        thread = Thread(target=play, args=(path,))
        thread.start()

    if input('Enter yY to remove it: ') in 'yY':
        del_files(path)

    if input('Enter yY to repeat: ') in 'yY':
        test(videos)


if __name__ == '__main__':
    main()
