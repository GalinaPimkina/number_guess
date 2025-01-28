import unittest
from main import check_value


# python -m unittest test_main

class TestNumber(unittest.TestCase):

    def test_values_false(self):
        self.assertFalse(check_value("ab"), False)
        self.assertFalse(check_value(["ab", "4", 5]), False)

    def test_values_true(self):
        self.assertTrue(check_value("55"), True)
        self.assertTrue(check_value(55), True)