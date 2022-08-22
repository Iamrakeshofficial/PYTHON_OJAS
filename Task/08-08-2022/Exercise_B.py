'''1) create a nested list by taking list elements from the user like below
[1,2,[3,4],[5,6,7],8,9]'''

##l=[]
##i=0
##
##while i<=5:
##    n=eval(input("Enter The Number Of Values:"))
##    l.append(n)
##    i+=1
##print(l)

'''2) write a program on to retrieve the data from the file and use seek() and tell() method.'''

##with open("rakesh.txt",mode="r+") as f:   
##    data=f.read()
##    print(data)
##    b=f.tell()
##    print(b)
##    a=f.seek(4)
##    print(a)
##    print(f.readline())
##    
'''3) write a program on rlock in multithreading.'''

##from threading import*
##l=RLock()
##def factorial(n):
##    l.acquire()
##    if n==0:
##        result=1
##    else:
##        result=n*factorial(n-1)
##    l.release()
##    return result
##
##def results(n):
##    print("The Factorial of",n,"is:",factorial(n))
##
##t1=Thread(target=results,args=(5,))
##t2=Thread(target=results,args=(9,))
##
##t1.start()
##t2.start()

'''4) wap to create three functions and three threads for each functions and run those threads.'''

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
##def cube(number):
##    for i in number:
##        print("Cube Values:",i*i*i)
##
##number=[1,2,3,4,5]
##t1=Thread(target=square,args=(number,))
##t2=Thread(target=rakesh,args=(number,))
##t3=Thread(target=cube,args=(number,))
##
##t1.start()
##t2.start()
##t3.start()
##t1.join()
##t2.join()
##t3.join()

'''5) wap to print the next 100th decimal of entered user input 
input = 129, output = 200 , if input = 334, output=400'''


##n=int(input("Enter a Number:"))
##m=100
##while True:
##    if n<m:
##        print(m)
##        break
##    else:
##        m+=100
