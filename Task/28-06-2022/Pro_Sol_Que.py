'''Write a Python program to find the second lowest grade of any student(s)
from the given names and grades of each student using lists and lambda.
Input number of students, names and grades of each student.

Note: If there are multiple students with the same grade then print each name alphabetically.

sample out:
Input number of students:  5
Name:  S ROY
Grade:  1
Name:  B BOSE
Grade:  3
Name:  N KAR
Grade:  2
Name:  C DUTTA
Grade:  1
Name:  G GHOSH
Grade:  1

Names and Grades of all students:
[['S ROY', 1.0], ['B BOSE', 3.0], ['N KAR', 2.0], ['C DUTTA', 1.0], ['G GHOSH', 1.0]]

Second lowest grade:  2.0

Names:
N KAR'''

students=[]
grades=[]
lower_Grade=0

n=int(input("Enter how Many student you Want:"))
for i in range(n):
    Name=input("Enter the Student Name:")
    Grade=float(input("Enter the Student Grade:"))
    students.append([Name,Grade])
    grades.append(Grade)
print("\nNames and Grades of all students:")
print(students)
print(grades)


