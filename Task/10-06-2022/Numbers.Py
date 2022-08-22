'''1.Write a program to find sum of number. '''
##a=int(input("Enter a Number:"))
##add=0
##while a>0:
##    rem=a%10
##    add=add+rem
##    a=a//10
##print(add)

'''2.WAP to find the number is strong number or not  '''

##sum=0  
##
##num=int(input("Enter a number:"))  
## 
##temp=num  
##  
##while(num):  
##     
##    i=1  
##    
##    fact=1  
##    rem=num%10  
##    while(i<=rem):  
##        fact=fact*i   
##        i=i+1  
##    sum=sum+fact  
##    num=num//10  
##if(sum==temp):  
##    print("Given number is a strong number")  
##else:  
##    print("Given number is not a strong number") 
##                       
                       
                       

'''3.Python Program to Find the Square Root '''
##a=int(input("Enter a Number:"))
##b=a**0.5
##print(b)
'''4.Python Program to Calculate the Area of a Triangle ...'''

##b=float(input("Enter the base for triangle:"))
##h=float(input("Enter height for triangle:"))
##area=0.5*b*h
##print("Area of Triangle is :{}".format(area))

'''5.Python Program to Solve Quadratic Equation.'''

'''6.Python Program to Swap Two Variables '''
##a=eval(input("Enter the value of a:"))
##b=eval(input("Enter the value of b:"))
##a,b=b,a
##print(a,b)

'''7.Python Program to Convert Kilometres to Miles '''
##a=int(input("enter the number"))
##b=a*1000
##print(b)


'''8.Python Program to Check Leap Year '''
##a=int(input("enter the number"))
##if a%4==0:
##    if a%100==0:
##        if a%400==0:
##            print("true")
##        else:
##            print("false")
##    else:
##        print("true")

'''9.Python Program to Check Prime Number '''

##n=int(input("Enter the Number:"))
##if n>1:
##    for i in range(2,int(n/2)+1):
##        if n%i==0:
##            print(n,"is not a Prime Number.")
##            break
##        else:
##            print(n,"is a Prime Number.")
##            break
##else:
##    print(n, "is not a Prime Number.")

'''10.Python Program to Find the Factorial of a Number.'''

##n=int(input("Enter a Number:"))
##factorial=1
##if n<0:
##    print("The Factorial Number Of Negative Number does not exist!")
##elif n==0:
##    print("The Factorial of 0 is 1.")
##else:
##    for i in range(1,n+1):
##        factorial=factorial*i
##    print("The Factorial of given number {} is {}".format(n,factorial))
 

'''11.Python Program to Print the Fibonacci sequence '''
##
##a=int(input("enter the number"))
##b=0
##c=1
##print(b)
##print(c)
##for i in range(a+1):
##    a=b+c
##    b=c
##    c=a
##    print(a)


'''12.Python Program to Check Armstrong Number'''
##a=(input("enter the number"))
##len_a=len(a)
##add=0
##temp=int(a)
##while temp>0:
##    rem=temp%10
##    add=add+rem**len_a
##    temp=temp//10
##if add==int(a):
##    print("yes armstrong")
##else:
##    print("not armstrong")

'''13.Python Program to Find Armstrong Number in an Interval '''
##lower = 100
##upper = 2000
##for num in range(lower, upper + 1):
##    order = len(str(num))
##    sum = 0
##    temp = num
##    while temp > 0:
##        digit = temp % 10
##        sum += digit ** order
##        temp //= 10
##        if num == sum:
##            print(num)
         
        
'''14.Python Program to Find the Sum of Natural Numbers '''

##n=int(input("Enter a Number to find sum of Natural Numbers: " ))
##add=0
##for i in range(n+1):
##    add=add+i
##print("The sum of Natural number is {}.".format(add))            

'''15.Python Program to Find the Factors of a Number .'''

##n=int(input("Enter a Number:"))
##factors=[]
##for i in range(1,n+1):
##    if n%i==0:
##        factors.append(i)
##print("The Factors of the {} are :{}".format(n,factors))

'''16.Python Program to Convert Decimal to Binary, Octal and Hexadecimal .'''

##dec = int(input("Enter an integer: "))
##print("The decimal value of",dec,"is:")
##print(bin(dec),"in binary.")
##print(oct(dec),"in octal.")
##print(hex(dec),"in hexadecimal.")

'''17.Python Program to Find LCM. '''
##a=int(input("Enter the First Number:"))
##b=int(input("Enter the Second Number:"))
##if a>b:
##    big=a
##else:
##    big=b
##while(True):
##    if(big%a==0 and big%b==0):
##        print("The LCM of {} and {}={}".format(a,b,big))
##        break;
##    big=big+1
##        





