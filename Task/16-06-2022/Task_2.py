'''1) wap to print range of twin prime numbers by not using function.'''
##a=int(input("Enter the Range:"))
##for i in range(a):
##    if i>1:
##        for j in range(2,i):
##            if i%j==0:
##                break
##        else:
##            x=i+2
##            for k in range(2,x):
##                if x%k==0:
##                    break
##            else:
##                print(i,x)

'''2) wap to print perimutations of the string "abc" by not using function.'''

##a="abc"
##for i in a:
##    for j in a:
##        for k in a:
##            if i!=j and i!=k and j!=k :
##                print(i,j,k)
##        

'''3) wap to print even and odd numbers separatly from a list by using filter function.'''
##
##l=[10,9,8,7,6,5,4,3,2]
##result=list(filter(lambda x:x%2==0,l))
##result2=list(filter(lambda x:x%2!=0,l))
##print(result)
##print(result2)



'''4) wap to print range of fibonacci series by using recursion function.'''

##def fibonacci(n):
##    if(n <= 1):
##        return n
##    else:
##        return(fibonacci(n-1) + fibonacci(n-2))
##n=int(input("Enter a Number:"))    
##print("Fibonacci sequence:")
##for i in range(n):
##    print(fibonacci(i))
  

'''5) wap to print the strings from a list which are having the length of the list.'''

##s=["Python","java","c",".Net"]

##for i in s:
##    if len(s)==len(i):
##        print(i)
##    
