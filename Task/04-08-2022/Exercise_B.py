'''1) take a list and output has to be repeated of the second half of the list elements
input = [1,2,3,4,5,6]
output = [4,5,6,4,5,6]'''

##list = [10, 20, 30, 40, 50, 60]
##
##
##list1= list [:3]
##
##list2= list [3:]
##
##print("list : ",list)
##print("list1: ",list1)
##print("list2: ",list2)


'''2) Write a Python program to check that a string contains only a certain
set of characters (in this case a-z, A-Z and 0-9)'''

##import string
##text = input("Enter: ")
##correct = string.ascii_letters + string.digits
##status = True
##for char in text:
##    if char not in correct:
##        status = False
##if status:
##    print('Correct')
##else:
##    print('InCorrect')

'''3) Write a Python program that matches a string that has an a followed by zero or more b's.'''

##a=input("Enter Zeros and b's:")
##if "b" in a:
##    print(True)
##else:
##    print(False)

'''4) Write a Python program that matches a word at the beginning of a string.'''

##a=input("Enter a string:")
##b=input("Enter the word to check:")
##c=a.split()
##if b==c[0]:
##    print(True)
##else:
##    print(False)


'''5) open a file and enter a lists like each list is having two or more elements
in to the file and retrieve their details in the ouput in lists'''


##names= ["Vaddepa","Rakesh","Priya"]
##with open("file.txt","w") as f:
##    for i in names:
##        f.write("%s\n"%i)
##        print(i)

