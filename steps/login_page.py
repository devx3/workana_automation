from steps.base_page import BasePage
from common.elements import LoginPageElements
import json
import os


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def load_login_credentials(self):
        with open(os.path.join(os.getcwd(), 'config.json')) as f_config:
            config = json.load(f_config)
            email = config['email']
            password = config['password']

        return email, password

    def is_title_matches(self):
        return 'Acesse sua Conta' in self.driver.page_source


if __name__ == "__main__":
    pass