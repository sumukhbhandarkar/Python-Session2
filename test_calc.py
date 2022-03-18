import unittest
import calculator


class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.multiply(1, 4), 4)
