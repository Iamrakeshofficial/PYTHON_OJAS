"""WAP for to check the Number is Prime or Not using Sys .
##1.write a python program in prime number using outer and inner function and using decorator."""

##from sys import*
##
##if int(argv[1])>1:
##    for i in range(2,(int(argv[1]))//2):
##        if ((int(argv[1]))%i)==0:
##            print("Is not a Prime Number.")
##
##    else:
##        print("Is a Prime Number.")
##
##else:
##    print("Is  not a Prime Number.")


"""sYS"""
##from sys import*
##n=int(argv[1])
##if n>1:
##    for i in range(2,n//2):
##        if (n%i)==0:
##            print("It is not a Prime.")
##            break
##
##    else:
##        print("It is a Prime Number.")
##       
##
##else:
##     print("It is not a Prime Number.")

"""Closure Function"""

##def Outer(fun):
##    def inner():
##        n=int(input("Enter a Number."))
##        if n>1:
##            for i in range(2,n//2):
##                if(n%i)==0:
##                    print("It is Not a Prime Number.")
##                    break
##            else:
##                print("It is a Prime Number.")
##
##        else:
##            print("It is not a Prime Number.")
##
##    return inner
##
##
##def new():
##    pass
##
##
##op=Outer(new)
##op()

##def outer(fun):
##    def inner():
##        n=int(input("enter a number"))
##
##        count=0
##        for i in range(1,n+1):
##            if n%i==0:
##                count=count+1
##        if count==2:
##            print("it is prime ")
##        else:
##            print("it is not prime")
##   
##    return inner
##def new():
##    pass
##    
##reult=outer(new)
##reult()



"""2.write a python program in armstrong number using outer and inner function and using decorator."""

##def is_Armstrong(fun):
##    def inner():
##        num=int(input("Enter a Number."))
##        sum=0
##        temp=num
##        while(temp>0):
##            digit=temp%10
##            sum+=digit**3
##            temp//=10
##
##            if num==sum:
##                print("It is  an Armstrong Number.")
##                break
##                
##        else:
##            print("It is not an Armstrong Number.")
##
##    return inner
##@is_Armstrong
##def new():
##    pass
####result=is_Armstrong(new)
####result()
##new()

"""Sys"""
##from sys import*
##num=int(argv[1])
##sum=0
##temp=num
##while(temp>0):
##    digit=temp%10
##    sum+=digit**3
##    temp//=10
##    if num==sum:
##        print("It is  an Armstrong Number.")
##        break
##                
##else:
##    print("It is not an Armstrong Number.")

"""3.write a python program in strong number using outer and inner function and using decorator."""

##def is_Strong(fun):
##    def inner():
##        num=int(input("Enter a Number."))
##        sum=0
##        temp=num
##        while (num):
##            i=1
##            fact=1
##            rem=num%10
##            while(i<=rem):
##                fact=fact*i
##                i=i+1
##                
##            sum=sum+fact
##            num=num//10
##
##        if(sum==temp):
##            print("It is a strong Number.")
##        else:
##            print("It is not a Strong Number.")
##    return inner
##
##@is_Strong
##def new():
##    pass
##new()

"""Sys"""
##from sys import*
##num=int(argv[1])
##sum=0
##temp=num
##while (num):
##    i=1
##    fact=1
##    rem=num%10
##    while(i<=rem):
##        fact=fact*i
##        i=i+1
##    sum=sum+fact
##    num=num//10
##
##if(sum==temp):
##    print("It is a strong Number.")
##else:
##    print("It is not a Strong Number.")

"""4.write a python program in palindrome for integers using inner and outer function and using decorator."""

##def is_Palindrome(num):
##    def inner():
##        num=int(input("Enter a Number."))
##        sum=0
##        temp=num
##        while temp>0:
##            digit=temp%10
##            sum=sum*10+digit
##            temp=temp//10
##            
##            if num==sum:
##                print("It is a Palindrome Number.")
##                break
##            
##
##        else:
##            print("It is not a Palindrome Number.")
##    return inner
##
##@is_Palindrome
##def new():
##    pass
##new()

