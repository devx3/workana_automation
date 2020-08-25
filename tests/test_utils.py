''' Remember: Saturday is the 5th day of the week '''
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

from common.utils import get_remaining_days_until_saturday, \
    get_remaining_proposes_per_day
from datetime import datetime
import unittest
import math


class TestUtils(unittest.TestCase):

    def test_remaining_days_until_saturday_must_raise_an_error_if_date_is_not_string(self):
        with self.assertRaises(AssertionError):
            get_remaining_days_until_saturday(123)

    def test_get_remaining_days_until_saturday(self):
        self.assertIsInstance(
            get_remaining_days_until_saturday(),
            int,
            msg="Remaining days must be an int"
        )
        self.assertEqual(get_remaining_days_until_saturday(), 5 - datetime.today().weekday())

    def test_get_remaining_days_must_not_return_zero(self):
        self.assertNotEqual(get_remaining_days_until_saturday("2020-08-29"), 0)

    def test_get_remaining_proposes(self):
        self.assertIsInstance(
            get_remaining_proposes_per_day(25),
            int,
            msg="Remaining proposes must return INT"
        )
        for i in range(5, 130):
            with self.subTest(i=i):
                self.assertEqual(
                    get_remaining_proposes_per_day(i),
                    math.floor(i / (5 - datetime.today().weekday()))
                )


if __name__ == "__main__":
    unittest.main(verbosity=2)
