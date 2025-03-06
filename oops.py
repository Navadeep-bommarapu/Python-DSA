# OOPS
# class and object
class Student(): # class
    name = "navadeep"
    age = 20
    
s1 = Student() # object
print(s1.name)
print(s1.age)

s2 = Student() # object
print(s2.name)
print(s2.age)

# Constructor (__init__ function)
class Student():
    def __init__(self): # default constructors
        pass
    # parameterized constructors
    def __init__(self,name, marks): # constructor / self is the current instance of the class
        self.name = name
        self.marks = marks
    
s1 = Student("navadeep", 90) # object
print(s1.name, s1.marks)

s2 = Student("arjun", 87) # object
print(s2.name, s2.marks)


# Attributes
class Student():
    college_name = "Parul University" # Class attribute
    name = "anonymous"
    def __init__(self): # default constructors
        pass
    # parameterized constructors
    def __init__(self,name, marks): # constructor / self is the current instance of the class
        self.name = name
        self.marks = marks
        
s1 = Student("navadeep", 90)
print(s1.name, s1.marks) # s1.name, s1.marks are the instance attribute (object attribute)

print(s1.name) # object attr > class attr
print(s1.college_name)
print(Student.college_name)


# Methods
class Student():
    def __init__(self,name, marks): 
        self.name = name
        self.marks = marks
        
    def welcome(self): # method
        print("Welcome", self.name)
    
    def get_marks(self): # method
        print(self.marks)
        
s1 = Student("navadeep", 90)
s1.welcome()
s1.get_marks()
