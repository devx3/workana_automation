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

    def test_login_workana_is_ok(self):
        login = LoginPage(self.driver)
        assert login.is_title_matches(), "Isn't login page..."

        # Check if email and password is not blank
        self.assertNotEqual(
            login.email,
            '',
            msg="Email não pode ser vazio"
        )
        self.assertNotEqual(
            login.password,
            '',
            msg="Password não pode ser vazio"
        )

        # Check if credentials matches
        with open(os.path.join(os.path.dirname(__file__), 'credentials.json')) as fname:
            data = json.load(fname)

        self.assertTupleEqual(
            (login.email, login.password),
            (data['email'], data['password'])
        )

        # Check if has error on fill the fields
        self.assertTrue(
            login.fill_input_fields(),
            msg="Erro ao preencher campos"
        )

        # Check if is logged in
        self.assertTrue(
            login.is_logged_in(),
            msg="Erro: Não estamos logados"
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
