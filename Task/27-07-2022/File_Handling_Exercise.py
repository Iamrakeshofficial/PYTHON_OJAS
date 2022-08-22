'''
Q1. Write a program in python to replace all word “the” by
another word “them” in a file “poem.txt”. '''

##f=open("Essay.txt")
##d=f.read()
##d=d.replace("the","them")
##f.close()
##f=open("Essay.txt","w")
##f.write(d)
##f.close()

'''
Q2. Write a program in python to replace a character by another character
in a file “story.txt”. (Accept both the characters from the user) '''

##
##f=open("Essay.txt")
##g=f.read()
##n1=input("Enter a charactor:")
##n2=input("Enter a replaced charactor:")
##g=g.replace(n1,n2)
##f.close()
##f=open("Essay.txt","w")
##f.write(g)
##f.close()



'''
Q3. Write a program in python to replace all the ‘a’ by ‘@’ in a file “data.txt”. '''
##
##f=open("History.txt",'w+')
##f.write("Welcome to OJas Family Guys.Wish Ypu all The luck for Your Bright Future.")
##f.close()


##f=open("History.txt",'r')
##k=f.read()
##k=k.replace('a','@')
##f.close()
##f=open("History,txt","w")
##f.write(k)
##f.close()

'''
Q4. Write a program in python to read file
“data.txt” and display only those lines whose length is more
than 40 characters. '''

##f=open("Essay.txt",'r')
##k=f.readlines()
##for i in k:
##    if len(i)>40:
##        print(i)
##f.close()


'''
Q5. Write a program in python to remove all duplicate lines from the
file “story.txt”. '''


##f=open("Essay.txt",'r')
##m=f.readlines()
##m1=[]
##for i in m:
##    if i not in m1:
##        m1.append(i)
##print(m1)
##f.close()
    
'''
Q6. Write a program in python to display only unique words from the file
“story.txt”.'''

##f=open("Essay.txt","r")
##k=f.read()
##k=k.split()
##str1=""
##
##for i in k:
##    if i not in str1:
##        str1=str1+i
##        print(i,end=" ")
##f.close()

'''
Q7. Write a program in python to count the frequency of each vowels in
a file “task.txt”.'''

##f = open("Essay.txt", "r")
##d = f.read()
##
##xa=xe=xo=xu=xi=0
##
##for i in d:
##     if i=='a' or i=='A':
##         xa=xa+1
##     if i=='e' or i=='E':
##         xe=xe+1
##     if i=='i' or i=='I':
##         xi=xi+1
##     if i=='o' or i=='O':
##         xo=xo+1
##     if i=='u' or i=='U':
##         xu=xu+1
##print("Frequency of vowel \"a\" is", xa)
##print("Frequency of vowel \"e\" is", xe)
##print("Frequency of vowel \"i\" is", xi)
##print("Frequency of vowel \"o\" is", xo)
##print("Frequency of vowel \"u\" is", xu)
'''
Q8. Write a program in python to count those words whose length is more than
7 characters in a file “story.txt”.'''

##f=open("Essay.txt",'r')
##k=f.read()
##k=k.split()
##count=0
##for i in k:
##    if len(i)>7:
##        count=count+1
##print("the total words are:",count)
##f.close()

'''
Q9. Write a program in python to count those lines from the file “div.txt”
which are starting from ‘T’ or ‘M’.'''

##f=open("Essay.txt",'r')
##z=f.readlines()
##count=0
##for i in z:
##    if i[0]=='T' or i[0]=='M':
##        count=count+1
##        print(i)
##print("the number of lines are:",count)
##f.close()

'''
Q10. Write a program in python to count those lines from the file “div.txt”
which are not starting from ‘M’.'''

##f=open("Essay.txt",'r')
##b=f.readlines()
##count=0
##for i in b:
##    if i[0]!='M':
##        count=count+1
##print("The Line Which is not start with 'M' charactor are :",i,"\n","The number of Lines are:",count)
##f.close()

'''
Q11. Write a program in python to display those words from a file
“image.txt” which are ending from alphabet ‘m’.'''

##f=open("Essay.txt",'r')
##c=f.read()
##c=c.split()
##for i in c:
##    if i[-1]=='m':
##        print(i)
##f.close()

'''
Q12. Write a program in python to read all lines of file “data.txt”
using readline() only.'''

##f=open("Essay.txt",'r')
##k=f.readline()
##while k:
##    k=f.readline()
##    print(k,end="")
##f.close()

'''
Q13. Write a program in Python to copy the entire content from file “data.txt”
to “story.txt”'''

##f=open("Essay.txt",'r')
##f2=open("Poem.txt",'w')
##R=f.read()
##f2.write(R)
##f.close()
##f2.close()

'''
Q14. Write a program in Python to copy the alternate lines from file
“data.txt” to “story.txt”'''

##f=open("Essay.txt",'r')
##m1=open("Poem.txt",'w')
##k=f.readlines()
##for i in range(len(k)):
##    if i%2==0:
##        m1.write(k[i])
##f.close()
##m1.close()

