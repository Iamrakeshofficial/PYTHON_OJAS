'''1.Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.'''

##def nums(a,b):
##    for i in range(a,b+1):
##        if i%7==0 and i%5!=0:
##            print(i,end=",")
##nums(1,80)


'''2.Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320 '''

##l=eval(input("enter some list: "))
##for i in l:
##    fact=1
##    for j in range(1,i+1):
##        fact=fact*j
##    print(fact,end=",")
        
'''3.With a given integral number n, write a program to generate a dictionary that contains (i, i*i)
such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}'''


##n=int(input("enter any number: "))
##d={}
##for i in range(1,n+1):
##    d1={i:i*i}
##    d.update(d1)
##print(d)

'''4.Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98') '''

##n=input("enter some sequence: ")
##m=n.split(sep=",")
##print(tuple(m))
##print(list(m))

'''5.Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods. '''


'''6.Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24 '''

##def func(D):
##    for i in D:
##        C=50
##        H=30
##        q=(2 * C * i)/H
##        q=int(q)
##        for i in range(q):
##            if i*i>q:
##                print(i-1,end=",")
##                break
##l=100,150,180
##func(l)



'''7.Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,????Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]'''


'''8.Write a program that accepts a comma separated sequence of words as input and
prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world '''

##n=input("enter some sequence: ")
##l=n.split(",")
##for i in sorted(l):
##    print(i,end=",")
  


'''9.Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT'''

##a  = """Hello world
##Practice makes perfect"""
##a.upper()
##print(a)

'''10.Write a program that accepts a sequence of whitespace separated words as input
and prints the words after removing all duplicate words and sorting them alphanumerically.

Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world '''

##s=input("enter some sequence: ")
##l=s.split(" ")
##l1=[]
##for i in l:
##    if i not in l1:
##        l1.append(i)
##for i in sorted(l1):
##    print(i,end=" ")
    
'''11.Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input
and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console. '''

##def my_fun(bina):
##    for binary in bina:
##        bin2=binary[::-1]
##        k=0
##        digit=0
##        for i in bin2:
##            twos=2**k
##            k=k+1
##            if i=="1":
##                digit=digit+twos
##        if digit%5==0:
##            print(binary)
##binary=["0100","0011","1010","1001"]
##my_fun(binary)
    
'''s="0100,0011,1010,1001"
l=s.split(",")
print(l)
for bina in l:
    bina2=l[::-1]
    k=0
    digit=0
    for j in bina2:
        twos=2**k
        k=k+1
        if j=="1":
            digit+=twos
        if digit%5==0:
            print(bina) '''

'''12.Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line. '''

    
##def my_fun(sma,big):
##    for i in range(sma,big):
##        count=0
##        even=i
##        while i>0:
##            div=i%10
##            if div%2==0:
##                count=count+1
##            i=i//10
##        if count==len(str(even)):
##            print(even,end=",")
##sma=int(input())
##big=int(input())
##my_fun(sma,big)


'''13.Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3'''

##s=input("enter a a sentence: ")
##l=0
##d=0
##for i in s:
##    if i.isalpha():
##        l+=1
##    elif i.isdigit():
##        d+=1
##print("LETTERS ",l,"\nDIGITS",d)

'''14.Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9 '''

##s=input("enter a a sentence: ")
##u=0
##l=0
##for i in s:
##    if i.isupper():
##        u+=1
##    elif i.islower():
##        l+=1
##print("UPPER CASE ",u,"\nLOWER CASE ",l)

'''15.Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106 '''


##
##a=input()
##k=0
##for i in range(1,5):
##    temp=str(a)*i
##    k+=int(temp)
##print(k)
    
##n=input()
##a=n
##b=a*2
##c=a*3
##d=a*4
##k=int(a)+int(b)+int(c)+int(d)
##print(k)































































