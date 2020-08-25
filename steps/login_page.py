from selenium.webdriver.common.keys import Keys
from common.locators import LoginPageLocators
from steps.base_page import BasePage
import json
import os


class LoginPage(BasePage):

    def __init__(self, driver, email=None, password=None):
        super().__init__(driver)

        self.email, self.password = (email, password)
        if self.email is None and self.password is None:
            self.email, self.password = self._load_login_credentials()

    def start(self):
        ''' Bootstrap of the application '''
        assert self._is_title_matches(), 'Title not match... Is the login page?'
        assert self.email is not None, 'Email cannot be None'
        assert self.password is not None, 'Password cannot be None'
        assert self.email is not '', 'Email cannot be empty'
        assert self.password is not '', 'Password cannot be empty'
        assert isinstance(self.email, str), 'Email must be a String'
        assert isinstance(self.password, str), 'Password must be a String'

        self._fill_input_fields()
        assert self._is_logged_in(), "Credential's Error: We could not login"

    def _load_login_credentials(self):
        ''' Load credentials from config file '''
        with open(os.path.join(os.getcwd(), 'config.json')) as f_config:
            config = json.load(f_config)
            config = config['config']['credentials']
            email = config['email']
            password = config['password']

        return email, password

    def _is_title_matches(self):
        ''' Check if is login page '''
        return 'Acesse sua Conta' in self.driver.page_source

    def _fill_input_fields(self):
        ''' Fill all the input fields to login '''
        try:
            email_element = self.driver.find_element(*LoginPageLocators.EMAIL_INPUT)
            password_element = self.driver.find_element(*LoginPageLocators.PASSWORD_INPUT)

            email_element.send_keys(self.email)
            password_element.send_keys(self.password)
            password_element.send_keys(Keys.RETURN)

            return True
        except Exception:
            return False

    def _is_logged_in(self):
        ''' Check if user has logged with success '''
        assert 'dashboard' in self.driver.page_source
        return True
