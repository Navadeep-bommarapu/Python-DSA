# Patterns in python

for i in range(5):
    for j in range(5):
        print("*", end="")
    print()
# output:
# *****
# *****
# *****
# *****
# *****


for i in range(5):
    for j in range(i+1):
        print("*", end="")
    print()
# output:
# *
# **
# ***
# ****
# *****


n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end='')
    print()
# output:
# 1
# 12
# 123
# 1234
# 12345


n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i, end="")
    print()
# output:
# 1
# 22
# 333
# 4444
# 55555


n = 5
for i in range(n,0,-1):
    for j in range(i):
        print("*", end="")
    print()
# Output:
# *****
# ****
# ***
# **
# *


n = 5
for i in range(n):
    for j in range(n-i-1,0,-1):
        print(" ",end="")
    for k in range(2*i+1):
        print("*",end="")
    print()
# output:
#     *
#    ***
#   *****
#  *******
# *********


n = 5
for i in range(n,0,-1):
    for j in range(n,i,-1):
        print(" ",end="")
    for k in range(2*i-1):
        print("*",end="")
    print()
# output:
# *********
#  *******
#   *****
#    ***
#     *

n = 5
for i in range(n):
    for j in range(n-i-1,0,-1):
        print(" ",end="")
    for k in range(2*i+1):
        print("*", end="")
    print()
for i in range(n,0,-1):
    for j in range(n,i,-1):
        print(" ",end="")
    for k in range(2*i-1):
        print("*", end="")
    print()
# output:
#     *
#    ***
#   *****
#  *******
# *********
# *********
#  *******
#   *****
#    ***
#     *        

n = 5
for i in range(n+1):
    for j in range(i):
        print("*", end="")
    print()
for i in range(n,0,-1):
    for j in range(i):
        print("*", end="")
    print()
# output:
# *
# **
# ***
# ****
# *****
# *****
# ****
# ***
# **
# *

n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        if (i+j) % 2 == 0: 
            print("1", end="")  
        else: 
            print("0",end="") 
    print()
# output:
# 1
# 01
# 101
# 0101
# 10101

n = 4
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    for k in range(n,i,-1):
        print("  ", end="")
    for j in range(1,i+1):
        print(i-j+1,end="")
    print()
# output:
# 1      1
# 12    21
# 123  321
# 12344321

n = 5
count = 1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(count, end=" ")
        count+=1
    print()
# output:
# 1 
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

n = 5
for i in range(1,n+1):
    for j in range(ord("A"),ord("A")+i):
        print(chr(j),end="")
    print()
# output:
# A
# AB
# ABC
# ABCD
# ABCDE

n = 5
for i in range(n,0,-1):
    for j in range(ord("A"), ord("A") + i):
        print(chr(j),end="")
    print()
# output:
# ABCDE
# ABCD
# ABC
# AB
# A

n = 5
for i in range(n):
    for j in range(i+1):
        print(chr(65 + i), end="")
    print()
# output:
# A
# BB
# CCC
# DDDD
# EEEEE


n=5
for i in range(1,n+1):
    for j in range(n-i,0,-1):
        print(" ",end="")
    for k in range(i):
        print(f"{chr(65 + k)}", end="")
    for l in range(i-1,0,-1):
        print(chr(64 + l), end="")
    print()
# output:
#     A
#    ABA
#   ABCBA
#  ABCDCBA
# ABCDEDCBA

n=5
for i in range(1,n+1):
    for j in range(ord("F"), ord("F") + i):
        print(chr(j-i), end="")
    print()
# output:
# E
# DE
# CDE
# BCDE
# ABCDE

n = 5
for i in range(n):
    for j in range(n-i,0,-1):
        print("*", end="")
    for k in range(i):
        print("  ",end="")
    for l in range(n-i,0,-1):
        print("*", end="")
    print()
for i in range(n,0,-1):
    for j in range(n-i+1,0,-1):
        print("*", end="")
    for k in range(i-1):
        print("  ",end="")
    for l in range(n-i+1,0,-1):
        print("*", end="")
    print()
# output:
# **********
# ****  ****
# ***    ***
# **      **
# *        *
# *        *
# **      **
# ***    ***
# ****  ****
# **********


n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*", end="")
    for k in range(2*(n-i)):
        print(" ",end="")
    for l in range(1,i+1):
        print("*", end="")
    print()
for i in range(n-1,0,-1):
    for j in range(i):
        print("*", end="")
    for k in range(2*(n-i)):
        print(" ",end="")
    for l in range(i):
        print("*", end="")
    print()
# output
# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *

n = 5
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == 1 or j == 1 or i == n or j == n:
            print("*",end="")
        else:
            print(" ", end="")
    print()
# output
# *****
# *   *
# *   *
# *   *
# *****
