# This file contains the unit test for generator functions from generator.py
from src.generator import *
import unittest, re

class TestGenerator(unittest.TestCase):
    def test_generate_ip(self):
        ip = generate_ip()
        pattern = r'^(\d{1,3}).(\d{1,3}).(\d{1,3}).(\d{1,3})$'
        compiled_p = re.compile(pattern=pattern)

        # print(f"Tesing IP: {ip} | { compiled_p.match(ip) }")
        self.assertTrue(bool(re.match(pattern, ip)), "IP Address not match.")