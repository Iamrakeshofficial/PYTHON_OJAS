'''1) write a program on magical method add , pos and neg?'''

##class Employee(object):
##    def __init__(self,name,salary):
##        self.salary=salary
##        self.name=name
##
##
##    def details(self):
##        return f"The Name is{self.name}.Salary is{self.salary}"
##
##    def __add__(self,other):
##        return self.salary+other.salary
##
##    def __sub__(self,other):
##        return self.salary-other.salary
##    def __pos__(self):
##        return self.name
##
##    def __neg__(self):
##        return self.salary
##    
##
##e=Employee("Raj",13000)
##e1=Employee("Tarak",19000)
##
##print(e+e1)
##print(e-e1)
##print(+e)
##print(-e)



'''2) write a program convert day number to date in particular year?'''



##from datetime import datetime
##day="30"
##print("the day number"+str(day))
##a=day.rjust(3+len(day),'0')
##print(a)
##year="2020"
##res=datetime.strptime(year + "-" + day,"%Y-%d")
##print("resolved"+ str(res))


'''3) write a dictionary to a file in python?'''

##dic = {100:'Apple',200:'Mango',300:'Kiwi'}
##
##with open('Rakesh.txt','w') as f:
##    f.write(f'{dic}')
##    print("Successfully Created")



'''4) find the most repeated word in a text file?'''

##from collections import Counter
##
##with open('data.txt','w') as f:
##    f.write('''Multitasking is the ability of an operating system and it is a logical extension of multiprogramming.
##            It is the ability of an operating system to execute more than one
##            task simultaneously on a single processor machine''')
##
##    
##with open('data.txt', 'r') as f:
##    r = f.read()
##    c = Counter(r)
##    print(c.most_common(2))
##
##



'''5) write a program on sprial number?

eg:-1 2 3
    8 9 4
    7 6 5 '''

##a=int(input("Enter the Number:"))
##l=[[0 for x in range(a)] for y in range(a)]
##n=1
##low=0
##high=a-1
##count=int(a+1)//2
##for i in range(count):
##    for j in range(low,high+1):
##        l[i][j]=n
##        n+=1
##    for j in range(low+1,high+1):
##        l[j][high]=n
##        n+=1
##    for j in range(high-1,low-1,-1):
##        l[high][j]=n
##        n+=1
##    for j in range(high-1,low,-1):
##        l[j][low]=n
##        n+=1
##    low+=1
##    high-=1
##for i in range(a):
##    for j in range(a):
##        print(l[i][j],end=" ")
##    print()
