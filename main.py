#!/usr/bin/env python3
from logic.files_handler import convert_to_mp3, del_files
from logic.youtube_scripts import YoutubeParser, download_video


def main():
    # youtube parser
    parser = YoutubeParser('logic/youtube_scripts/drivers/chromedriver')

    # asking user for some vars
    video_name = input('Enter the name of youtube video: ')
    max_results = int(input('Enter the number of max results: '))

    # getting videos
    videos = parser.get_videos_by_name(video_name, max_results)

    # closing parser
    parser.exit()

    # printing videos data
    for video in videos:
        print(f'{videos.index(video) + 1}. {video["title"]}, {video["duration"]}')

    # asking user to choose video number
    video_number = int(input("Enter the video number:")) - 1

    # download video
    mp4 = download_video(videos[video_number])
    print(f'Downloaded file "{mp4}"')

    # convert video to mp3
    mp3 = convert_to_mp3(mp4)
    print(f'Converted "{mp4}" to "{mp3}"')

    if input(f'Input y/Y to del {mp4}: ') in 'yY':
        del_files(mp4)
        print(f'Removed file {mp4}')

    if input(f'Input y/Y to del {mp3}: ') in 'yY':
        del_files(mp3)
        print(f'Removed file {mp3}')


if __name__ == '__main__':
    main()
