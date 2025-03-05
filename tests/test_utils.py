# This file contains the unit test for utility functions from utils.py
from src.utils import *
import unittest

class TestUtils(unittest.TestCase):
    """Unit test for utility functions defined in utils.py"""
    # def test_print_banner(self):
    #     print_banner()

    def test_binary_to_decimal(self):
        self.assertEqual(binary_to_decimal("11000000"), 192, "Binary and decimal are not equal")
        self.assertEqual(binary_to_decimal("11111111"), 255, "Binary and decimal are not equal")        
        self.assertEqual(binary_to_decimal("10101000"), 168, "Binary and decimal are not equal")