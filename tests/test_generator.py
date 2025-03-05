# This file contains the unit test for generator functions from generator.py
from src.generator import *
import unittest, re

class TestGenerator(unittest.TestCase):
    def test_generate_ip(self):
        ip = generate_ip()
        pattern = r'^(\d{1,3}).(\d{1,3}).(\d{1,3}).(\d{1,3})$'
        self.assertTrue(bool(re.match(pattern, ip)), "IP Address not match.")

    def test_generate_cidr(self):
        cidr = generate_cidr()
        pattern = r'^(\d){1,2}$'
        self.assertTrue(bool(re.match(pattern, cidr)), "Invalid CIDR suffix.")