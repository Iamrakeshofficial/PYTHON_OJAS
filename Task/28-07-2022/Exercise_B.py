'''1) write a python program on files to check whether the given file exists or not. 
if it is available then print its content? '''

##import os
##a=os.path.isfile("student.txt")
##print(a)
##f=open('student.txt',mode='r')
####f.write("Tarak is a Godd Boy")
####f.lclose()
##data=f.read()
##print(data)
##f.close()

'''2) Write a Python program to create a file where all letters of English alphabet are listed by specified
number of letters on each line.'''


##number=int(input("Enter  The Number of characters u Want in a Line:"))
##alphabets=""
##for i in range(65,65+26):
##    char=chr(i)
##    alphabets+=char
##f='sample.txt'
##with open(f,"w") as file:
##     modified = [alphabets[i:i + number] +
##                       "\n" for i in range(0, len(alphabets), number)]
##
##     file.writelines(modified)
##
##     print("Successfully Done.")
##    


'''3) Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt.'''

##for i in range(65, 65+26):
##    filename = chr(i)+'.txt'
##    with open(chr(i) + ".txt", "w") as file:
##        file.writelines(chr(i))
##

'''4) Write a Python program to interleave multiple lists of the same length. Use itertools module. '''

##import itertools
##
##def interleave(l1,l2,l3):
##    result = list(itertools.chain(zip(l1, l2, l3)))
##    return result
##     
##l1 = [100,200,300,400,500,600,700]
##l2 = [10,20,30,40,50,60,70]
##l3 = [1,2,3,4,5,6,7]
##print(interleave(l1,l2,l3))

'''5) Using lambda function print following output.
1
2
fizz
4
buzz
fizz
7
8
fizz
buzz
11
fizz
13
14
fizzbuzz
16
17
fizz
19
buzz
fizz
22
23
fizz
buzz
26
fizz
28
29
fizzbuzz'''

##rs = lambda i: 'FizzBuzz' if i%15 == 0 else 'Fizz' if i%3 == 0 else 'Buzz' if i%5 == 0  else i
##print (list( map ( rs, [ i for i in range( 1,31 )  ]) ) )
