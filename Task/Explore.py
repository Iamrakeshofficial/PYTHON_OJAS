'''1)Find the mean of a list of integers.'''
##def Mean(l): 
##    mean= sum(l) / len(l) 
##    return mean
##  
##my_list = [2,4,6,8,10] 
##mean= Mean(my_list) 
##  
##print("Mean of my_list is", mean)

'''2.Take a list and perform list operation.'''

##l=[10,9,8,7,6,5,4,3,2,1]


##l.append(12)
##print(l)

##l.clear()
##print(l)

##l1=l.copy()
##print(l1)

##print(l.count(10))

##l2=["Java","python","DS","AI"]
##l.extend(l2)
##print(l)

##print(l.index(10))

##l.insert(2,"python")
##print(l)

##l.pop()
##print(l)

##l.remove(10)
##print(l)

##l.reverse()
##print(l)

'''3.Collatz Sequence.'''

##n=int(input("Enter a Number:"))
##while n>1:
##    if n%2==0:
##        n=n//2
##        print(n,end=" ")
##    else:
##        n=3*n+1
##        print(n,end=" ")

'''4.Find the midpoint of a line.'''
##
##x1 = float(input('The value of x1 :'))
##y1 = float(input('The value of y1 :'))
##
##x2 = float(input('The value of x2 :'))
##y2 = float(input('The value of y2 :'))
##
##midpoint_of_x = (x1 + x2)/2
##midpoint_of_y = (y1 + y2)/2
##
##print( "The midpoint's x value is: ",midpoint_of_x)
##print( "The midpoint's y value is: ",midpoint_of_y)
##
##print("The midpoint of line is :({},{} )".format(midpoint_of_x,midpoint_of_y))

'''5.Get the values in one list and keys in another from a dictionary.'''

##d1={10:"Rossum",20:"Ritche",30:"Gosling",40:"Travis"}
##ks=d1.keys()
##print(ks)
##vs=d1.values()
##print(vs)
