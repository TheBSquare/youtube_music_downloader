from logic import YoutubeParser
from logic import download_from_youtube
from settings import output


def main():
    # youtube parser
    parser = YoutubeParser()

    # asking user for some vars
    video_name = input('Enter the name of youtube video: ')

    # getting videos
    videos = parser.get_videos_by_name(video_name)

    # closing parser
    parser.exit()

    # printing videos data
    for video in videos:
        print(f'{videos.index(video) + 1}. {video["title"]}, {video["duration"]}')

    # asking user to choose video number
    video_number = int(input("Enter the video number:")) - 1

    # ask what to do
    operation = input(f'1. Download video\n'
                      f'2. Download audio\n'
                      f'3. Download both\n'
                      f'Enter the number of the operation: ')
    operations = {
        '1': 'only_video',
        '2': 'only_audio',
        '3': 'both'
    }

    download_from_youtube(videos[video_number]['link'], download_type=operations[operation], output_dir=output)


if __name__ == '__main__':
    main()

