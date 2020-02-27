import unittest

from Calculator.Calculator import Calculator


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_calculator_return_sum(self):
        result = self.calculator.Sum(1, 2)
        self.assertEqual(3, result)

    def test_calculator_return_difference(self):
        result = self.calculator.Difference(1, 2)
        self.assertEqual(-1, result)

    def test_calculator_return_product(self):
        result = self.calculator.Product(2,2)
        self.assertEqual(4,result)

    def test_calculator_return_quotient(self):
        result = self.calculator.Division(6,2)
        self.assertEqual(3,result)

    def test_calculator_return_power(self):
        result = self.calculator.Power(2,2)
        self.assertEqual(4,result)

    def test_calculator_return_root(self):
        result = self.calculator.Root(1)
        self.assertEqual(1,result)

    def test_calculator_return_log(self):
        result = self.calculator.Log(16,2)
        self.assertEqual(4,result)

    def test_calculator_access_difference_result(self):
        self.calculator.Difference(1, 2)
        self.assertEqual(-1, self.calculator.Result)

    def test_calculator_access_sum_result(self):
        self.calculator.Sum(1, 2)
        self.assertEqual(3, self.calculator.Result)

    def test_calculator_access_product_result(self):
        self.calculator.Product(2,2)
        self.assertEqual(4, self.calculator.Result)

    def test_calculator_access_quotient_result(self):
        self.calculator.Division(6,2)
        self.assertEqual(3, self.calculator.Result)

    def test_calculator_access_power_result(self):
        self.calculator.Power(2,2)
        self.assertEqual(4,self.calculator.Result)

    def test_calculator_access_root_result(self):
        self.calculator.Root(1)
        self.assertEqual(1,self.calculator.Result)

    def test_calculator_access_log_result(self):
        self.calculator.Log(16,2)
        self.assertEqual(4,self.calculator.Result)

    def test_multiple_calculators(self):
        calculator1 = Calculator()
        calculator2 = Calculator()
        self.calculator.Sum(calculator1.Sum(1, 2), calculator2.Difference(3, 4))
        self.assertEqual(2, self.calculator.Result)



if __name__ == '__main__':
    unittest.main()