"""Sys"""
##from sys import *
##
##num=int(argv[1])
##sum=0
##temp=num
##while temp>0:
##    digit=temp%10
##    sum=sum*10+digit
##    temp=temp//10
##            
##    if num==sum:
##        print("It is a Palindrome Number.")
##        break
##            
##
##else:
##    print("It is not a Palindrome Number.")


"""5.write a python program in perfect number using outer and inner function and using decorator."""
##def is_Perfect(num):
##    def inner():
##        num=int(input("Enter a Number."))
##        i=1
##        sum=0
##        while(i<num):
##             if num%i==0:
##                 sum=sum+i
##             i=i+1
##        if num==sum:
##             print("It is a Perfect Number.")
##
##        else:
##            print("It is not a Perfect Number.")
##
##    return inner
##
##@is_Perfect
##def new():
##    pass
##new()


"""SYS"""
##from sys import*
##num=int(argv[1])
##i=1
##sum=0
##while(i<num):
##    if num%i==0:
##        sum=sum+i
##    i=i+1
##if num==sum:
##    print("It is a Perfect Number.")
##
##else:
##    print("It is not a Perfect Number.")

"""6.write a python program in factorial number using outer and inner function and using decorator."""

##def is_Factorial(fun):
##    def inner():
##        num=int(input("Enter a Number."))
##        fact=1
##        for i in range(1,num+1):
##            fact=fact*i
##        print(fact)
##        fun()
##
##    return inner
##
##@is_Factorial
##def factorial():
##    print("Hello ")
##
##factorial()

"""SYS"""
##from sys import*
##num=int(argv[1])
##fact=1
##for i in range(1,num+1):
##    fact=fact*i
##print(fact)

"""7.write a python program in odd or even number using outer and inner function and using decorator."""

##def is_Odd(func):
##    def inner():
##        num=int(input("Enter a Number:"))
##        if num%2!=0:
##            print("It is an Odd Number.")
##
##        else:
##            print("It is an Even Number.")
##        func()
##    return inner
##
##@is_Odd
##def odd():
##    print("I am Groot.")
##odd()

"""SYS"""

##from sys import*
##num=int(argv[1])
##if num%2!=0:
##    print("It is an Odd Number.")
##
##else:
##    print("It is an Even Number.")

"""8.write a python program in even or odd number using outer and inner function and using decorator."""

##def is_Even(func):
##    def inner():
##        num=int(input("Enter a Number."))
##        if num%2==0:
##            print("It is an Even Number.")
##        else:
##            print("It is an Odd Number.")
##
##        func()
##    return inner
##
##@is_Even
##
##def even():
##    print("It is an Unique Code.")
##
##even()

"""SYS"""
##from sys import*
##num=int(argv[1])
##if num%2==0:
##    print("It is an Even Number.")
##else:
##    print("It is an Odd Number.")

"""9.write a python program convert octal to decimal  using outer and inner function and using decorator."""

##def Oct_Dec(fun):
##    def inner():
##        num=int(input("Enter a Number."))
##        decimal=0
##        base=1
##
##        while(num):
##            digit=num%10
##            num=int(num/10)
##            decimal+=digit*base
##            base=base*8
##
##        print("The Decimal Value is:",decimal)
##
##        fun()
##    return inner
##
##@Oct_Dec
##def oct():
##    print("Hello")
##oct()




"""10.write a python program in lcm number using outer and inner function and using decorator."""

##def Lcm(func):
##    def inner():
##        x=int(input("Enter a Number."))
##        y=int(input("Enter a Number."))
##
##        if x>y:
##            greater=x
##        else:
##            greater=y
##
##        while(True):
##            if((greater%x==0)and(greater%y==0)):
##                lcm=greater
##                break
##            greater+=1
##        print("The Lcm of {} and {} is {}.".format(x,y,lcm))
##
##        func()
##
##    return inner
##
##
##@Lcm
##def lcm():
##    print("Helo Good Morning.")
##
##lcm()

"""SYS"""

##from sys import*
##x=int(argv[1])
##y=int(argv[2])
##
##if x>y:
##    greater=x
##else:
##    greater=y
##
##while(True):
##    if((greater%x==0)and(greater%y==0)):
##        lcm=greater
##        break
##    greater+=1
##print("The Lcm of {} and {} is {}.".format(x,y,lcm))










                    
