##for row in range(0,5):
##    for col in range(row,5):
##        print(row*col,end=" ")
##
##    print()
##

##def wish(name,**salary):
##    print("Hello",name,salary)
##
##wish('vaddepa')
##    

##def factorial(num):
##    fact=1
##    for i in range(1,num+1):
##        
##        if num<0:
##            print("Negative number does not exist")
##
##        elif num==0:
##            print("fact is ",fact)
##
##        else:
##            fact=fact*i
##    print("Factorial of ",num,"is",fact)
##
##factorial(5)

##b=[1,2,3,4]
##l=[i for  i in b if i%2==0]
##print(l)

##s=[10,20,30,40,20,30]
##
##s=[i for i in s if i==30 ]
##print(s)

##a=[1,2,3,4]
##b=['a','b','c','d']
##d={key:val for key,val in zip(a,b)}
##print(d)


##class father:
##    pass
##class son(father):
##    pass
##class grandson(son):
##    pass


##x=[10,20,30,40]
##a=iter(x)
##print(next(a))
##print(next(a))
##print(next(a))
##print(next(a))
##print(next(a))

##def simple():
##    for i in range(10):
##        if i%2==0:
##            yield i
##
##for i in simple():
##    print(i)
##    
##with open("akash.txt",'w') as f:
##    
##    f.write("Akash Kumar SAhoo")
##    f.close()
##    print("Wrote sucessfully.")

##from pickle import*
##with open("akash.txt") as f:
##    a=pickle.dump("akash.txt")
##    
##class A:
##    def __init__(self,a):
##        print(self.a)
##
##
##    def __add__(self):
##        print(self.a)
##a=A(2)
###a.add()
##+a


##class Employee(object):
##    def __init__(self,salary):
##        self.salary=salary
####        self.name=name
##
##
##    def details(self):
##        return f"The Name is{self.name}.Salary is{self.salary}"
####    def __str__(self):
####        return f"The Name is {self.name} and Salary is :{self.salary} and i am str method"
####    def __repr__(self):
####        return f"The Name is {self.name} and Salary is :{self.salary}"
####
####    def __unicode__(self):
####        
##        
####        
######
##    def __add__(self,other):
##        return self.salary+other.salary
####
##    def __sub__(self,other):
##        return self.salary-other.salary
##
##    def __lt__(self,other):
##        return self.salary<other.salary
##    def __le__(self,other):
##        return self.salary<=other.salary
##    def __gt__(self,other):
##        return self.salary>other.salary
##
####    def __pos__(self,
####    
##
##
##
##e=Employee(13000)
##e1=Employee(19000)
####print(str(e))
####print(e)
####
##print(e+e1)
