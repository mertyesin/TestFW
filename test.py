#!/usr/bin/env python
import pytest
#from selenium import webdriver
import time
import highlight
from library import *

def test_guru99():
	browser = Browser(type="chrome")
	driver = browser.create_driver()
	driver.get("http://demo.guru99.com/test/newtours/index.php")
	
	home_page_elements = driver.find_elements_by_xpath("/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td[1]/a")
	if len(home_page_elements) > 0:
		text = home_page_elements[0].click()
	
	sign_on_elements = driver.find_elements_by_xpath("/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[3]/td/p/font/b")
	if len(sign_on_elements) > 0:
		text = sign_on_elements[0].text
		highlight.highlight(sign_on_elements[0])
		assert text == "Welcome back to Mercury Tours!"
	time.sleep(1)
	driver.close()
