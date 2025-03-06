# OOPS
# class and object
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
    def __init__(self,name, marks): # constructor / self is the current instance of the class
        self.name = name
        self.marks = marks
    
s1 = Student("navadeep", 90) # object
print(s1.name, s1.marks)

s2 = Student("arjun", 87) # object
print(s2.name, s2.marks)