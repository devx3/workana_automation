'''
Dashboard Tests
Tasks:
- [ ] Get the Username and Total Amount and then send a Welcome Message
- [ ] Get Used Connections and Total Connections
- [ ] Make the calc for the number of connection that we'll use on day
        The Formula:

            total available connections / number of days until the end of workdays

            e.g: 25 / 2 (now is thursday morning so we have two entire days to send propose to the
            prospects)

- [ ] Save the number of proposes done of the day (this is used to manage how much proposes we need
      to do)
- [ ] Go to Projects Page...
'''
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
        self.login = LoginPage(self.driver).start()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)
