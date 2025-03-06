class Student():
    college_name = "Parul University" # Class attribute
    def __init__(self): # default constructors
        pass
    # parameterized constructors
    def __init__(self,name, marks): # constructor / self is the current instance of the class
        self.name = name
        self.marks = marks
        
s1 = Student("navadeep", 90)
print(s1.name, s1.marks) # s1.name, s1.marks are the instance attribute (object attribute)
