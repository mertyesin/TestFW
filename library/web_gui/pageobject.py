import time
import json

with open("/home/mert/Documents/Training/TestFW/library/web_gui/object_repository.json", "r") as json_file:
    object_repository = json.loads(json_file.read())
print(object_repository["MainPage"][0]["register"])

countryList = {'ALBANIA': '1', 'ALGERIA': '2', 'AMERICAN SAMOA': '3'}


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
        self.register_label_path = object_repository["MainPage"][0]["register"]

    def get_register_label(self):
        return Label(self.driver, self.register_label_path)

    def click_register_label(self):
        self.get_register_label().click()


class RegisterForm(object):

    def __init__(self, driver):
        self.driver = driver
        self.first_name_textbox_path = object_repository["MainPage"][0]["registerPage"][0]["first_name_textbox_path"]
        self.last_name_textbox_path = object_repository["MainPage"][0]["registerPage"][0]["last_name_textbox_path"]
        self.phone_textbox_path = object_repository["MainPage"][0]["registerPage"][0]["phone_textbox_path"]
        self.email_textbox_path = object_repository["MainPage"][0]["registerPage"][0]["email_textbox_path"]

        self.address_textbox_path = object_repository["MainPage"][0]["registerPage"][0]["address_textbox_path"]
        self.city_textbox_path = object_repository["MainPage"][0]["registerPage"][0]["city_textbox_path"]
        self.state_textbox_path = object_repository["MainPage"][0]["registerPage"][0]["state_textbox_path"]
        self.postalCode_textbox_path = object_repository["MainPage"][0]["registerPage"][0]["postalCode_textbox_path"]
        self.dropDown_list__path = object_repository["MainPage"][0]["registerPage"][0][
            "dropDown_list__path"]
        self.submit_button_path = object_repository["MainPage"][0]["registerPage"][0]["submit_button_path"]

    def get_first_name_textbox(self):
        return Textbox(self.driver, self.first_name_textbox_path)

    def set_first_name_textbox(self, first_name):
        self.get_first_name_textbox().set_text(first_name)

    def get_last_name_textbox(self):
        return Textbox(self.driver, self.last_name_textbox_path)

    def set_last_name_textbox(self, last_name):
        self.get_last_name_textbox().set_text(last_name)

    def get_phone_textbox(self):
        return Textbox(self.driver, self.phone_textbox_path)

    def set_phone_textbox(self, phone):
        self.get_phone_textbox().set_text(phone)

    def get_email_textbox(self):
        return Textbox(self.driver, self.email_textbox_path)

    def set_email_textbox(self, email):
        self.get_email_textbox().set_text(email)

    def get_address_textbox(self):
        return Textbox(self.driver, self.address_textbox_path)

    def set_address_textbox(self, address):
        self.get_address_textbox().set_text(address)

    def get_city_textbox(self):
        return Textbox(self.driver, self.city_textbox_path)

    def set_city_textbox(self, city):
        self.get_city_textbox().set_text(city)

    def get_state_textbox(self):
        return Textbox(self.driver, self.state_textbox_path)

    def set_state_textbox(self, state):
        self.get_state_textbox().set_text(state)

    def get_postalCode_textbox(self):
        return Textbox(self.driver, self.postalCode_textbox_path)

    def set_postalCode_textbox(self, postalcode):
        self.get_postalCode_textbox().set_text(postalcode)

    def get_country_multiple_selection(self):
        return DropDownList(self.driver, self.dropDown_list__path)

    def set_country_multiple_selection(self, country):
        self.get_country_multiple_selection().set_text(country)

    def fill_register_form(self, form_data):
        self.set_first_name_textbox(form_data[0]["first_name"])
        self.set_last_name_textbox(form_data[0]["last_name"])
        self.set_phone_textbox(form_data[0]["phone"])
        self.set_email_textbox(form_data[0]["email"])
        self.set_address_textbox(form_data[0]["address"])
        self.set_city_textbox(form_data[0]["city"])
        self.set_state_textbox(form_data[0]["state"])
        self.set_postalCode_textbox(form_data[0]["postalCode"])
        self.set_country_multiple_selection(form_data[0]["country"])

    def get_submit_button(self):
        return Button(self.driver, self.submit_button_path)

    def submit_form(self):
        self.get_submit_button().click()


class RegisterResultPage(object):

    def __init__(self, driver):
        self.driver = driver
        self.result_message_label_path = object_repository["MainPage"][0]["registerPage"][1][
            "register_result_message_path"]

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


class DropDownList(Component):

    def __init__(self, driver, path):
        super(DropDownList, self).__init__(driver, path)
        global countryList
        self.path = path

    def set_text(self, text):
        self.path = self.path + "/option[" + countryList[text] + "]"
        self.get().click()


class Button(Component):

    def __init__(self, driver, path):
        super(Button, self).__init__(driver, path)
