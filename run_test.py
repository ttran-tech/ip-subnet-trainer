# This file contains the main source code to run
# all the unit test in /test folder.
import unittest
from tests.test_utils import TestUtils
from tests.test_generator import TestGenerator
from tests.test_calculator import TestCalculator

if __name__ == "__main__":
    unittest.main(verbosity=2)