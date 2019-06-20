import time


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
        self.last_name_textbox_path = "/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[3]/td[2]/input"
        self.phone_textbox_path = "/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[4]/td[2]/input"
        self.email_textbox_path = "/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[5]/td[2]/input"

        self.submit_button_path = "/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[17]/td/input"

    def get_first_name_textbox(self):
        return Textbox(self.driver, self.first_name_textbox_path)

    def set_first_name_textbox(self, first_name):
        self.get_first_name_textbox().set_text(first_name)

    def get_last_name_textbox(self):
        return Textbox(self.driver, self.last_name_textbox_path)

    def set_last_name_textbox(self, first_name):
        self.get_last_name_textbox().set_text(first_name)

    def get_phone_textbox(self):
        return Textbox(self.driver, self.phone_textbox_path)

    def set_phone_textbox(self, first_name):
        self.get_phone_textbox().set_text(first_name)

    def get_email_textbox(self):
        return Textbox(self.driver, self.email_textbox_path)

    def set_email_textbox(self, first_name):
        self.get_email_textbox().set_text(first_name)

    def fill_register_form(self, form_data):
        self.set_first_name_textbox(form_data[0]["first_name"])
        self.set_last_name_textbox(form_data[0]["last_name"])
        self.set_phone_textbox(form_data[0]["phone"])
        self.set_email_textbox(form_data[0]["email"])

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
