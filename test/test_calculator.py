import unittest
from src.calculator import sum, multiply, divide
from src.calculator import subtrac

class CalculatorTest(unittest.TestCase):

    def test_sum(self):
        assert sum(2,3) == 5 

    def test_subtrac(self):
        assert subtrac(10, 5) == 5

    def test_multiply(self):
        assert multiply(3,2) == 6

    def test_divide(self):
        result = divide(10,2)
        expected = 5
        assert result == expected

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)