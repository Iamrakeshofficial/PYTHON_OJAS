"""1. Define a function that accepts roll number and returns whether the student is present or absent."""
##def fun(a):
##    rollnum=[100,101,102,103,104,105]
##    
##    if a in rollnum:
##        print("Present")
##
##    else:
##        print("Absent")
##
##a=int(input("Enter a Number to check:"))
##fun(a)

"""2.  	a. Write a python program to print multiple arguments."""
##
##def Rakesh (*n):
##    for i in n:
##        print(i)
##
##result=Rakesh(["a","b","c"])
##print(result)
##
##op=['a', 'b', 'c']
##
##        


"""b. Write a function that accepts variable length key value pair as arguments."""
##
##def tarkesh(**name):
##    for key,value in name.items():
##        print("{} is {}".format(key,value))
##
##tarkesh(name="Rakesh",age=23)
##    


"""3. 	 a. Write a python program to find the power of a number using recursion."""

##def fun(num,power,c):
##    if power>1:
##        num=num*c
##        power-=1
##        fun(num,power,c)
##
##    if power==1:
##        print(num)
##
##num=10
##power=3
##c=num
##fun(num,power,c)



"""b. Write a Python program of recursion list sum 
Test Data: [1, 2, [3,4], [5,6]]
Expected Result: 21"""

##def  fun(lst):
##    add=0
##    for i in range (len(lst)):
##        if type(lst[i])==list:
##            add+=fun(lst[i])
##        else:
##            add=add+lst[i]
##    return add
##
##lst=[1, 2, [3,4], [5,6]]
##
##print(fun(lst))

"""4. Create an inner function to calculate the addition in the following way
Create an outer function that will accept two parameters, a and b
Create an inner function inside an outer function that will calculate the addition of a and b
At last, an outer function will add 5 into addition and return it"""

##def outer_fun(a,b):
##    def inner_fun():
##        c=a+b
##        return c
##    return inner_fun()+5
##
##a=int(input("Enter a Number:"))
##b=int(input("Enter b Number:"))
##print( "The  Results Is",outer_fun(a,b))
##
##op=
##Enter a Number:12
##Enter b Number:13
##The  Results Is 30



"""5. 	a.  Assign a different name to function and call it through the new name."""

##def wish():
##    print("Hello Guys")
##
##greetings=wish
##    
##greetings()
##op=
##Hello Guys


"""b. 15.Create a function showEmployee() in such a way that it should accept employee name,
and it’s salary and display both, and if the salary is missing in function call it should show it as 9000"""

##def showEmployee(name,salary=9000):
##    print("Employee Details:\n Emp Name is:{}\nEmp Slary is :{}".format(name,salary))
##
##
##showEmployee("Rakesh",15000)
##showEmployee("Rakesh")
##
##op=
##Employee Details:
## Emp Name is:Rakesh
##Emp Slary is :15000

##Employee Details:
## Emp Name is:Rakesh
##Emp Slary is :9000





"""6.a. Write a Python function that takes a number as a parameter and check the number is prime or not."""

##def isprime(num):
##    for i in range(2,num):
##        if num%i==0:
##            print("The number is not prime.")
##            break
##
##    else:
##        print("It is a Prime Number")
##
##num=int(input("Enter a Number to check:"))
##isprime(num)


"""b. Write a Python function that checks whether a passed number is palindrome or not. """

##def ispalindrome(num):
##    temp=num
##    rev=0
##    while num>0:
##        dig=num%10
##        rev=rev*10+dig
##        num=num//10
##    if temp==rev:
##        print("The number is a palindrome!")
##    else:
##        print(" It is Not a palindrome!")
##        
##
##num=int(input("Enter a Number."))
##ispalindrome(num)
##
##op=
##Enter a Number.121
##The number is a palindrome!

"""7. 	a. Write a Python program to sort a list of tuples using Lambda.
Original list of tuples:
[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
Sorting the List of Tuples:
[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]"""

##m=[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
##m.sort(key=lambda x:x[1])
##print(m)
##
##op=
##[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]



"""b. 	Write a Python program to create Fibonacci series upto n using Lambda."""
##lst=[0,1]
##print(0,1,end=" ")
##
##for i in range(5):
##    b=lambda x:x[-2]+x[-1]
##    print(b(lst),end=" ")
##    lst.append(b(lst))
##
##op=
##0 1 1 2 3 5 8 


