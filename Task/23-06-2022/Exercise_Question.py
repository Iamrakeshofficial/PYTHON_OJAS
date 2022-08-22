'''1)Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.'''

##s = input("Enter a Sentence:")
##d={"UPPER CASE":0, "LOWER CASE":0}
##for c in s:
##    if c.isupper():
##        d["UPPER CASE"]+=1
##    elif c.islower():
##        d["LOWER CASE"]+=1
##    else:
##        pass
##print( "UPPER CASE:", d["UPPER CASE"])
##print("LOWER CASE:", d["LOWER CASE"])


'''2)Python Program to Remove the ith Occurrence of the Given Word in a List.'''

##a=[]
##n= int(input("Enter the number of elements in list:"))
##for x in range(0,n):
##    element=input("Enter element" + str(x+1) + ":")
##    a.append(element)
##print(a)
##c=[]
##count=0
##b=input("Enter word to remove: ")
##n=int(input("Enter the occurrence to remove: "))
##for i in a:
##    if(i==b):
##        count=count+1
##        if(count!=n):
##            c.append(i)
##    else:
##        c.append(i)
##if(count==0):
##    print("Item not found ")
##else: 
##    print("The number of repetitions is: ",count)
##    print("Updated list is: ",c)
   

'''3)Python Program to Merge Two Lists and Sort it.'''

##a=[]
##c=[]
##n1=int(input("Enter number of elements in 1st List:"))
##for i in range(1,n1+1):
##    b=int(input("Enter element:"))
##    a.append(b)
##n2=int(input("Enter number of elements in 2nd List:"))
##for i in range(1,n2+1):
##    d=int(input("Enter element:"))
##    c.append(d)
##new=a+c
##new.sort()
##print("Sorted list is:",new)


'''4)Python Program to Find the Gravitational Force between Two Objects.'''

##m1=float(input("Enter the first mass: "))
##m2=float(input("Enter the second mass: "))
##r=float(input("Enter the distance between the centres of the masses: "))
##G=6.673*(10**-11)
##f=(G*m1*m2)/(r**2)
##print("Hence, the gravitational force is: ",round(f,2),"N")

'''5) Write a Python Program for Even Number Pyramid Pattern.'''

##n=0
##for j in range(1,5):
##    for x in range(5,j,-1):
##        print(" ",end="")
##    for i in range(0,j):
##        print(str(n)+" ",end="")
##        n=n+2
##    print()
##





















