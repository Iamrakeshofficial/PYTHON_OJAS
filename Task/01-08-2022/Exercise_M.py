'''1.write a python program do multiplication program using generators and use sys module to find memory size.'''
##import sys
##def table(num):
##    for i in range(1,11):
##        yield (i*num)
##num=int(input("Enter a Number:"))
##
##a=(table(num))
##
##
##size=sys.getsizeof(a)
##print(f"The Memory size is :{size}")
##for i in a:
##    print(f"The MulTable is :{i}")

'''2..write a python program do multiplication program using function.'''

##def table(num):
##    l=[]
##    for i in range(1,11):
##        l.append(i*num)
##    return l
##a=table(5)
##import sys
##size=sys.getsizeof(a)
##print(size)
##for i in a:
##    print(i)
##

'''3.Write a Python program to extract characters from various text files and puts them into a list.'''

##fname = input("Enter file name: ")
##l2=[]
##with open(fname, 'r') as f:
##    for line in f:
##        words = line.split()
##        for i in words:
##            for letter in i:
##                if(letter.isalpha()):
##                   l2.append(letter)
##            print(l2)
##


'''4. Write a Python program to create a file where all letters of English
alphabet are listed by specified number of letters on each line.'''

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


'''5.write a python program in twin prime using outer and inner functions.'''

##def Twin_Prime(n):
##    def inner():
##        
##          for i in range(2,n+1):
##              for j in range(2,i):
##                  if i%j==0:
##                      break
##              else:
##                  x=i+2
##                  for k in range(2,x):
##                      if x%k==0:
##                          break
##                  else:
##                      print((i,x))
##    return inner()
##
##n=int(input("ENter The Range:"))
##Twin_Prime(n)  

