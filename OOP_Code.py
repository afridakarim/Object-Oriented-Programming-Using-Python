from abc import ABC, abstractmethod
#Encapsulation
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

#Abstraction


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

#Inheritance
class Person( object ):               
        def __init__(self, name, idnumber):    
                self.name = name 
                self.idnumber = idnumber 
        def display(self): 
                print(self.name) 
                print(self.idnumber) 
  
 
class Employee( Person ):            
        def __init__(self, name, idnumber, salary, post): 
                self.salary = salary 
                self.post = post 
   
                Person.__init__(self, name, idnumber)  
  
                  
a = Person('Bob', 239619)      
a.display() 

#Polymorphism
class Bird:
     def intro(self):
       print("There are different types of birds")
 
     def flight(self):
       print("Most of the birds can fly but some cannot")
 
class parrot(Bird):
     def flight(self):
       print("Parrots can fly")
 
class penguin(Bird):
     def flight(self):
       print("Penguins do not fly")
 
obj_bird = Bird()
obj_parr = parrot()
obj_peng = penguin()
 
obj_bird.intro()
obj_bird.flight()
 
obj_parr.intro()
obj_parr.flight()
 
obj_peng.intro()
obj_peng.flight()
