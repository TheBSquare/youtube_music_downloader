from argparse import ArgumentParser
from yt_parser import get_videos_by_name, download_audio


def main():
    # creating arg parser
    args_parser = ArgumentParser(description='')
    args_parser.add_argument('video_name', type=str, help='Enter the name of the youtube video')
    args_parser.add_argument('-m', type=int, default=5, help='Enter the number of results')

    # getting args
    args = args_parser.parse_args()

    # getting videos by args (video_name, max_results)
    videos = get_videos_by_name(args.video_name, args.m)

    # printing videos data
    for video in videos:
        print(f'{videos.index(video)+1}. {video["title"]}, duration={video["duration"]}')

    # asking user to choose video number
    video_number = int(input("Enter the video number:")) - 1

    # download video
    download_audio(videos[video_number])


if __name__ == '__main__':
    main()