from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from time import sleep, ctime
from collections import namedtuple
from threading import Thread
from os.path import isfile
import csv


BANDCAMP_FRONTPAGE = 'https://bandcamp.com/'


class BandLeader():
    def __init__(self):
        # create a headless browser
        opts = Options()
        opts.set_headless()
        self.browser = Firefox(options=opts)
        self.browser.get(BANDCAMP_FRONTPAGE)

        # track list related state
        self._current_track_number = 1
        self.track_list = []

    # def tracks(self):
    #     '''Query the page to populate a list of available tracks'''

    #     # Sleep to give the browser time to render  and finish any animations
    #     sleep(1)

    #     # Get the container for the visible track list
    #     discover_section = self.browser.find_element_by_class_name(
    #         'discover-results')
    #     left_x =
