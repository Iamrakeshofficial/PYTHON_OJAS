'''1.write a python program to find the Nth term in a fibonacci series using recursion.'''

##def fib(n):
##    
##    if n<=0:
##        return 0
##    elif n<=1:
##        return 1
##
##    else:
##        return (fib(n-1)+fib(n-2))
##
##n=int(input("Enter the Nth term:"))
##result=fib(n)
####for i in range(n+1):
####    print(fib(i))
##print("The  {}th Term of Fibonacci Series is :{}".format(n,result))


'''2.write a python program to implement matrix multiplication.'''

##A=[[12, 18, 19],
##  [8 , 45 ,11],
##  [14 , 9, 10]]
##
##B=[[5, 8, 1],
##    [6, 7, 3],
##    [4, 5, 9]]
##
##
##result=[[0,0,0],
##        [0,0,0],
##        [0,0,0]]
##
##for i in range(len(A)):
##    for j in range(len(B[0])):
##        for k in range(len(B)):
##            result[i][j] += A[i][k] * B[k][j]
##            
##print("The matrix Multiplication of A and B is:{}".format(result))
##for r in result:
##    print(r)
##        


'''3.write a python program to draw a circle of square using turtle.'''

##import turtle
##turtle.goto(0, 100)
##turtle.right(90)
##turtle.goto(100, 100)
##turtle.right(90)
##turtle.goto(100, 0)
##turtle.right(90)
##turtle.goto(0, 0)
##turtle.penup()
##turtle.goto(50, 50)
##turtle.pendown()
##turtle.circle(20)
##turtle.done()

from turtle import *
  
  

for i in range(60):
      
    
    for j in range(4):
          
        
        fd(100)
          
        
        rt(90)
          
    
    rt(6)

'''4.write a python program even and odd using list comprehension.'''


##obj = [f"{i} is Even" if i%2==0 else f"{i} is Odd" for i  in range(10)] 
##print("\n".join(obj))



'''5.write a python program  to print the number from a given number N till 0 using recursion.'''


##def countdown(n):
##    print(n)
##    if n == 0:
##        return 0
##    return countdown(n - 1)

##countdown(10)

##n=int(input("Enter a Number:"))
##res=countdown(n)
##print(res)
