from selenium import webdriver

class Browser(object):

    def __init__(self, type=None):
        self.browser_type = type

    def create_driver(self):
        if self.browser_type == "chrome":
            return webdriver.Chrome()