"""c.  Write a Python program to add two given lists using map and lambda."""

##l1=[1,2,3,4,5]
##l2=[8,9,10,11,12]
##l3=list(map(lambda x,y:x+y,l1,l2))
##print(l3)
##
##op=
##[9, 11, 13, 15, 17]



"""d. Write a Python program to find palindromes in a given list of strings using Lambda.  
Orginal list of strings:
['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
List of palindromes:
['php', 'aaa']"""


##s=['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
##l=list(filter(lambda x:x==x[::-1],s))
##print(l)
##
##op=['php', 'aaa']




"""e. Using .sort() method, create a lambda function that sorts the list in descending order. Refrain from using the reverse parameter.
(Hint: lambda will be passed to sort method's key parameter as argument)"""

##c=[10,20,30,40,50,60]
##c.sort(key=lambda x:-x)
##print(c)

##op=[60, 50, 40, 30, 20, 10]
##



"""f. Write a lambda function which takes z as a parameter and returns z*11"""
##x=lambda z:z*11
##print(x(10))
##
##op=
##110

"""8. 	a. Using List Comprehension Find all of the numbers from 1–1000 that are divisible by 8"""


##l=[i for i in range(1,1000) if i%8==0]
##print(l)
##
##op=
##[8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160, 168, 176, 184, 192, 200,
## 208, 216, 224, 232, 240, 248, 256, 264, 272, 280, 288, 296, 304, 312, 320, 328, 336, 344, 352, 360, 368, 376,
## 384, 392, 400, 408, 416, 424, 432, 440, 448, 456, 464, 472, 480, 488, 496, 504, 512, 520, 528, 536, 544, 552,
## 560, 568, 576, 584, 592, 600, 608, 616, 624, 632, 640, 648, 656, 664, 672, 680, 688, 696, 704, 712, 720, 728,
## 736, 744, 752, 760, 768, 776, 784, 792, 800, 808, 816, 824, 832, 840, 848, 856, 864, 872, 880, 888, 896, 904,
## 912, 920, 928, 936, 944, 952, 960, 968, 976, 984, 992]



"""b. Use list comprehension to contruct a new list but add 6 to each item."""


##l=[10,11,12,13,14,15]
##l1=[i+6  for i in l]
##print(l1)
##
##op=
##[16, 17, 18, 19, 20, 21]



"""9. string = "Practice Problems to Drill List Comprehension in Your Head."
Remove all of the vowels in a string (use string above)
Find all of the words in a string that are less than 5 letters (use string above)
Use a dictionary comprehension to count the length of each word in a sentence (use string above)"""


##string = "Practice Problems to Drill List Comprehension in Your Head."
##vowels=['a','e','i','o','u']
##s=" "
##for i in string:
##    if i not in vowels:
##        s+=i
##print(s)
##
##l=string.split()
##for i in l:
##    if len(i)<5:
##        print(i)
##
##d={x:len(x) for x in l}
##print(d)
##

##op= Prctc Prblms t Drll Lst Cmprhnsn n Yr Hd.


##to
##List
##in
##Your


##{'Practice': 8, 'Problems': 8, 'to': 2, 'Drill': 5, 'List': 4, 'Comprehension': 13, 'in': 2, 'Your': 4, 'Head.': 5}


"""10. First, create a range from 100 to 160 with steps of 10.
Second, using dict comprehension, create a dictionary where each number in the range
is the key and each item divided by 100 is the value."""

##lst=[i for i in range(100,160,10)]
##dic={i:i%100 for i in lst}
##print(dic)

##op=
##{100: 0, 110: 10, 120: 20, 130: 30, 140: 40, 150: 50}

   
"""11. Using dict comprehension and a conditional argument create a dictionary from the
current dictionary where only the key:value pairs with value above 2000 are taken to the new dictionary.

dict1={"NFLX":4950,"TREX":2400,"FIZZ":1800, "XPO":1700}"""

##d1={"NFLX":4950,"TREX":2400,"FIZZ":1800, "XPO":1700}
##
##d2={i:d1[i] for i in d1 if d1[i]>2000}
##print(d2)
##op=
##{'NFLX': 4950, 'TREX': 2400}



"""12. Write a Python Set comprehension with an if clause example."""

##set2={i for i in range(20) if i%2==0}
##print(set2)
##
##op=
##{0, 2, 4, 6, 8, 10, 12, 14, 16, 18}

