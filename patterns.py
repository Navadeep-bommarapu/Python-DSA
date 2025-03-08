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


