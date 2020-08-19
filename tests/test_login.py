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

    def test_load_login_credentials(self):
        with open(os.path.join(os.path.dirname(__file__), 'credentials.json')) as fname:
            data = json.load(fname)

        self.assertTupleEqual(
            LoginPage(self.driver).load_login_credentials(),
            (data['email'], data['password'])
        )

    def test_login_workana_is_ok(self):
        assert LoginPage(self.driver).is_title_matches(), "Isn't login page..."

        LoginPage(self.driver).fill_input_fields()


if __name__ == "__main__":
    unittest.main(verbosity=2)
