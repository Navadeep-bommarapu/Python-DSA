# taking list as input
name = input("enter the list: ").split(" ")
print(name)
print(type(name))


# String
fname = "Navadeep"
lname = "Bommarapu"
name = fname + " " + lname #String concatenation
print(name) 
print(name[3]) # indexing
print(name[1:10]) # slicing from index 1 to 9 (since python doesnot include the end index)
print(name[:10]) # slicing from index 0 to 9
print(name[5:]) # slicing from index 5 to end
print(name[0: -1]) # negative indexing
print(name[-9: -3]) # negative indexing from index -9 to -2
print(len(name)) # length of the string

# Integer
num = 20
print(num)
print(type(num)) # type of num

# Float
number = 30.34
print(number)
print(type(number)) # type of number
print(num + number) # Add operation
print(num - number) # Subtract
print(num * number) # Multiple
print(num / number) # Divide
print(num % number) # Modulus

# Boolean
a = 3
b = 4
print(a > b) # returns boolean value
print(a == b)
print(a < b)


# Conditional Statement
age = 20

if age < 13:
    print("Todler")
elif 13 <= age <= 18:
    print("Teenager")
elif 18 < age <= 50:
    print("Adult")
else:
    print("Olderly")

# Nesting Conditional Statement
number = 0

if number < 0:
    print("Negative number: ", number)
    if number < -50:
        print("Lesser than -50: ",number)
    else:
        print("Greater than -50: ",number)
elif number > 0:
    print("Positive Number")
    if number < 50:
        print("Lesser than 50: ", number)
    else:
        print("Greater than 50: ",number)
else:
    print("Number is 0")
        