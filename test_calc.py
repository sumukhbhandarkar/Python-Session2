import unittest
import calculator


class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(1, 5), 6)
