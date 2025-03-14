# count digits
def count_digit(num):
    count = 0
    for i in str(num):
        num = int(num/10)
        count+=1
    print("The number of digits :",count)

count_digit(int(input()))


# reverse a number
def reverse(num):
    for i in str(num):
        last = num % 10
        num = int(num/10)
        print(last, end="")

reverse(123)



# check the digit in num can divisible by num           
def count_digit(num):
    count = 0
    temp = num
    while temp > 0:
        last = temp % 10
        if last != 0 and num % last == 0:
            count+=1
        temp = int(temp/10)
    print("The number of digits :",count)
count_digit(5555)

# Checking palindrome
def palindrome(n):
    num = str(n)
    if num == num[::-1]:
        return True
    else:
        return False

def palindrome(n): # Another solution
    temp = n
    rev = 0
    while temp > 0:
        last = temp % 10
        temp = int(temp/10)
        rev = (rev * 10) + last
    if n == rev:
        return True
    else:
        return False        
result = palindrome(3030)
print(result)


# # Armstrong Number
def armstrong_num(n):
    temp = n
    add = 0
    while temp > 0:
        last = temp % 10
        temp = int(temp/10)
        add = add + (last ** 3)
    if add == n:
        return f"{n} is the armstrong number"
    else:
        return f"{n} is not the armstrong number"

result = armstrong_num(153)
print(result)

# Print all divisor
def divisor(n):
    for i in range(1,n+1):
        if n % i == 0:
            print(i)
            
import math
def divisor(n): # Another solution
    num = []
    s = int(math.sqrt(n))
    for i in range(1,s+1):
        if n % i == 0:
            num.append(i)
            if n/i != i:
                num.append(int(n/i))
    num.sort()
    return num
result = divisor(50)
print(result)


# Prime number      
def is_prime(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True        
       
       
def is_prime(n):
    count = 0
    for i in range(1,n+1):
        if n % i == 0:
            count+=1
        
    if count == 2:
        return False
    else:
        return True
result = is_prime(4)
print(result)


# Greatest Common Divisor
def gcf(n,m):
    num = []
    if n > m:
        for i in range(1,n+1):
            if n % i == 0 and m % i == 0:
                num.append(i)
    elif m > n:
        for i in range(1,n+1):
            if n % i == 0 and m % i == 0:
                num.append(i)
    else:
        num.append(n)
    num.sort()
    return num.pop()

def gcf(n,m): # Another Solution
    gcf = 1 
    for i in range(1,min(n,m)+1):
        if n % i == 0 and m % i == 0:
            gcf = i
    return gcf


def gcf(n,m): # Another solution
    gcf = 1
    for i in range(min(n,m), 0, -1):
        if n % i == 0 and m % i == 0:
            gcf = i
    return gcf


def gcf(n,m): # euclidean algorithm
    while n > 0 and m > 0:
        if n > m:
            n = n % m 
        else:
            m = m % n
    if n == 0:
        return m
    else:
        return n

result = gcf(30,15)
print("Greatest Common Divisor:",result)
    