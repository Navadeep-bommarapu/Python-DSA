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

reverse(int(input()))



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
        
result = palindrome(303)
print(result)
# Output: True