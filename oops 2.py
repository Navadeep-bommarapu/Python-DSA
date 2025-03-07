# del Keyword
class Student:
    def __init__(self,name,age): # Constructor
        self.name = name
        self.age = age
        
s1 = Student("navadeep", 20)
print(s1.name,s1.age)
del s1.name # deletes object attribute
del s1 # deletes object 

# Private attributes and methods
class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass # pribate attr are declared with __ in front
    
    def resetPassword(self): # private attribute are only accessible in class
        return self.__acc_pass

a1 = Account("2341232", "2357344122357908")
print(a1.acc_no) # public attribute
"print(a1.__acc_pass)" # private attribute
print(a1.resetPassword())

class Person:
    __name = "navadeep" # private attr
    
    def __hello(self): # private method
        print("hello", self.__name)
        
    def showName(self):
        return self.__hello()

p1 = Person()
"print(p1.__name)" # cannot access private attr in object other than class
"print(p1.__hello())" # cannot access private method in object other than class
p1.showName()


# Abstraction: showing only the essential features to the user
class Car: 
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
    
    def start(self):
        self.acc = True
        self.clutch = True
        print("Car started")
        
c1 = Car()
c1.start()


# Encapsulation: Wrapping data and functions in a single unit

# Inheritance: class derives the methods and properites of the other class
# Single Inheritance
class Car:
    color = "black"
    
    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stopped")
    
class OtherCar(Car): # Inheritance
    def __init__(self, name):
        self.name = name
        

c1 = OtherCar("bmw")
print(c1.color)
c1.start()
c1.stop()

# Multi-level Inheritance
class Car:
    color = "black"
    
    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stopped")
    
class OtherCar(Car): # Single Inheritance
    def __init__(self,brand):
        self.brand = brand

class BMW(OtherCar): # Multi-level Inheritance: Parent -> Child -> Grandchild -> ...
    def __init__(self, types):
        self.types = types
 

c1 = BMW("petrol", "m5")
print(c1.types)
c1.start()
c1.stop()

# Multiple  Inheritance
class A:
    a = "class A"

class B:
    b = "class B"
    
class C(A,B): # multiple inheritance: mutliple parent properties in the child
    c = "class C"

c1 = C()
print(c1.c) 
print(c1.a) # property of class A (parent)
print(c1.b) # property of class B (parent)

# super() method: used to access methods of the parent class    
class Car: 
    def __init__(self,name):
        self.name = name
        
    @staticmethod
    def start():
        print('starts')
        
    @staticmethod
    def stop():
        print('stops')

class BMW(Car):
    def __init__(self, types, name):
        self.types = types
        super().__init__(name) # super method
        super().start()

c1 = BMW("petrol", "m5")
print(c1.name)


# class method
class Person: # changing a class attr
    name = "anonymous"
    
    "another method"
    # def changeName(self, name):
    #     "self.name = name" # create a seperate name attr in the object instead of changing the class attr
    #     "Person.name = name" # this changes the class attr 
    #     self.__class__.name = name # another way to change class attr

    @classmethod # decorator
    def changeName(cls, name):
        cls.name = name
    
p1 = Person()
p1.changeName("navadeep")
print(p1.name)

# property decorator
class Student:
    def __init__(self, phy, math, chem):
        self.phy = phy
        self.math = math
        self.chem = chem

    "another method"
    # def calculate(self):
    #     return str((self.phy + self.math + self.chem)/3) + "%"
        
    
    @property
    def calculate(self): # this function can be used as property / atrribute
        return str((self.phy + self.math + self.chem)/3) + "%"
    

s1 = Student(90,98,99)
s1.math = 50
"print(s1.calculate())" 
print(s1.calculate) # attr


# Polymorphism: same operator is allowed to have different meaning according to the context
# dunder function
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    
    def showNum(self):
        print(self.real, "i +", self.img, "j")
    
    def __add__(num1, num2): # dunder function (__add__)
        newReal = num1.real + num2.real
        newImg = num1.img + num2.img
        return Complex(newReal, newImg)
    
    def __sub__(num1, num2): # dunder function (__sub__)
        newReal = num1.real - num2.real
        newImg = num1.img - num2.img
        return Complex(newReal, newImg)
    
num1 = Complex(1, 2) # object 1
num1.showNum()

num2 = Complex(4, 6) # object 2
num2.showNum()
        
num3 = num1 + num2 # adds two objects which is possible by dunker functions
num3.showNum()

print(type(num1)) # Complex type, which are not possible to add
