from time import sleep
from selenium.webdriver.common.keys import Keys
import pytest
import pytest_html
from selenium import webdriver
from.selenium.webdriver.chrome.options import Options


# fixture for chrome


class BasicTest:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.baseurl = "http://localhost"
