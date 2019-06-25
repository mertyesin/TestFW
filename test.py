import pytest
import json
from library import *


def test_guru98():
    browser = Browser("chrome")
    browser.go_to_url("http://demo.guru99.com/test/newtours/index.php")

    with open("/home/mert/Documents/Training/TestFW/library/web_gui/user_data.json", "r") as json_file:
        user_data = json.loads(json_file.read())

    expected_register_message = "Thank you for registering."

    page_object = PageObject(driver=browser.driver)
    assert expected_register_message in page_object.register_user(user_data["registerInfo"])

    browser.close()
