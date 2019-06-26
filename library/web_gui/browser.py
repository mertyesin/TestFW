# noinspection PyUnresolvedReferences
from selenium import webdriver


class Browser(object):

    def __init__(self, browser_type):
        self.browser_type = browser_type
        self.driver = None

        self.create_driver()

    def create_driver(self):
        if self.browser_type == "chrome":
            self.driver = webdriver.Chrome()

    def go_to_url(self, url):
        if self.driver:
            self.driver.get(str(url))
        else:
            raise

    def close(self):
        self.driver.close()
        self.driver.quit()
