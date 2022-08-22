'''1.write a program to count elements in a file?'''

##with open("rakesh.txt", mode="r") as  f:
##    
##    lines = len(f.readlines())
##print('Total Number of lines:', lines)
##print("succcessfully done.")


'''2.write a python program on atleast three magic methods?'''
##class Employee(object):
##    def __init__(self,name,salary):
##        self.name=name
##        self.salary=salary
##
##    def __str__(self):
##        return f"The Name is {self.name} and Salary is :{self.salary} and i am str method"
##
##    def __repr__(self):
##        return f"The Name is {self.name} and Salary is :{self.salary}"
##
##    def __add__(self,other):
##        return self.salary+other.salary
##
##
##e=Employee("Tarak",13000)
##e1=Employee("Vaddepa",15000)
##
##print(e)
##print(repr(e))
##
##print(e+e1)


'''3.Write python program on multithreading?'''

##from threading import*
##
##def square(number):
##    for i in number:
##        print("Square VAlues:",i*i)
##
##
##def rakesh(number):
##    for i in number:
##        print("Double values:",2*i)
##
##number=[1,2,3,4,5]
##t1=Thread(target=square,args=(number,))
##t2=Thread(target=rakesh,args=(number,))
##
##t1.start()
##t2.start()
##t1.join()


'''4.Write a dictionary to a file in Python.'''

##exDict = {1:1, 2:2, 3:3}
##with open('file.txt', 'w+') as file:
##    file.write(str(exDict))
##
##

'''5.write the program to Get Yesterday’s date using Python?'''

##from datetime import*
##
##today = date.today()
##print("Today is: ", today)
## 
##yesterday = today - timedelta(days = 1)
##print("Yesterday was: ", yesterday)
