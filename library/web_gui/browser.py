# noinspection PyUnresolvedReferences
from selenium import webdriver
# noinspection PyUnresolvedReferences
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


class Browser(object):

    def __init__(self, browser_type):
        self.browser_type = browser_type
        self.driver = None

        self.create_driver()

    def create_driver(self):
        if self.browser_type == "chrome":
            self.driver = webdriver.Chrome()
        if self.browser_type == "firefox":
            self.driver = webdriver.Firefox()

    def go_to_url(self, url):
        if self.driver:
            self.driver.get(str(url))
        else:
            raise

    def close(self):
        self.driver.close()
        # self.driver.quit()
