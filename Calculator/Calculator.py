from MathOperations.addition import Addition
from MathOperations.subtraction import Subtraction
from MathOperations.multiplication import Multiplication
from MathOperations.division import Division
from MathOperations.exponent import Exponent
from MathOperations.root import Root
from MathOperations.logarithm import Logarithm


class Calculator:
    Result = 0

    def __init__(self):
        pass

    def Sum(self, a, b):
        self.Result = Addition.sum(a, b)
        return self.Result

    def Difference(self, a, b):
        self.Result = Subtraction.difference(a, b)
        return self.Result

    def Product(self,a,b):
        self.Result = Multiplication.product(a,b)
        return self.Result

    def Division(self, a,b):
        self.Result = Division.quotient(a,b)
        return self.Result

    def Power(self, a,b):
        self.Result = Exponent.power(a,b)
        return self.Result

    def Root(self,a):
        self.Result = Root.root(a)
        return self.Result

    def Log(self,a,b):
        self.Result = Logarithm.log(a,b)
        return self.Result
