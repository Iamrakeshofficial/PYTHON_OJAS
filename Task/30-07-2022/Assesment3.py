'''1.Write a Python class to get all possible unique subsets from a set of distinct integers.
Input : [4, 5, 6]
Output : [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]
'''
##class Myclass:
##    def f1(self, s1):
##        return self.f2([], sorted(s1))
##
##    def f2(self, curr, s1):
##        if s1:
##            return self.f2(curr, s1[1:]) + self.f2(curr + [s1[0]], s1[1:])
##        return [curr]
##
##
##a = [4,5,6]
##print("Subsets: ")
##print(Myclass().f1(a))

##op=Subsets: 
##[[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]
##

'''2.Write a Python class to find the three elements that sum to zero from a set of n real numbers.
Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
Output : [[-10, 2, 8], [-7, -3, 10]]
'''
##class Myclass:
##
##    def sum(self,nums):
##        
##        nums=sorted(nums)
##        result=[]
##        i=0
##
##
##        while i < len(nums) - 2:
##            j, k = i + 1, len(nums) - 1
##            while j < k:
##                if nums[i] + nums[j] + nums[k] < 0:
##                    j += 1
##                elif nums[i] + nums[j] + nums[k] > 0:
##                    k -= 1
##                else:
##                    result.append([nums[i], nums[j], nums[k]])
##                    j= j + 1
##                    k=k - 1
##                    while j < k and nums[j] == nums[j - 1]:
##                        j += 1
##                        while j < k and nums[k] == nums[k + 1]:
##                            k -= 1
##            i += 1
##        while i < len(nums) - 2 and nums[i] == nums[i - 1]:
##                  i += 1
##        return result
##print(Myclass().sum([-25, -10, -7, -3, 2, 4, 8, 10]))
##
##op=[[-10, 2, 8], [-7, -3, 10]]

'''3.Write a Python class which has two methods get_String and print_String. get_String accept
a string from the user and print_String print the string in upper case'''

##class Rakesh:
##    def get_String(self):
##        self.gender=input("Enter Your Gender:")
##
##    def print_String(self):
##        print("The Gender is :{}".format(self.gender.upper()))
##
##r=Rakesh()
##r.get_String()
##r.print_String()
##
##op=
##Enter Your Gender:male
##The Gender is :MALE


'''4.Write a Python program to count the frequency of words in a file'''

##f=open("Essay.txt",'r')
##d=f.read()
##d=d.split()
##count=0
##for i in d:
##    count=count+1
##print("the frequency of word are:", count)
##f.close()
##    
##output:
##
##
##the frequency of word are: 240




'''5..Write a Python program to extract characters from various text files and puts them into a list.'''

##f=open("Essay.txt",'r')
##l=[]
##a=f.readlines()
##for i in a:
##    l.append(i)
##print(l)
##f.close()
    

'''6.Write a Python program to generate the running product of the elements of an given iterable.'''


##def Gen(a):
##    b=0
##    for i in range(a):
##        b=b+i
##        yield b
##
##n=int(input("Enter A Number :"))
##result=Gen(n)
##for i in result:
##    print(i,end=" ")
##
##op=
##Enter A Number:5
##0 1 3 6 10 



