"""1.Write a python program in fibonacci series using generator."""

##def fib(num):
##   p, q = 0, 1
##
##   while p < num:
##       yield p
##       p, q = q, p + q
##
##n = int(input("Enter the number up to : "))
##
##x = fib(n)
##print("Fibonacci Series up to", n, "is :")
##for i in x:
##   print(i)

"""2.Write a python program to generate the running product of the elemnts of a given iterable."""

##from itertools import accumulate
##import operator
##
##def product(l):
##    return accumulate(l,operator.mul)
##result=product([1,2,3,4])
##for i in result:
##    print(i)

"""3.factorial using iterators."""

##n=6
##fact=1
##for i in range(1,n+1):
##    fact=fact*i
##print(fact)



"""4.Write a simple registeration form which contains input buttons heading and radio buttons."""

##from tkinter import*
##root = Tk()
##root.geometry('500x500')
##root.title("Registration Form")
##label_0 = Label(root, text="Registration form",width=20,font=("bold", 20))
##label_0.place(x=90,y=53)
##label_1 = Label(root, text="FullName",width=20,font=("bold", 10))
##label_1.place(x=80,y=130)
##entry_1 = Entry(root)
##entry_1.place(x=240,y=130)
##label_2 = Label(root, text="Email",width=20,font=("bold", 10))
##label_2.place(x=68,y=180)
##entry_2 = Entry(root)
##entry_2.place(x=240,y=180)
##label_3 = Label(root, text="Gender",width=20,font=("bold", 10))
##label_3.place(x=70,y=230)
##var = IntVar()
##Radiobutton(root, text="Male",padx = 5, variable=var, value=1).place(x=235,y=230)
##Radiobutton(root, text="Female",padx = 20, variable=var, value=2).place(x=290,y=230)
##label_4 = Label(root, text="Age:",width=20,font=("bold", 10))
##label_4.place(x=70,y=280)
##entry_2 = Entry(root)
##entry_2.place(x=240,y=280)
##Button(root, text='Submit',width=20,bg='brown',fg='white').place(x=180,y=380)
##print("registration form  seccussfully created...")
##
##root.mainloop()



"""5.prime progam using sys module."""

##from sys import *
##
##for i in range(2,int(argv[1])):
##    if int(argv[1])%i==0:
##        print("It is not a Prime Number.")
##        break
##else:
##    print("It is a  Prime Number.")
##


##import sys
##def prime(a):
##    for i in range(1,a+1):
##        f=0
##        for j in range(2,i):
##            if (i%j)==0:
##                f=f+1
##    if f==0:
##        print("Prime")
##    else:
##        print("Not a Prime")
##a=int(input())
##prime(a)
