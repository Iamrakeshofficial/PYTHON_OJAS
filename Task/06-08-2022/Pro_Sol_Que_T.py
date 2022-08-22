'''write a python program on sprial number using inner function
and decorator
eg:-1 2 3
    8 9 4
    7 6 5'''

##def Spiral_Num(n):
##    def inner():
##        l=[[0 for x in range(a)] for y in range(a)]
##        n=1
##        low=0
##        high=a-1
##        count=int(a+1)//2
##        for i in range(count):
##            for j in range(low,high+1):
##                l[i][j]=n
##                n+=1
##            for j in range(low+1,high+1):
##                l[j][high]=n
##                n+=1
##            for j in range(high-1,low-1,-1):
##                l[high][j]=n
##                n+=1
##            for j in range(high-1,low,-1):
##                l[j][low]=n
##                n+=1
##            low+=1
##            high-=1
##        for i in range(a):
##            for j in range(a):
##                print(l[i][j],end=" ")
##            print()
##
##    return inner()
##
##
##a=int(input("Enter the Number:"))
##Spiral_Num(a)
