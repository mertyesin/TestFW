import pytest
import json
import highlight
from library import *


# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys


@pytest.mark.skip(reason="no way of currently testing this")
def test_guru99():
    browser = Browser("chrome")
    browser.go_to_url("http://demo.guru99.com/test/newtours/index.php")

    home_page_elements = browser.driver.find_elements_by_xpath(
        "/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td[1]/a")
    if len(home_page_elements) > 0:
        text = home_page_elements[0].click()

    sign_on_elements = browser.driver.find_elements_by_xpath(
        "/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[3]/td/p/font/b")
    if len(sign_on_elements) > 0:
        text = sign_on_elements[0].text
        highlight.highlight(sign_on_elements[0])
        assert text == "Welcome back to Mercury Tours!"
    time.sleep(1)
    browser.close()


def test_guru98():
    browser = Browser("chrome")
    browser.go_to_url("http://demo.guru99.com/test/newtours/index.php")

    with open("/home/mert/Documents/Training/TestFW/library/web_gui/user_data.json", "r") as json_file:
        user_data = json.loads(json_file.read())

    expected_register_message = "Thank you for registering."

    page_object = PageObject(driver=browser.driver)
    assert expected_register_message in page_object.register_user(user_data["registerInfo"])

    browser.close()
