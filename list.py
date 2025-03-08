# HackerRank: List Comprehension
"""Let's learn about list comprehensions! 
You are given three integers  and  representing the dimensions of a cuboid along with an integer n. 
Print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of i + j + k is not equal to n. 
Here, 0 <= i <= x; 0 <= j <= y; 0 <= k <= z. Please use list comprehensions rather than multiple loops, as a learning exercise."""
# if __name__ == '__main__':
#     x = int(input())
#     y = int(input())
#     z = int(input())
#     n = int(input())
    

# values = [] 
# for i in range(x + 1):
#     for j in range(y+1):
#         for k in range(z+1):
#             if i + j + k !=n:
#                 values.append([i,j,k])

# print(values)


# HackerRank: Nested Lists
"""Given the names and grades for each student in a class of N students, 
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, 
order their names alphabetically and print each name on a new line."""

# if __name__ == '__main__':
#     records = []
    
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         records.append([name, score])
        

# grades = sorted(set(score for _, score in records))
# second_grade = grades[1]

# second_grade_student = sorted([name for name, score in records if score == second_grade])

# for student in second_grade_student:
#     print(student)  
