'''1. How would you confirm that 2 strings have the same identity?'''
##s1="Ram"
##s2="Ram"
##if id(s1)==id(s2):
##    print("Both string have same identity.")
##else:
##    print("False")

'''2. How would you check if each word in a string begins with a capital letter?'''
##s1=input("Enter some string: ")
##if s1.istitle():
##    print("yes")
##else:
##    print("no")

    
'''3. Check if a string contains a specific substring'''
##s="Ram is a good Boy"
##sub="is"
##if s.find(sub):
##    print("Yes")
##else:
##    print("No")

'''4. Find the index of the first occurrence of a substring in a string'''
##s="Python is an OOP Lang"
##print(s.find('o'))


'''5. Count the total number of characters in a string'''
##s="Python"
##print(len(s))

'''6. Count the number of a specific character in a string'''
##s="Python"
##print(s.count('t'))

'''7. Capitalize the first character of a string'''
##s="python"
##s1=s.capitalize()
##print(s1)

'''8. What is an f-string and how do you use it?'''

##name = 'Rakesh'
##age = 23
##print(f"Hello, My name is {name} and I'm {age} years old.")

'''9. Search a specific part of a string for a substring'''
##s="Python is an oop Lang"
##print(s.index('oop'))
##10. Interpolate a variable into a string using format()
'''11. Check if a string contains only numbers'''
##s="1223"

##b=s.isdigit()
##print(b)
'''12. Split a string on a specific character'''
##s="Python-is-an-oop-lang"
##l=s.split("-")
##print(l)
'''13. Check if a string is composed of all lower case characters'''
##s="python"
##b=s.islower()
##print(b)

'''14. Check if the first character in a string is lowercase'''
##s="pYTHON"
##print(s.islower())

'''15. Can an integer be added to a string in Python?'''
'''16. Reverse the string “hello world”.'''
##s="hello world"
##print(s[::-1])
'''17. Join a list of strings into a single string, delimited by hyphens'''
##s=["Python","Is","An","Oop","Lang"]
##k="-"
##k1=k.join(s)
##print(k1)
##18. Check if all characters in a string conform to ASCI
'''19. Uppercase or lowercase an entire string'''
##s="python"
##s1=s.upper()
##print(s1)
##s="PYTHON"
##s2=s.lower()
##print(s2)
'''20. Uppercase first and last character of a string.'''
##s=input("Enter a string:")
##print(s[0].upper()+s[1:-1]+s[-1].upper())

'''21. Check if a string is all uppercase.'''
##s="PYTHON"
##s1=s.isupper()
##print(s1)
'''22. When would you use splitlines()?'''
##Python String splitlines() method is used to split the lines at line boundaries.
##The function returns a list of lines in the string, including the line break(optional)
##txt = "Thank you for the music\nWelcome to the jungle"
##
##x = txt.splitlines()
##
##print(x)
'''23. Give an example of string slicing.'''
##s="Python"
##print(s[1:6:2])
'''24. Convert an integer to a string.'''
##s=123
##n=str(s)
##print(n,type(n))
'''25. Check if a string contains only characters of the alphabet.'''

##s1='Python'
##check_s1 = s1.isalpha()
##print(check_s1)

'''26. Replace all instances of a substring in a string.'''

##string_a = "The brown eye."
##string_b = string_a.replace("brown", "blue")
##print(string_a)
##print(string_b)
'''27. Return the minimum character in a string.'''
##str1 = "salute to the mother earth"
##str2 = "salute-to-the-mother-earth!"
##str3 = "salutetothemotherearth"
## 
##print("Minimum alphabetic character in the string1 is :", min(str1))
##print("Minimum alphabetic character in the string2 is :", min(str2))
##print("Minimum alphabetic character in the string3 is :", min(str3))


'''28. Check if all characters in a string are alphanumeric'''
##s="Python123"
##s1=s.isalnum()
##print(s1)
'''29. Remove whitespace from the left, right or both sides of a string'''
##s=" Python is an oop Lang "
##s1="".join(s.split())
##print(s1)
'''30. Check if a string begins with or ends with a specific character?'''

##s="happy"
##print(s[0]=="h" and s[-1]=="h")
##

