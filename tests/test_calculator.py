# This file contains the unit test for calculator functions from calculator.py
from src.calculator import *
import unittest

class TestCalculator(unittest.TestCase):
    def test_calculate_subnet_mask(self):
        subnet = calculate_subnet_mask('19')
        self.assertEqual(subnet, [255,255,224,0], "Subnet mask does not match")
