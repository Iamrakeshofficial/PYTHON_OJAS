"""1.Write a Python program to get all possible combinations of the elements of a given list using itertools module."""
##import itertools
##
##l=[12,23,1,2,3,4,5,6]
##result=list(itertools.combinations(l,5))
##print(result)


"""2.Write a python program to create an iterator that returns consecutive keys and groups from an iterable."""

##import itertools
##
##lst=[("apple","banana",5),("grapes","cherry",6),("apple","cherry","banana"),("kiwi","cherry",5)]
##
##def Rakesh(lst):
##    result=itertools.groupby(lst,key=lambda x:x[1])
##    for key,group in result:
##        print(key,list(group))
##
##Rakesh(lst)


"""3. Write a Python program to find the years where 25th of December be a Sunday between 2000 and 2150."""

##from datetime import date
##def Years():
##    for i in range(2000,2151):
##        def is_Sunday(i):
##            return 6==date(i,12,25).weekday()
##        if is_Sunday(i):
##            print(i)
##Years()


"""4.write a python program using generator write armstrong."""

##def Armstrong(num):
##    sum=0
##    temp=num
##    while temp>0:
##        digit=temp%10
##        sum+=digit**3
##        temp//=10
##        if num==sum:
##            yield num
##            break
##    else:
##        print("It is Not an Armstrong Number.")
##
##
##
##num=int(input("Enter a Number to Check."))
##
##res=Armstrong(num)
##for i in res:
##    if i==num:
##        print("{} is an Armstrong Number".format(i))

"""5.write a python program by using math module use 3 function for each function one example."""

"""Area of Circle"""
##import math
##
##r=float(input("Enter Radious of circle:"))
##pi=math.pi
##area=math.pi*r*r
##print("Area of the Circle is:{}".format(area))

"""Factorial of a Number"""

##import math as m
##n=int(input("Enter a Number:"))
##print("The Factorial of {} is {}.".format(n,m.factorial(n)))

"""Power of a Number"""

##import math as m
##x=int(input("Enter the Base:"))
##n=int(input("Enter the Power:"))

##res=m.pow(x,n)

##print("{} to the Power of {} is {}".format(x,n,res))












