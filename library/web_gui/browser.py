from selenium import webdriver

class Browser(object):

	def __init__(self, type=None):
		self.browser_type = type

	def create_driver(self):
        if self.browser_type == "chrome":
        	self.create_chrome_driver()
            	
	def create_chrome_driver(self):
		driver = webdriver.Chrome()
