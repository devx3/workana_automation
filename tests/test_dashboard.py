'''
Dashboard Tests
Tasks:
- [x] Check if title matches
- [x] Get the Username and Total Amount and then send a Welcome Message
- [x] Get Used Connections and Total Connections
- [x] Make the calc for the number of connection that we'll use on day
        The Formula:

            total available connections / number of days until the end of workdays

            e.g: 25 / 2 (now is thursday morning so we have two entire days to send propose to the
            prospects)

            PS: To get the rest of the days until the end of the week, just take the current day of
            the week - saturday number of the week.

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
from steps.dashboard_page import DashboardPage
from selenium import webdriver
import unittest
import json


class TestDashboard(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://workana.com/login')
        LoginPage(self.driver).start()
        self.dashboard = DashboardPage(self.driver)

    def tearDown(self):
        self.driver.close()

    # def test_is_title_matches(self):
    #     self.assertTrue(self.dashboard._is_title_matches())

    # def test_get_name_and_amount(self):
    #     self.dashboard.collect()
    #     self.assertIsNotNone(self.dashboard.name, msg="Name cannot be None")
    #     self.assertIsNotNone(self.dashboard.total_ammount, msg="total_ammount cannot be None")

    #     self.assertIsInstance(self.dashboard.name, str)
    #     self.assertEqual(self.dashboard.name.upper(), 'LIZ')

    #     self.assertIsNotNone(self.dashboard.total_ammount)
    #     self.assertIsInstance(self.dashboard.total_ammount, float)

    # def test_get_number_of_proposes_to_use(self):
    #     self.dashboard.collect()
    #     self.assertIsInstance(
    #         self.dashboard._number_of_proposes_to_use(self.dashboard.connections_available),
    #         int,
    #         msg="Number of proposes must be an int"
    #     )
    #     self.assertEqual(
    #         self.dashboard._number_of_proposes_to_use(self.dashboard.connections_available),
    #         1
    #     )

    def test_get_num_proposes_of_the_day(self):
        self.dashboard.collect()
        self.assertEqual(self.dashboard.get_num_proposes(), 1)
        pass

    def test_save_num_proposes_of_the_day(self):
        pass


if __name__ == "__main__":
    unittest.main(verbosity=2)
