# Data Structures
# List
lst = [10, "navadeep", 30.42, True]
print(lst) 
print(type(lst)) # Type of the lst
print(len(lst)) # Length of the lst
print(lst[1]) # indexing
lst[1]='bommarapu' # Mutable
print(lst)

# # List Slicing
print(lst[1:3]) 
print(lst[1: ])
print(lst[:2])

# List Methods
array = [1,2,3,4,5,6]
array.append(7) # add the element at the last
print(array)

array.pop() # removes the last index element
print(array)

array.pop(1) # remove the element at a index
print(array)

array.remove(1) # remove the element occurence in the array
print(array)

array.reverse() # reverse the array
print(array)

array.sort() # sorts the ascending order
print(array)

array.sort(reverse=True) #reverse the array 
print(array)

array.insert(2, 10) # insert the element at the given index
print(array)


# Tuples
tup = (1,2,3,4,3,3)
print(tup)
print(len(tup)) # length of tup
print(type(tup)) # type of tup
print(tup[1]) # indexing
"tup[1] = 3" # tuples are immutable
"tup = (1)" # python consider this as a integer
"tup = (3.4)" # similarly this as float
print(tup[1:3])


# Tuples Methods
print(tup.index(3)) # returns the index of the element in first occurence
print(tup.count(3)) # returns the occurence of the element


# Dictionary
dic = { 
    "name" : "Navadeep",
    "age" : 34,
    "subjects" : ["Web Dev","DBMS","DSA"],
    "topics": ("Javascript", "SQL", "Python"),
    "is_adult" : True,
    "marks" : 40.52,
    
}
print(dic) # returns the dictionary 
print(dic["name"]) # returns the value of the key
print(len(dic)) # returns the length of the dic
print(type(dic)) # returns the type of the dic
print(dic["subjects"]) # returns the list of the subjects
dic["age"] = 20 # mutable
print(dic)


# Nested Dictionaries
student = {
    "name" : "Navadeep",
    "subject-marks": {
        "phy" : 90,
        "chem" : 80,
        "math" : 98
    }
}
print(student) # returns the dicitonary
print(student["subject-marks"]) # returns the dictionary of student-marks
print(student["subject-marks"]["phy"]) # returns the marks of the phy subject in the nested dictionary

# Dictionary Methods
print(dic.keys()) # returns all the keys from the dictionary
print(dic.values()) # returns all the values from the dictionary
print(dic.items()) # returns all the (key,value) pairs
print(dic.get("age")) # gets the value of the key
new_dic = {"city" : "hyderabad"}
dic.update(new_dic) # adds the new dictionary to the previous dictionary
print(dic) 


# Sets
sets = {1, 2, 3, 4, "hello", "world", 6, 10, "world","navadeep"} 
print(sets) # set is the unordered data structure ie, returns the data randomly at random index
print(type(sets)) # returns the type of the sets
print(len(sets)) # ignores the duplicate value from the set
"print(sets[0])" # indexing is not possible in set, ie set is mutable but the elements in set are immutable
collection = set()
print(collection) # to create a empty set
print(type(collection))


# Set Methods
collection.add(1) # adds element in the set
collection.add(2)
collection.add(2) # set contains only unique values
collection.add("navadeep")
collection.add((1,2,3)) 
"collection.add([1,2,3])" # adding lists in set are not possible
print(collection) 
collection.remove(1)
print(collection)
collection.pop() # removes the random value
print(collection) 
print(sets.union(collection)) # combines the sets and collection set
print(sets.intersection(collection)) # returns the common values in both sets
collection.clear() # empties the set
print(collection) 

# Loops
# while loop
n = 1
while n <= 100: # returns numbers 1 to 100
    print(n)
    n+=1

n = 100 
while n>=1: # returns the numbers 100 to 1
    print(n)
    n-=1

n = 1
i = 2
while n <= 10 : # returns the multiple of 2
    print(i * n)
    n+=1
    
lst = []
n = 1
while n <= 10: # adds the squares of 1 to 10 in the list
    lst.append(n*n)
    n+=1
print(lst)

tup =(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 36
n = 0
while n < len(tup): # returns the index of the element in tuple
    if tup[n] == x:
        print("found", n)
    n+=1

num = [1,2,3,4,5]
i = 0
while i < len(num): # return will end the loop
    print(num[i])
    if i == 2:
        break
    i+=1
print("loop ends")

i = 1
while i <= 5: # skips the condition literation
    if i == 3:
        i+=1
        continue
    print(i)
    i+=1

# for loop
num = [1,2,3,4,5]

for i in num: # returns every elements in num array
    print(i)

for i in range(5): # prints numbers from 0 to 4
    print(i)
    
for i in range(1,5): # prints numbers from 1 to 4
    print(i)

for i in range(1,20,2): # prints the numbers from 1 to 19 with jumping 2 numbers 
    print(i)

for i in range(100, 0, -1): #prints the numbers from 100 to 1
    print(i)
    
    
for i in range(10): # pass is a null statement that does nothing, it can be used for future code modification
    pass

n = 50
for i in range(n):
    s = i+n
print(s)


fact = 1
for i in range(1, 6): # print factorial of the number
    if i==0:
        continue
    fact = fact * i
print(fact)

# Function
def sums(a, b): # returns the sum of two numbers
    return a+b

print(sums(2,4))

def listLength(lst):
    count = 0
    for i in range(1,len(lst)+1): # returns the sum of elements in the list
        count+=i
    return count

result = listLength([1,2,3,4,5])
print(result)

def singleLineList(lst): 
    for i in range(1,len(lst)+1): # returns list in the same line
        print(i, end=" ")
    
result = singleLineList([1,2,3,4,5,6])
print(result)

# Recursion function
def show(n): # returns the numbers from n t0 1
    if n == 0: # base case
        return  
    print(n)
    show(n-1)
    
show(4)