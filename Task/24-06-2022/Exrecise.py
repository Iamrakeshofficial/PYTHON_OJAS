'''1) write a python program to print string in right angle triangle 
input:python
output:
p
p y
p y t
p y t h
p y t h o
p y t h o n'''

##s1=input("Enter a String:")
##l=len(s1)
##for row in range(l):
##    for col in range(row+1):
##        print(s1[col],end=" ")
##    print()
##    

'''2) Write a Python program to split a given dictionary of lists into list of dictionaries.'''



x = {'Ram':["Apple", "Banana"], 'Sita': [2, 3], 'Laxman': ["Dragon", "strawberry"]}

print ("Dictionary of lists : " + str(x))

result = [{key : value[i] for key, value in x.items()}
      for i in range(2)]

print ("Final List of dictionaries: " + str(result))



'''3)WPP to accept student name and marks from the keyboard and creates a dictonary.
Also display student marks by taking stundent name as input.'''

##students = dict()
##n = int(input("Enter number of students :"))
##for i in range(n):
##        sname = input("Enter names of student :")
##        marks= []
##        for j in range(5):
##           mark = float(input("Enter marks :"))
##           marks.append(mark)
##        students[sname] = marks
##print("Dictionary of student created :{}".format(students))


'''4) write a program to print a program like below

          1   
        1   1
      1   2   1
    1   3   3   1
  1   4   4   4   1
1   5   5   5   5   1'''
##
##n = 5
##for i in range(n):
##    for j in range(n-i-1 ):
##        print(' ', end='')
##    for k in range(2 * i + 1):
##        print("*", end='')
##    print()

'''5) write a function which is taking another funciton as an argument.'''

##def wish(text): 
##    return text.upper() 
##  
##def pray(text): 
##    return text.capitalize() 
##  
##def greet(func): 
##    
##    greeting = func("Hello Guys.") 
##    print(greeting)
##  
##greet(wish) 
##greet(pray) 
