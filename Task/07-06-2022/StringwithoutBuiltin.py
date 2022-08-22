'''Solve without using builtin methods:'''

'''1. WAP to print middle charector of the string.'''
##n=input("Enter a String:")
##print("The Original String is:",n)
##middle=n[len(n)//2]
##print("The middle String is:",middle)

'''2. WAP to print half reverse of the string. 
Input: KNOWLEDGE
Output: EGDELKNOW'''
##s="KNOWLEDGE"
##print(s[-1:-6:-1]+s[:4])


'''3. WAP to remove all the vowels from the given string.'''

##n=input("Enter a String:")
##vowels=['a','e','i','o','u','A','E','I','O','U']
##result=""
##for i in range(len(n)):
##    if n[i] not in vowels:
##        result=result+n[i]
##print("\n The String after Removing Vowels Is:",result)


'''4. WAP to insert * in front of every vowels in the string.
Input: BANANA
Output: B*AN*AN*A'''

##s="BANANA"
##v=['a','e','i','o','u','A','E','I','O','U']
##output=str()
##for i in s:
##    if i in v:
##        i="*"+i
##    output=output+i
##print(output)


'''5. WAP to count number of words in the string.'''

##string=input("Enter string:")
##count=1
##for i in string:
##    if i==" ":
##        count=count+1
##print("Length of the Word is:")
##print(count)

'''6. WAP to remove extra space from the given string.'''

##string = input("Enter a String : ")
##result=''
##for i in string:
##    if i!=' ':
##        result+=i
##print("String after removing the spaces :",result,end=" ")

'''7. WAP to insert string in between the given string.
Input: Ojas technologies 
Output: Ojas innovative technologies'''

##s="Ojas Technologies"
##print(s[0:4]+'Innovative'+s[5:])

'''8. WAP to find the ascci value of given char.'''

##n=input("enter A char to fin ascii:")
##print(ord(n))

'''9. insert ojas in front of every string.'''
##string = input("enter the string:")
##insert = input("enter the string:")
##for r in string:
## print(r,end = " ")
## print(insert,end = " ")



'''10. insert ojas in every extra space in the string.'''

##string = input("enter the string with space:")
##insert = input("enter the string:")
##for i in string:
##    print(i,end = "")
##    if i == " ":
##        print(insert,end = " ")
