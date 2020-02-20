# Object-Oriented-Programming-Using-Python

Object Oriented Programming (OOP) is using objects and their interactions to create various applications and computer programs.

In this tutorial, I will be explaining and demonstrating four principles in object oriented programming. 
These principles are: encapsulation, abstraction, inheritance, and polymorphism. 



### Encapsulation
Encapsualtion can be understood enclosing something in a capsule. In the case of OOP, this would mean to restrict the state of an object only to one class. This state cannot be accessed by other classes unless allowed through the method function. Encapsulation helps in  preventing accidental data changes in code.

The following is an illustration of encapsulation:
```code
class Hello:
    def __init__(self, greetings):
        self.a = 'ahoy!'
        self._b = 'What up?'

hello = Hello('name')
print(hello.a)
print(hello.b)
```
Notice the underscore in second variable. This underscore indicates that the variable is encapsulated, hence cannot be called. If this is printed, we would get an error:
``` AttributeError: 'Hello' object has no attribute 'b' ```
To call the encapsulated method, we would use a setter and getter function. This will help us manually call the method:
```
class Hello:
    def __init__(self, greetings):
        self.a = 'ahoy!'
        self._b = 'What up?'

    def set_b(self, value):
        self._b = value

    def get_b(self):
        return self._b

hello = Hello('name')

print(hello.a)
print(hello.get_b())

```
### Abstraction
In OOP, abstraction is used to simplify features without the complex details or explanations. It aids in modeling classes appropirate to the problem. The high-level mechanism of objects are exposed, but this mechanism should hide implemented details.

The following is an illustration of abstraction:
```
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self): pass

class Square(Shape):
    def __init__(self, side):
        self.__side = side

    def area(self):
        return self.__side * self.__side

square = Square(2)
print(square.area())
```
In the above illustrated code, there are several points to be made. The code uses abstract classes and abstract methods. Abstract classes contain one or more abstract method. Abstract methods are declared, but they contain no implementation. Abstract classes may not have an instance and therefore require subclasses. The subclasses provide implementations for the abstract method. 



