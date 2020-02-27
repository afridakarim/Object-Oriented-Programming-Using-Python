[![Build Status](https://travis-ci.org/afridakarim/Object-Oriented-Programming-Using-Python.svg?branch=master)](https://travis-ci.org/afridakarim/Object-Oriented-Programming-Using-Python)
# Object-Oriented-Programming-Using-Python

Object Oriented Programming (OOP) is using objects and their interactions to create various applications and computer programs.

In this tutorial, I will be explaining and demonstrating four principles in object oriented programming. 
These principles are: encapsulation, abstraction, inheritance, and polymorphism. 

### Encapsulation
Encapsualtion can be understood enclosing something in a capsule. In the case of OOP, this would mean to restrict the state of an object only to one class. This state cannot be accessed by other classes unless allowed through the method function. Encapsulation helps in  preventing accidental data changes in code.

The following is an illustration of encapsulation:
https://github.com/afridakarim/individual_project_1/blob/master/MathOperations/subtraction.py

Here the ```def difference(minuend, subtrahend)``` the  ```minuend/subtrahend```  is encapsulated within the ```difference``` function
As stated above, this cannot be accessed by other classes unless allowed.




### Abstraction
In OOP, abstraction is used to simplify features without the complex details or explanations. It aids in modeling classes appropirate to the problem. The high-level mechanism of objects are exposed, but this mechanism should hide implemented details.

The following is an illustration of abstraction:
https://github.com/afridakarim/individual_project_1/blob/master/Calculator/Calculator.py

In the code below:
```def Difference(self, a, b):
        self.Result = Subtraction.difference(a, b)
        return self.Result
```
Here all the ```Difference``` function needs to call is  the ```difference``` function from ```MathOperations```

### Inheritance
Inheritance is used to form new classes from already defined classes. The base classes (where all methods and properties are derived from) are called parent classes. Where as, the derived classes (newly formed classes) are called child classes. By using inheritance, one does not need to keep rewriting similar class strucutures and it reduces the complexity of a program. 

The following is an illustration of inheritance:

https://github.com/afridakarim/individual_project_1/blob/master/Tests/test_MathOperations.py

In the code below:
```
 def test_MathOperations_subtraction(self):
        self.assertEqual(-1, Subtraction.difference(1, 2))
```
```def test_MathOperations_subtraction(self)``` is a new function, but it inherits the parent ```Subtraction.difference``` functions and makes a new execution



### Polymorphism
In inheritane we have the ability to derive methods from the parent class into the child class. But the issue comes when you want to derive multiple methods but wish to change up some things in the new class. This is where polymorphism comes to play. Coming from the greek words 'Poly' (many) and 'morphism' (forms), it helps to use the same function name with different signatures for different types of child classes. In all, polymorphism allows us to define a child class with the same name as defined in the parent class.  

The following is an illustration of polymorphism:

https://github.com/afridakarim/individual_project_1/blob/master/Tests/test_Calculator.py

```def test_multiple_calculators(self):
        calculator1 = Calculator()
        calculator2 = Calculator()
        self.calculator.Sum(calculator1.Sum(1, 2), calculator2.Difference(3, 4))
        self.assertEqual(2, self.calculator.Result)
```
In the above code, the ```Calculator()``` is called twice, but used in different context

---------