'''
Q15. Write a program in Python to read the entire content from file
“data.txt” and copy the contents to “story.txt” in upper case. '''

##f=open("Essay.txt",'r')
##f2=open("Poem.txt",'w')
##d=f.readlines()
##
##for i in d:
##    f2.write(i.upper())
##f.close()
##f2.close()

'''
Q16. Write a program in Python to read the entire content from file
“data.txt” and copy only those words to “story.txt” which start from vowels.'''

##f=open("Essay.txt",'r')
##f2=open("Poem.txt",'w')
##l=f.readlines()
##vowels='aeiouAEIOU'
##for i in l:
##    if i[0] in vowels:
##        f2.write(i)
##f.close()
##f2.close()

'''
Q17. Write a program in Python to read the entire content
from file “data.txt” and copy only those words in separate lines to
“story.txt” which are starting from lower case alphabets .'''

##f=open("Essay.txt",'r')
##f2=open("Poem.txt",'w')
##d=f.read()
##str1=d.split()
##for i in str1:
##    if i[0].islower():
##        f2.write(i)
##        f2.write("\n")
##        
##f.close()
##f2.close()


'''
Q18. Write a program in Python to read file “data.txt” and copy only
those lines to “story.txt” which are starting from alphabets “A” or “T”.'''

##f=open("Essay.txt",'r')
##f2=open("Poem.txt",'w')
##d=f.readlines()
##for i in d:
##    if (i[0]=='T' or i[0]=='A'):
##        f2.write(i)
##f.close()
##f2.close()

'''
Q19. Write a program in Python which display the longest word from file
“star.txt”'''

##f=open("Essay.txt",'r')
##d=f.read()
##d=d.split()
##l=""
##for i in d:
##    if len(i)>len(l):
##        l=i
##print("Longest word Are:",l)
##f.close()
    
'''
Q20. Write a program in Python which display the longest line from file
“star.txt” '''


##f=open("Essay.txt",'r')
##d=f.readlines()
##long=''
##for i in d:
##    if len(i)>len(long):
##        long=i
##print("The longest line is :",long)
##f.close()
'''Q21. Write a program in Python to read the file “star.txt” and display the entire content after removing leading
and trailing spaces.'''


##f = open("Essay.txt", "r")
##d = f.readlines()
##for i in d:
##    print(i.strip())
##f.close()

'''
Q22. Write a program in python that read the content from file “sumit.txt”
and display all numbers. '''

##f=open("Essay.txt",'r')
##d=f.read()
##for i in d:
##    if i.isdigit():
##        
##        print(i,end=' ')
##f.close()

'''
Q23. Write a program in Python that display the second and second
last line from the file “life.txt” '''


##f=open("Essay.txt",'r')
##d=f.readlines()
##print("The second line is :",d[1])
##print("The second last line is :",d[-2])
##f.close()

'''24.Consider a binary file “data.dat” which stores the record of “Hotel” in the form of list containing Room_no, Price, Room_type. Do the following task in a file 

Write a function addrec() to add a record in a file. 

Write a function disp() to display all the records from the file. 

Write a function specific_disp(room_no) which takes room number as argument and display its details. 

Write a function mod(room_no) which takes room number as argument and modify it’s details. 

Write a function del(room_no) which takes room number as argument and delete it’s record from file “data.dat” '''

##def addrec():
##     L=[ ]
##     f=open("Studentdata.pdf","ab")
##     rn = int(input("Enter Room Number"))
##     pr = int(input("Enter the price of room"))
##     rt = input("Enter the type of room")
##     L  = [rn, pr, rt]
##     pickle.dump(L, f)
##     print("Record added in the file")
##     f.close()
##addrec() 
##
##



'''25.Write a menu driven program which shows all operations on Binary File 

Add Record 

Display All Record 

Display Specific Record 

Modify Record 

Delete Record 

Use “data.dat” file which stores the record of “Hotel” in the form of list containing Room_no, Price, Room_type '''



'''26.Write a function disp75() in Python to display only those records of students from file “school.dat”
who scored more than 75 percent marks. Structure stored in “school.dat”
is in the form of list containing information like [rollno, name, class, percentage] '''

def disp75():
    f=open("Studentdata.pdf", "rb")
    d=f.read()
    print(d)
    f.close

disp75()

'''27.Write a function dispname() in Python which will display only names of all the students from file “school.dat”.
Structure stored in “school.dat” is in the form of list containing information like [rollno, name, class, percentage]''' 

'''28.Write a function disp12() in Python which will display records of class 12th students from file “school.dat”.
Structure stored in “school.dat” is in the form of list containing information like [rollno, name, class, percentage]''' 

'''29.Write a function search(name) in Python which will display record of a student from file “school.dat”
whose name is passed as an argument. Structure stored in “school.dat”
is in the form of list containing information like [rollno, name, class, percentage]''' 

'''30.Write a function disp_mob(model no.) in Python which will display the record of a mobile from “mobile.dat”
whose model number (integer type) is passed as an argument. Structure of “mobile.dat” is [Mobile id, Mobile brand,
Model No., Price] '''
