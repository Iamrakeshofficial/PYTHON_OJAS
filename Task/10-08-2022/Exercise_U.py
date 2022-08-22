'''1.Python Program to Reverse a Stack using Recursion.'''

##def reverse(s):
##    a=[]
##    for i in range(len(stack)):
##        popped=stack.pop()
##        a.append(popped)
##    print(a)
##stack=[1,2,3,4,5]
##reverse(stack)
##    


'''2.Python Program to Append the Content of One File to the End of Another File.'''
    
##f1 = input("Enter the first file name = ")
##
##f2= input("Enter the second file name to append data = ")
##
##fi1 = open(f1, "r")
##
##data1 = fi1.read()
##print(data1)
##
##fi1.close()
##
##fi2 = open(f2, "a")
##
##fi2.write(data1)
##print("Appended Successfully.")
##fi2.close()


'''3.Python Program to Create a Class and Get All Possible Distinct Subsets from a Set.'''

##class Subset:
##    def f1(self, s1):
##        return self.f2([], sorted(s1))
##
##    def f2(self, curr, s1):
##        if s1:
##            return self.f2(curr, s1[1:]) + self.f2(curr + [s1[0]], s1[1:])
##        return [curr]
##
##
##a = []
##n = int(input("Enter number of elements of list: "))
##for i in range(0, n):
##    b = int(input("Enter element: "))
##    a.append(b)
##print("Subsets: ")
##print(Subset().f1(a))

'''4.How can you randomize the items of a list in place in Python?'''

##import random
##
##l = list(range(5))
##print(l)
##
##random.shuffle(l)
##print(l)



'''5.write a python program on showing 
KeyboardInterrupt,
ArithmeticError,
StopIteration
AssertionError
ImportError
'''


'''KeyboardInterrupt'''

##n=int(input("Enter how many number u want to enter:"))
##
##while (True):
##    if n>0:
##        print(n)
##try:
##     raise KeyboardInterrupt
##except KeyboardInterrupt:
##     print("Keyboard interrupt exception caught")

#If the user want to stop the loop use ctrl+c to break then user will get KeyboardInterrupt Error.

'''ArithmeticError'''

##try:
##    value = 12 / 0
##except ZeroDivisionError as e:
##    print(e)

'''StopIteration'''

##mylist = iter(["apple", "banana", "cherry"])
##x = next(mylist)
##print(x)
##x = next(mylist)
##print(x)
##x = next(mylist)
##print(x)
##x=next(mylist)
##print(x)

'''ImportError'''
##Raised when a module, or member of a module, cannot be imported.
##There are a few conditions where an ImportError might be raised

##try:
##    from time import datetime
##except Exception as e:
##    print(e)

'''AssertionError'''
##Raised in case of failure of the Assert statement.

##try:
##    x = 1
##    y = 0
##    assert y != 0
##    print(x / y)
##except AssertionError :
##    print("Assertion error occured")
##

