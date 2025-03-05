#/bin/usr/python
import unittest
from trainer.utils import *


class TestUtils(unittest.TestCase):
    def test_binary_to_decimal(self):
        self.assertEqual(binary_to_decimal("11000000"), 192, "Binary and decimal are not equal")
        self.assertEqual(binary_to_decimal("11111111"), 255, "Binary and decimal are not equal")        
        self.assertEqual(binary_to_decimal("10101000"), 168, "Binary and decimal are not equal")
        

if __name__ == "__main__":
    print_banner()
    unittest.main()