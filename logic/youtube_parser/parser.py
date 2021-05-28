from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from time import sleep


class YoutubeParser:
    __options = Options()
    __options.headless = True

    def __init__(self):
        self.__driver = Firefox(options=self.__options)

    def get_videos_by_name(self, name, amount=1):
        self.__driver.get(f'https://www.youtube.com/results?search_query={name}&sp=EgIQAQ%253D%253D')
        sleep(2)
        videos = []
        height = 0
        for x in range(1, amount+1):
            video_section = self.__driver.find_element_by_css_selector(
                f'#contents > ytd-item-section-renderer:nth-child({x})')
            for video in video_section.find_elements_by_css_selector(f'#contents > ytd-video-renderer'):
                videos.append({
                    'title': video.find_element_by_css_selector('#video-title').text,
                    'link': video.find_element_by_css_selector('#video-title').get_attribute('href'),
                    'views': video.find_element_by_css_selector('#metadata-line > span:nth-child(1)').text,
                    'upload_time': video.find_element_by_css_selector('#metadata-line > span:nth-child(2)').text,
                    'channel_name': video.find_element_by_css_selector('#channel-info').text,
                    'channel_link': video.find_element_by_css_selector('#text > a').get_attribute('href'),
                    'channel_img_link': video.find_element_by_css_selector(
                        '#channel-info > a > yt-img-shadow > img').get_attribute('src'),
                    'duration': video.find_element_by_css_selector(
                        '#overlays > ytd-thumbnail-overlay-time-status-renderer > span').text,
                    'description': video.find_element_by_css_selector('#description-text').text,
                    'preview_link': video.find_element_by_css_selector(
                        '#thumbnail > yt-img-shadow > img').get_attribute('src')
                })
                self.__driver.execute_script(f"window.scrollTo(0, {height});")
                height += 250
                sleep(.1)
        return videos

    def exit(self):
        self.__driver.close()
        self.__driver.quit()
