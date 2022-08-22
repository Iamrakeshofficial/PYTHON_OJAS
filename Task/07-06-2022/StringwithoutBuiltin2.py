##Solve questions without using builtin functions:

'''1.How do you print duplicate characters from a string?'''
##s="Python is an oop Lang"
##print("Duplicate characters in a given string: ");  
##for i in range(0, len(s)):  
##    count = 1;  
##    for j in range(i+1, len(s)):  
##        if(s[i] == s[j] and s[i]!= ' '):  
##            count = count + 1   
##            s = s[:j] + '0' + s[j+1:]    
##    if(count > 1 and s[i] != '0'):  
##        print(s[i])

'''2.How do you find all the permutations of a string?'''

'''3.How can a given string be reversed using recursion?'''

##def reverse(string):
##    if len(string) == 0:
##        return string
##    else:
##        return reverse(string[1:]) + string[0]
##a = str(input("Enter the string to be reversed: "))
##print(reverse(a))

'''4.How do you check if a string contains only digits?'''

##s=input("enter some string: ")
##num="0123456789"
##count=0
##dig=0
##for i in s:
## count+=1
## if i in num:
##     dig+=1
##if count==dig:
## print("given string contains only digits")
##else:
## print("given string contains some other elements also")

'''5.How do you print the first non-repeated character from a string?'''
##
##a=input()
##b=[]
##c=[]
##for i in a:
##    if i not in b:
##        b.append(i)
##    else:
##        c.append(i)
##print(a)
##print(b)
##print(c)
##for i in b:
##    if i not in c:
##        print(i)
##        break

'''6.How do you check if two strings are a rotation of each other?( check if two String is an anagram of each other'''


'''7.Check if the string is anagram or not , if not make it anagram.'''

##s=str(input("Enter a String:"))
##s1=str(input("Enter another String:"))
##if len(sorted(s))==len(sorted(s1)):
##    print("The string is Anagram")
##else:
##    print("The string is not Anagram")

'''8.Given string str, How do you find the longest palindromic substring in str?'''


'''9.How do you remove a given character from String?'''

##s=input("enter some string: ")
##r=input("enter some character to remove: ")
##
##for i in s:
##    if i!=r:
##        print(i,end="")
        
'''10.How do you find the length of the longest substring without repeating characters'''
