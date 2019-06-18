import pytest
import time
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

    user_data = {
        "first_name": "Mert"
    }
    expected_register_message = "Thank you for registering."

    page_object = PageObject(driver=browser.driver)
    assert expected_register_message in page_object.register_user(user_data)

    browser.close()


class PageObject(object):

    def __init__(self, driver):
        self.driver = driver

    def register_user(self, user_data):
        tab_menu = TabMenu(self.driver)
        tab_menu.click_register_label()

        register_form = RegisterForm(self.driver)
        register_form.fill_register_form(user_data)
        register_form.submit_form()

        register_result_page = RegisterResultPage(self.driver)
        return register_result_page.get_message()


class TabMenu(object):

    def __init__(self, driver):
        self.driver = driver
        self.register_label_path = """/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody//a[text()[contains(., "REGISTER")]]"""

    def get_register_label(self):
        return Label(self.driver, self.register_label_path)

    def click_register_label(self):
        self.get_register_label().click()


class RegisterForm(object):

    def __init__(self, driver):
        self.driver = driver
        self.first_name_textbox_path = "/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[2]/td[2]/input"

        self.submit_button_path = "/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[17]/td/input"

    def get_first_name_textbox(self):
        return Textbox(self.driver, self.first_name_textbox_path)

    def set_first_name_textbox(self, first_name):
        self.get_first_name_textbox().set_text(first_name)

    def fill_register_form(self, form_data):
        self.set_first_name_textbox(form_data["first_name"])

    # self.set_lasT_name_textbox(form_data["last_name"])
    # pass

    def get_submit_button(self):
        return Button(self.driver, self.submit_button_path)

    def submit_form(self):
        self.get_submit_button().click()


class RegisterResultPage(object):

    def __init__(self, driver):
        self.driver = driver
        self.result_message_label_path = "/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[3]/td/p[2]/font"

    def get_result_message_label(self):
        return Label(self.driver, self.result_message_label_path)

    def get_message(self):
        return self.get_result_message_label().get_text()


class Component(object):

    def __init__(self, driver, path):
        self.driver = driver
        self.path = path
        self.element = None

    def get(self):
        if not self.element:
            time.sleep(1)
            self.element = self.driver.find_element_by_xpath(self.path)

        return self.element

    def click(self):
        self.get().click()


class Label(Component):

    def __init__(self, driver, path):
        super(Label, self).__init__(driver, path)

    def get_text(self):
        return self.get().get_attribute("innerHTML")


class Textbox(Component):

    def __init__(self, driver, path):
        super(Textbox, self).__init__(driver, path)

    def set_text(self, text):
        self.get().click()
        self.get().clear()
        self.get().send_keys(str(text))


class Button(Component):

    def __init__(self, driver, path):
        super(Button, self).__init__(driver, path)
