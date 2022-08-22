n=input("Enter a String:")
vowels=['a','e','i','o','u','A','E','I','O','U']
result=""
for i in range(len(n)):
    if n[i] not in vowels:
        result=result+n[i]
print("\n The String after Removing Vowels Is",result)
