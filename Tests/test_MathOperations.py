import unittest

from MathOperations.addition import Addition
from MathOperations.subtraction import Subtraction
from MathOperations.multiplication import Multiplication
from MathOperations.division import Division
from MathOperations.exponent import Exponent
from MathOperations.root import Root
from MathOperations.logarithm import Logarithm


class MyTestCase(unittest.TestCase):

    def test_MathOperations_addition(self):
        self.assertEqual(3, Addition.sum(1, 2))

    def test_MathOperations_subtraction(self):
        self.assertEqual(-1, Subtraction.difference(1, 2))

    def test_MathOperations_multiplication(self):
        self.assertEqual(4,Multiplication.product(2,2))

    def test_MathOperations_division(self):
        self.assertEqual(3, Division.quotient(6,2))

    def test_MathOperations_exponent(self):
        self.assertEqual(4, Exponent.power(2,2))

    def test_MathOperations_root(self):
        self.assertEqual(1, Root.root(1))

    def test_MathOperations_log(self):
        self.assertEqual(4,Logarithm.log(16,2))

    def test_MathOperations_sum_list(self):
        valuelist = [1, 2, 3]
        self.assertEqual(6, Addition.sum(valuelist))



if __name__ == '__main__':
    unittest.main()