##1. Define a function that accepts roll number and returns whether the student is present or absent.
##def roll_num(a):
##    x=[30,45,2,7,11,19]
##    if a in x:
##        print(f"Roll number {a} is present")
##    else:
##        print(f"Roll number {a} is absent")
##a=int(input())
##roll_num(a)

##12. Write a Python Set comprehension with an if clause example


##10. First, create a range from 100 to 160 with steps of 10.
##Second, using dict comprehension, create a dictionary where each number in the range is the key and each item divided by 100 is the value.
##a=range(100,160,10)
##print(list(a))

##Output:[100, 110, 120, 130, 140, 150]

##2.  	a. Write a python program to print multiple arguments.

##def pos(*a):
##    print(a)
##a=("mounika","priya","usha")
##pos(a)
##
##Output:
##(('mounika', 'priya', 'usha'),)







##	b. Write a function that accepts variable length key value pair as arguments.

##def key(**a):
##    return a
##print(key(key_1="Mounika",key_2="Usha",key_3="priya"))

##Output:
##{'key_1': 'Mounika', 'key_2': 'Usha', 'key_3': 'priya'}


##3. 	 a. Write a python program to find the power of a number using recursion

##def power(a,b):
##    if b==0:
##        return 1
##    else:
##        msg=a*power(a,b-1)
##    return msg
##a=2
##b=3
##print(power(a,b))

##Output:8


##3. 	 a. Write a python program to find the power of a number using recursion

##def power(a,b):
##    if b==0:
##        return 1
##    else:
##        msg=a*power(a,b-1)
##    return msg
##a=2
##b=3
##print(power(a,b))

##Output:8





##b. Write a Python program of recursion list sum 
##Test Data: [1, 2, [3,4], [5,6]]
##Expected Result: 21

##def sum_list(a):
##    b=0
##    for i in a:
##        if type(i)==type([]):
##            b=b+sum_list(i)
##        else:
##            b=b+i
##    return b
##print(sum_list([1, 2, [3,4], [5,6]]))

##Output:21

##4. Create an inner function to calculate the addition in the following way
##Create an outer function that will accept two parameters, a and b
##Create an inner function inside an outer function that will calculate the addition of a and b
##At last, an outer function will add 5 into addition and return it
##def outer(a,b):
##    sum=0
##    def inner():
##        sum=a+b
##        return sum
##    return inner()+5
##a=10
##b=20
##print(outer(a,b))

##Output:35

#5.a.  Assign a different name to function and call it through the new name

##def name(a):
##    print(a)
##name("Mounika")
##new_name=name
##new_name("Laxmi")


##Output:
##Mounika
##Laxmi


##b. 15.Create a function showEmployee() in such a way that it should accept employee name, and it’s salary and display both, and if the salary is missing in function call it should show it as 9000
##def sal(emp,salary=9000):
##    print("employee",emp)
##    print("Salary", salary)
##sal("Mounika",3000)
##sal("Laxmi")

##Output:
##employee Mounika
##Salary 3000
##employee Laxmi
##Salary 9000
##6.a. Write a Python function that takes a number as a parameter and check the number is prime or not. 


##def prime(a):
##    for i in range(1,a+1):
##        f=0
##        for j in range(2,i):
##            if (i%j)==0:
##                f=f+1
##    if f==0:
##        print("Prime")
##    else:
##        print("Not a Prime")
##a=int(input())
##prime(a)

##Output:
##4
##Not a Prime
##3
##Prime

##==================================================================================================================================================

##b. Write a Python function that checks whether a passed number is palindrome or not
##def palindrome(a):
##    if a[::-1]==a:
##        print("Palindrome")
##    else:
##        print("Not a Palindrome")
##a=input()
##palindrome(a)

##Output
##123
##Not a Palindrome
##121
##Palindrome

##7. 	a. Write a Python program to sort a list of tuples using Lambda.
##Original list of tuples:
##[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
##Sorting the List of Tuples:
##[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]

##marks=[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
##print(marks)
##marks.sort(key=lambda x:x[1])
##print(marks)

##Output:
##[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
##[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]


##b.Write a Python program to create Fibonacci series upto n using Lambda

##from functools import reduce
##fib=lambda b:reduce(lambda a,x:a+[a[-1]+a[-2]],range(b-2),[0,1])
##print(fib(10))

##Output:
##[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

##c.Write a Python program to add two given lists using map and lambda.

##l1=[1,2,3,4]
##l2=[4,5,6,7]
##result=map(lambda a,b:a+b,l1,l2)
##print(list(result))

##Output:
##[5, 7, 9, 11]

##d. Write a Python program to find palindromes in a given list of strings using Lambda.  
##Orginal list of strings:
##['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
##List of palindromes:
##['php', 'aaa'] 
##l1=['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
##print(l1)
##x=list(filter(lambda x: (x=="".join(reversed(x))),l1))
##print(x)

##Output:
##['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
##['php', 'aaa']


##e. Using .sort() method, create a lambda function that sorts the list in descending order. Refrain from using the reverse parameter.
##(Hint: lambda will be passed to sort method's key parameter as argument)





##
##f. Write a lambda function which takes z as a parameter and returns z*11

##f=lambda z:z*11
##print(f(5))

##Output:
##55

##8a. Using List Comprehension Find all of the numbers from 1–1000 that are divisible by

##x=[i for i in range(1,1000) if i%8==0]
##print(x)

##Output:
##[8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160, 168, 176, 184, 192, 200, 208, 216, 224, 232, 240, 248, 256, 264, 272, 280, 288, 296, 304, 312, 320, 328,
## 336, 344, 352, 360, 368, 376, 384, 392, 400, 408, 416, 424, 432, 440, 448, 456, 464, 472, 480, 488, 496, 504, 512, 520, 528, 536, 544, 552, 560, 568, 576, 584, 592, 600, 608, 616, 624, 632, 640,
## 648, 656, 664, 672, 680, 688, 696, 704, 712, 720, 728, 736, 744, 752, 760, 768, 776, 784, 792, 800, 808, 816, 824, 832, 840, 848, 856, 864, 872, 880, 888, 896, 904, 912, 920, 928, 936, 944, 952,
## 960, 968, 976, 984, 992]



##b. Use list comprehension to contruct a new list but add 6 to each item.
##l1=[0,1,2,3,4,5,6,7,8,9,10]
##l2=[i+6 for i in l1]
##print(l2)

##Output:
##[6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

##9. string = "Practice Problems to Drill List Comprehension in Your Head."
##Remove all of the vowels in a string (use string above)
##Find all of the words in a string that are less than 5 letters (use string above)
##Use a dictionary comprehension to count the length of each word in a sentence (use string above)

##a="Practice Problems to Drill List Comprehension in Your Head."
##for i in a:
##    if i not in ("a","e","i","o","u"):
##        print(i,end="")


##Output:Prctc Prblms t Drll Lst Cmprhnsn n Yr Hd.


##a="Practice Problems to Drill List Comprehension in Your Head."
##x=a.split()
##for j in x:
##    if len(j)<5:
##        print(j,end=" ")


##Output: to List in Your 

##a="Practice Problems to Drill List Comprehension in Your Head."
##s=a.split()
##d={x:len(x) for x in s}
##print(d)

##Output:
##{'Practice': 8, 'Problems': 8, 'to': 2, 'Drill': 5, 'List': 4, 'Comprehension': 13, 'in': 2, 'Your': 4, 'Head.': 5}