'''7.A class Student is given to you. Add details in the Student class. 
Student: 
Instance Variables: studentId : PUBLIC  , studentName : PUBLIC , 
Marks: PRIVATE, grade: PRIVATE 
PUBLIC Methods: displayDetails(): , 
PRIVATE METHOD : calculateGrade():
Default constructor 
A constructor that that takes the following parameter: studentId, studentName, marks. 
Note that grade is not set either through constructor or setter as it is a calculated value. 
 
Methods 
displayDetails(): This method should display the details of the student in the following format: 
Student [name=John Smith, studentId=123, marks=95, grade=A] 
 
calculateGrade(): This is a private method that calculates the grade based on the marks that is set.
If marks is above 90, grade is set to A. If marks is between 80 and 90, grade is set to B,
if marks is between 70-80 grade is set to C, if marks is between 60-70, grade is set to D, if marks is less than 60,
grade is set to E.Use this method when you need to set or reset grade
'''
'''8.In the given Class DateFormatter, implement the method format() such that it accepts the date (date month year),
separated by comma / space or both and return the date in the format of YYYY-MM-DD. 
Eg.: 21,May,2012 / 21 May 2012 / 21, May, 2012 
Output : 2012-05-21 
 
Note the following: 
The input can have comma, space or both. No other separator is allowed 
The month can be given in full form (January, February etc) or in short 3-Letter form (Jan, feb,mar, apr, may, jun, jul, aug, sep, oct, nov, dec) . This program should accept both types. 
Output month should always be a number. 
Validate for invalid values. 
Return null for error in input.'''

##from datetime  import*
##class DateFormatter:
##    def __init__(self,date,month,year):
##        self.date=date
##        self.month=month
##        self.year=year
##
##    def display(self):
##        print("Date Is:",self.date)
##        print("Month Is:",self.month)
##        print("Year Is:",self.Year)
##
##d=DateFormatter(date,month,year)
##d.display()

import datetime
n=input("Enter the Date month and Year:")

a=datetime.datetime.strptime(n,'%d,%B,%Y')
a=datetime.datetime.strptime(n,'%d,%B,%Y')
a=datetime.datetime.strptime(n,'%d,%B,%Y')

print(a)

'''9.Write a python program on filtering consonants 
 
Note the following points: 
The method should scan the given input, remove all the consonants and return the resulting string. 
The output should contain only vowels and all other characters, including special characters should be filtered out. 
If input is null, return null. 
Example input: “Telephone”, Output: “eeoe” '''

##a=input("Enter a String to remove Cons:")
##b=" "
##for i in a:
##    if i in "aeiouAEIOU":
##        b+=i
##    
##print(b)
##
##op=Enter a String to remove Cons:Telephone
## eeoe


'''10.Write a python program to find factorial , Fibonacci series, sum of digits, product of digits, reverse of a number,
amstrong number.'''

##Factorial Number.

##def is_Factorial(fun):
##    def inner():
##        num=int(input("Enter a Number."))
##        fact=1
##        for i in range(1,num+1):
##            fact=fact*i
##        print(fact)
##        fun()
##
##    return inner
##
##@is_Factorial
##def factorial():
##    print("Hello ")
##
##factorial()
##
##op=Enter a Number.5
##120
##Hello 


# Fibonacci

##def fib(n):
##    def fibonacci(k):
##        a=0
##        b=1
##        for i in range(k+1):
##            add=a+b
##            a=b
##            b=add
##            print()
##        return fibonacci
##

#Armstrong Number

##def is_Armstrong(fun):
##    def inner():
##        num=int(input("Enter a Number."))
##        sum=0
##        temp=num
##        while(temp>0):
##            digit=temp%10
##            sum+=digit**3
##            temp//=10
##
##            if num==sum:
##                print("It is  an Armstrong Number.")
##                break
##                
##        else:
##            print("It is not an Armstrong Number.")
##
##    return inner
##@is_Armstrong
##def new():
##    pass
####result=is_Armstrong(new)
####result()
##new()
##
##op=Enter a Number.153


##It is  an Armstrong Number.


##Reverse Number

##def is_Palindrome(num):
##    def inner():
##        num=int(input("Enter a Number."))
##        sum=0
##        temp=num
##        while temp>0:
##            digit=temp%10
##            sum=sum*10+digit
##            temp=temp//10
##            
##            if num==sum:
##                print("It is a Palindrome Number.")
##                break
##            
##
##        else:
##            print("It is not a Palindrome Number.")
##    return inner
##
##@is_Palindrome
##def new():
##    pass
##new()
##
##op=
##Enter a Number.121
##It is a Palindrome Number.









