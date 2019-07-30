# noinspection PyUnresolvedReferences
import pytest
# noinspection PyUnresolvedReferences
import json
from library import *


# @pytest.mark.skip(reason="no way of currently testing this")
def test_guru98():
    with open("/home/mert/Documents/Training/TestFW/library/web_gui/data/test_data.json", "r") as jsonFile:
        test_data = json.loads(jsonFile.read())

    browser_type = test_data["browserType"]
    url = test_data["url"]
    
    browser = Browser(browser_type)
    browser.go_to_url(url)

    expected_register_message = "Thank you for registering."

    page_object = PageObject(driver=browser.driver)
    assert expected_register_message in page_object.register_user(test_data["registerInfo"])

    browser.close()
