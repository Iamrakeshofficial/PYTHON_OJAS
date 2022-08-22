'''1. Write a Python program to make a chain of function decorators (bold, italic, underline etc.) in Python. '''

##def make_bold(fn):
##    def wrapped():
##        return "<b>" + fn() + "</b>"
##    return wrapped
##
##def make_italic(fn):
##    def wrapped():
##        return "<i>" + fn() + "</i>"
##    return wrapped
##
##def make_underline(fn):
##    def wrapped():
##        return "<u>" + fn() + "</u>"
##    return wrapped
##
##@make_bold
##@make_italic
##@make_underline
##def hello():
##    return("Hello Guys.")
##print(hello())

'''2. Write a Python program to extract specified size of strings from a give list of string values using lambda.
Original list:
['Python', 'list', 'exercises', 'practice', 'solution']
length of the string to extract:
8
After extracting strings of specified length from the said list:
['practice', 'solution']'''

##def extract(lis,a):
##    res=list(filter(lambda x:len(x)==a,lis))
##    return res
##
##lis=['Python', 'list', 'exercises', 'practice', 'solution']
##
##print("Original List is:",lis)
##a=8
##print("\n After Extracting the list:",extract(lis,a))


'''3. Write a Python program to create a deep copy of a given dictionary. Use copy.copy'''

##import copy
##d={'apple':100,'banana':40,'kiwi':300}
##
##d1=copy.deepcopy(d)
##print(d1)
##d1['banana']=50
##print(d1)
##print(d)




'''4. Write a Python Program to Check a Number is a Spy Number or Not? note:- without  forloop.'''

##num=int(input("Enter a Number to check Spy Number:"))
##temp=num
##sum=0
##prod=1
##
##while temp>0:
##    dig=temp%10
##    sum=sum+dig
##    prod=prod*dig
##    temp=temp//10
##
##
##print("\nThe Sum Of The Digits are:",sum)
##print("\nThe Product Of the Digit is:",prod)
##
##if sum==prod:
##    print(num,"is a Spy Number.")
##else:
##    print(num,"is a not Spy Number.")



'''5. Write a Python program to find the XOR of two given strings interpreted as binary numbers.
Input:
['0001', '1011']
Output:
0b1010
Input:
['100011101100001', '100101100101110']
Output:
0b110001001111'''

##def test(nums):
##    return bin(int(nums[0],2) ^ int(nums[1],2))
##nums =  ["0001", "1011"]
##n=['100011101100001', '100101100101110']
##print("The XOR of two given strings interpreted as binary numbers is:",test(nums))
##print("The XOR of two given strings interpreted as binary numbers is:",test(n))
