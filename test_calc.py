# import unittest
# import calculator

import sys
sys.path.append(/Users/sumukhbhandarkar/Desktop/Python Demo)
import update

class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(1, 5), 6)
        self.assertEqual(calculator.multiply(2, 4), 10)
