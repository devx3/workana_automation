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

from persisters.config import Config
import unittest
import json


class TestConfigPersister(unittest.TestCase):
    def setUp(self):
        self.config = Config()
        self.config.up()

    def test_create_file_if_not_exists(self):
        self.config.create_file()

    def test_if_config_file_exists(self):
        self.assertTrue(self.config.file_exists())

    def test_attribute_of_get_must_be_a_string(self):
        with self.assertRaises(AssertionError):
            self.config.get(1234)

    def test_attribute_of_get_need_to_have_dot(self):
        with self.assertRaises(AssertionError):
            self.config.get('connections')

    def test_get_config_total_connections(self):
        self.assertEqual(self.config.get('connections.total'), '5')

    def test_get_config_current_connections(self):
        self.assertEqual(self.config.get('connections.current'), '5')

    def test_get_config_times_a_day(self):
        self.assertEqual(self.config.get('connections.times_a_day'), '3')

    def test_update_configuration_attribute_need_to_have_dot(self):
        with self.assertRaises(AssertionError):
            self.config.update('connections', 'test')

    def test_update_configuration_value(self):
        self.assertTrue(self.config.update('connections.total', '5'))


if __name__ == "__main__":
    unittest.main(verbosity=2)
