# Object-Oriented-Programming-Using-Python

Object Oriented Programming (OOP) is using objects and their interactions to create various applications and computer programs.

In this tutorial, I will be explaining and demonstrating four principles in object oriented programming. 
These principles are: encapsulation, abstraction, inheritance, and polymorphism. 



### **Encapsulation:**
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





