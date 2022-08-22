'''1.Write a Python program to read last n lines of a file.'''

##f=open("News.txt",mode='r')
##lines=f.readlines()
##l=lines[-3:]
##print(l)
##
##f.close()




'''2.Write a Python program to read a file line by line and store it into a list.'''

##with open('News.txt') as f:
##    li = [line.rstrip() for line in f]
##
##print(li)




'''3.Write a Python program to read a file line by line store it into a variable.'''

##f = open("News.txt","r")
##str=""
##
##for i in range(0,100):
##    str=str + f.read(i)
##
##print(str)


'''5. Write a Python program to count the frequency of words in a file.'''

##from collections import Counter
##
##def word_count(News):
##        with open(News) as f:
##                return Counter(f.read().split())
##
##print("Number of words in the file :\n",word_count("News.txt"))


'''6. Write a Python program to read a random line from a file.'''

##import random
##def rakesh(News):
##    lines = open(News).read().splitlines()
##    return random.choice(lines)
##print(rakesh('News.txt'))


'''7.Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt.'''


##for i in range(65, 65+26):
##    filename = chr(i)+'.txt'
##    with open(chr(i) + ".txt", "w") as file:
##        file.writelines(chr(i))

'''8.Write a Python program to extract characters from various text files and puts them into a list.'''

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

'''9.Write a Python program that takes a text file as input and returns the number of words of a given text file
Note: Some words can be separated by a comma with no space.'''

##fname = input("Enter file name: ")
##with open(fname,'r') as f:
##	lines=f.read()
##	words=lines.split()
##	print(len(words))


'''10.Write a Python program to create a file where all letters of English
alphabet are listed by specified number of letters on each line .'''

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

