from selenium.webdriver.common.keys import Keys
from common.locators import LoginPageLocators
from steps.base_page import BasePage
import json
import os


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.start()

    def start(self):
        self.email, self.password = self.load_login_credentials()

    def load_login_credentials(self):
        with open(os.path.join(os.getcwd(), 'config.json')) as f_config:
            config = json.load(f_config)
            email = config['email']
            password = config['password']

        return email, password

    def is_title_matches(self):
        return 'Acesse sua Conta' in self.driver.page_source

    def fill_input_fields(self):
        try:
            email_element = self.driver.find_element(*LoginPageLocators.EMAIL_INPUT)
            password_element = self.driver.find_element(*LoginPageLocators.PASSWORD_INPUT)

            email_element.send_keys(self.email)
            password_element.send_keys(self.password)
            password_element.send_keys(Keys.RETURN)

            return True
        except Exception:
            return False

    def is_logged_in(self):
        if 'dashboard' in self.driver.page_source:
            return True
        return False
