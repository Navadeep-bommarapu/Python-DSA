# OOPS
# class and object
<<<<<<< HEAD
# class Student(): # class
#     name = "navadeep"
#     age = 20
    
# s1 = Student() # object
# print(s1.name)
# print(s1.age)

# s2 = Student() # object
# print(s2.name)
# print(s2.age)

# Constructor (__init__ function)
class Student():
=======
class Student: # class
    name = "navadeep"
    age = 20
    
s1 = Student() # object
print(s1.name)
print(s1.age)

s2 = Student() # object
print(s2.name)
print(s2.age)

# Constructor (__init__ function)
class Student:
>>>>>>> 0a48baa (DSA)
    def __init__(self,name, marks): # constructor / self is the current instance of the class
        self.name = name
        self.marks = marks
    
s1 = Student("navadeep", 90) # object
print(s1.name, s1.marks)

s2 = Student("arjun", 87) # object
<<<<<<< HEAD
print(s2.name, s2.marks)
=======
print(s2.name, s2.marks)

# Attributes
class Student:
    college_name = "Parul University" # Class attribute
    name = "anonymous" # class attribute
    # default constructor
    def __init__(self): 
        pass
    
    # parameterized constructor
    def __init__(self,name,marks): 
        self.name = name
        self.marks = marks
    

s1 = Student("navadeep", 90)
print(s1.name, s1.marks) # name and marks are object attribute
print(s1.name) # object attr > class attr
print(s1.college_name)

# Methods
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def welcome(self): # method
        print("Welcome", self.name)
        
    def get_marks(self): # method
        print(self.marks)
    
s1 = Student("navadeep", 90)
s1.welcome()
s1.get_marks()


# marks average
class Student:
    def __init__(self, name, sub1, sub2, sub3): # returns the average marks of the student
        self.name = name
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3
        
    def avgMarks(self):
        avg = (self.sub1 + self.sub2 + self.sub3)/3
        return avg
        
s1 = Student("navadeep", 90, 89, 70)
print(s1.sub1,s1.sub2,s1.sub3)
print(s1.avgMarks())

class Student:
    def __init__(self, name, marks): # returns the average marks of the student
        self.name = name
        self.marks = marks
        
    def avgMarks(self):
        add = 0
        for i in range(0,len(self.marks)):
            add += self.marks[i]
        avg = add/3
        return avg
        
s1 = Student("navadeep", [90, 89, 70])
print(s1.marks)
print(s1.avgMarks())


# Static methods
class Student:
    @staticmethod # decorator
    def college():
        print("Parul University")
    
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        
s1 = Student("navadeep", 90)
print(s1.name, s1.marks)
s1.college()


# Account in which debit, crebit and show balance 
class Account:
    def __init__(self, bal, acc):
        self.bal = bal
        self.acc = acc
        
    def debit(self, mon):
        self.bal -= mon
        return self.bal
    
    def credit(self,mon):
        self.bal += mon
        return self.bal
        
    def showBalance(self):
        print("Total balance: ", self.bal)
    
a1 = Account(1000,349239201)
a1.showBalance()
print(a1.debit(300))
print(a1.credit(200))
a1.showBalance()
>>>>>>> 0a48baa (DSA)
