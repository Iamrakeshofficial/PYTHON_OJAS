'''1.write a python program on logging.'''

##from logging import*
##basicConfig(filename="akash8.txt",level=DEBUG,filemode="w")
##debug("This is Debug")
##info("Information")
##warning("This is Warning")
##error("This is a Error")
##critical("This is a Message from Critical")


'''2.write a python program to remove all the occurances of the given number.'''

##li= [2,2,3,5,2,2,1,0]
##try:
##    while True:
##        li.remove(2) 
##    print(myList)
##except:
##    pass
##print(li)

'''3.write a python program to exact the numbers in a given string and print sum,minimum and maximum of those numbers.'''

##a=input("Enter an AlphaNumeric String:")
##b=[]
##for i in a:
##    if i.isdigit():
##        b.append(int(i))
##print("sum:",sum(b))
##print("max:",max(b))
##print("min:",min(b))        
##


'''4.write a python program on sprial number 
eg:-9 8 7     
    2 1 6        
    3 4 5'''

##n=1
##order=[4,3,6,7,8,5,2,1,0]
##lst=[1,2,3,4,5,6,7,8,9]
##for i in order:
##    lst[i]=n
##    n+=1
##print()
##m=0
##for i in lst:
##    print(i,end=' ')
##    m+=1
##    if m%3==0:
##        print()


'''5.create a list of combinations of entered number like below
input: 5
list must be created as [4,4,4,33,33,22,22,1,1,1]'''

##from itertools import combinations
##i=int(input("enter combinations:"))
##a=[4,4,4,33,33,22,22,1,1,1]
##c=combinations(a,i)
##for i in c:
##    print(i)
