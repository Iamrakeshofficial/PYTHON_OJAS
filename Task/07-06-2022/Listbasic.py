''' 1.Take 10 integer inputs from user and store them in a list and print them on screen. '''

##a=10
##b=[]
##for i in range(a):
##   c=int(input("enter a number"))
##   b.append(c)
##print(b)




''' 2.Take 10 integer inputs from user and store them in a list. Again ask user to give a number. Now, tell user whether that number is present in list or not.
( Iterate over list using while loop ). '''

##l=[]
##i=0
##while i<10:
##    a=int(input("enter an integer: "))
##    l.append(a)
##    i=i+1
##print(l)
##check=int(input("enter an int to check: "))
##if check in l:
##    print("yes")
##else:
##    print("no")

##    
''' 3.
Take 20 integer inputs from user and print the following:
number of positive numbers
number of negative numbers
number of odd numbers
number of even numbers
number of 0s. '''

##l=[]
##i=0
##e=0
##o=0
##p=0
##n=0
##z=0
##while i<5:
##    a=int(input("enter an integer: "))
##    l.append(a)
##    i=i+1
##print(l)
##for x in l:
##    if x>0:
##        p+=1
##    elif x<0:
##        n+=1
##    elif x%2==0:
##        e+=1
##    elif x%2!=0:
##            o+=1
##    elif x==0:
##        z+=1
##print("positive=",p)
##print("negative=",n)
##print("odd=",o)
##print("even=",e)
##print("zeros",z)



'''
4.Take 10 integer inputs from user and store them in a list. Now, copy all the elements in another list but in reverse order. '''



##l=[]
##i=0
##l1=[]
##while i<10:
##    a=int(input("enter an integer: "))
##    l.append(a)
##    i=i+1
##l1=l[::-1]
##print(l1)

'''
5.Write a program to find the sum of all elements of a list. '''

##l=[1,2,3,4,5,6]
##sum=0
##for i in l:
##    sum=sum+i
##print(sum)



'''
6.Write a program to find the product of all elements of a list. '''

##l=[1,2,3,4,5,6]
##mul=1
##for i in l:
##    mul=mul*i
##print(mul)




''' 7.Initialize and print each element in new line of a list inside list. '''

##a = [[1, 3, 4], [2, 5, 7],[10,15,20]]
##for i in a:
##    for j in i:
##        print(j, end = ' ')
##    print()



''' 8.Find largest and smallest elements of a list. '''
##l=[10,20,30,50,]
##print("smallest elemnt is: ",min(l))
##print("lorgest elemnt is: ",max(l))




''' 9.Write a program to print sum, average of all numbers, smallest and largest element of a list. '''
##l=[10,20,30,40]
##l1=len(l)
##
##print("smallest elemnt is: ",min(l))
##print("lorgest elemnt is: ",max(l))
##print("sum of all elements : ",sum(l))
##print("average of all elements : ",sum(l)/l1)





''' 10.Write a program to check if elements of a list are same or not it read from front or back. E.g.-
2	3	15	15	3	2  '''

##l=eval(input("enter a list : "))
##r=l[::-1]
##if r==l:
##    print("yes elements of a list are same ",r)
##else:
##    print("yes elements of a list are not same ",r)
##    



''' 11.Take a list of 10 elements. Split it into middle and store the elements in two dfferent lists. E.g.-
INITIAL list :
58	24	13	15	63	9	8	81	1	78  
After spliting :
58	24	13	15	63
9	8	81	1	78 '''


##l=[1,20,55,41,45,100]
##l2=l[:len(l)//2]
##l3=l[len(l)//2:]
##print(l)
##print(l2)
##print(l3)


    






''' 12.
Ask user to give integer inputs to make a list. Store only even values given and print the list. '''

##l=[]
##i=0
##ev=[]
##while i<4:
##    a=int(input("enter an integer: "))
##    l.append(a)
##    i=i+1
##for i in l:
##    if i%2== 0:
##        ev.append(i)
##print(ev)
##        
