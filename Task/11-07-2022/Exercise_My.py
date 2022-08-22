"""1). wap take one example duck typing,
 in this methods you must take 3 defferent classes names and in each one class you must take 3 defferent methods."""

##class Animal:
##    def talk(self):
##        print("Animal can talk also.")
##
##    def walk(self):
##        print("Animal can walk.")
##
##    def fly(self):
##        print("Animals Can't Fly.")
##
##
##class Employee:
##    def details(self):
##        print("I am an Employee of Ojas.")
##
##    def show(self):
##        print("I can show my skills.")
##
##    def walk(self):
##        print("Employees can Walk.")
##
##class Student:
##    def performance(self):
##        print("Student can perform well.")
##
##    def show_details(self):
##        print("Show the details of students.")
##
##
##    def walk(self):
##        print("Students Can walk fast also.")
##
##def function(obj):
##    obj.walk()
##
##a=Animal()
##function(a)
##
##e=Employee()
##function(e)
##
##s=Student()
##function(s)
##    


""" 2). wap take one example wrong method overloding."""

##class Myclass:
##    def __init__(self,age):
##        self.age=age
##    def disp(self):
##        print("My Age is:",self.age)
##
##    def disp(self):
##        print("My age is:")
##
##obj=Myclass(10)
##obj.disp()
##obj.disp()





""" 3). wap solve this pattern

  5 5 5 5 5
   * * * *
    3 3 3 
     * *
      1     """

##n=5
##for i in range(n,0,-1):
##    for j in range(n,0,-1):
##        if i>=j:
##            if i%2==1:
##                print(i,end=" ")
##
##            else:
##                print("*",end=" ")
##        else:
##            print(" ",end="")
##    print()




""" 4).wap  take one eaxmple in hierarchical method."""

##class Ceo(object):
##    def __init__(self,id,company):
##        self.id=id
##        self.company=company
##
##    def details(self):
##        print("I am the CEO and My Id is:{}\n Company Name is:{}".format(self.id,self.company))
##
##
##class Manager(Ceo):
##    def __init__(self,name,company):
##        self.name=name
##        super().__init__(id,company)
##
##    def show_details(self):
##        print("I am The Manager and My Name is:{}\n Company Name is:{}".format(self.name,self.company))
##
##
##class Employee(Ceo):
##    def __init__(self,company,Desg):
##        self.Desg=Desg
##        super().__init__(id,company)
##        
##
##    def display(self):
##
##        print("I am an Employee and My Company Name Is:{}\n My Designation Is:{}".format(self.company,self.Desg))
##
##
##e=Employee("Ojas","Python Dev")
##e.display()
##
##m=Manager("Kalyan","Ojas")
##m.show_details()


    
""" 5) What is the difference between Python Arrays and lists take one eaxmple ?"""


###ARRAY###

##from array import *
##l= array('i', [1,2,3,4,5])
##for i in l:
##    print(i)

##
##l=[10,20,30,40]
##print(l)


