try:
    import sys
    import os
    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '..'
            )
        )
    )

except Exception:
    pass

from steps.login_page import LoginPage
from selenium import webdriver
import unittest
import json


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://workana.com/login')

    def tearDown(self):
        self.driver.close()

    def test_is_title_not_match(self):
        with self.assertRaises(AssertionError):
            self.driver.get('https://workana.com')
            login = LoginPage(self.driver)

    def test_email_and_password_could_not_be_empty_or_integer(self):
        with self.assertRaises(AssertionError):
            LoginPage(self.driver, password='umasenhaaqui')

        with self.assertRaises(AssertionError):
            LoginPage(self.driver, email='algumemail@qualquer.com', password=123456)

        with self.assertRaises(AssertionError):
            LoginPage(self.driver, email='')

        with self.assertRaises(AssertionError):
            LoginPage(self.driver, email=True, password=123456)

    def test_login_workana_is_not_ok(self):
        with self.assertRaises(AssertionError):
            LoginPage(self.driver, 'umemailqualquer@aqui.com', 'senhadodjanho')

    def test_login_workana_is_ok(self):
        login = LoginPage(self.driver)

        # Check if credentials matches
        with open(os.path.join(os.path.dirname(__file__), 'credentials.json')) as fname:
            data = json.load(fname)

        self.assertTupleEqual(
            (login.email, login.password),
            (data['email'], data['password'])
        )

        # Check if is logged in
        self.assertTrue(
            login._is_logged_in(),
            msg="Erro: Não estamos logados"
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
