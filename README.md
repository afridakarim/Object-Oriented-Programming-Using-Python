# Object-Oriented-Programming-Using-Python

Object Oriented Programming (OOP) is using objects and their interactions to create various applications and computer programs.

In this tutorial, I will be explaining and demonstrating four principles in object oriented programming. 
These principles are: encapsulation, abstraction, inheritance, and polymorphism. 



### **Encapsulation:**
Encapsualtion can be understood enclosing something in a capsule. In the case of OOP, this would mean to restrict the state of an object only to one class. This state cannot be accessed by other classes unless allowed through the method function. Encapsulation helps in  preventing accidental data changes in code.

The following is an illustration of encapsulation:
`code`
class Hello:
    def __init__(self, greetings):
        self.a = 'ahoy!'
        self._b = 'What up?'

hello = Hello('name')
print(hello.a)
print(hello.b)
`code`




