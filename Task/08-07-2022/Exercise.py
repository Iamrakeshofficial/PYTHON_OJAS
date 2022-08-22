"""1.Define Multiple inheritance and write an example?"""


##class Student_1(object):
##    def __init__(self):
##        self.name="Rakesh"
##        self.age=19
##
##    def get_Name(self):
##        print("My name is :{}\n My age is:{}".format(self.name,self.age))
##
##class Student_2(object):
##    def __init__(self):
##        self.name="RAJ"
##        self.id=22069
##
##    def get_Name(self):
##        print("My name is :{}\n My Id is:{}".format(self.name,self.id))
##
##                
##class Students(Student_1,Student_2):
##    def __init__(self):
##        Student_1.__init__(self)
##        Student_2.__init__(self)
##
##    def get_Name(self):
##        print("My name is :{}\n My Id is:{}".format(self.name,self.id))
##
##        
##s=Students()
##s.get_Name()

        

    


"""2.WAP on Duck type polymorphism. with example."""

##class India:
##    def language(self):
##        print("The Most used language is Hindi")
##
##    def capital(self):
##        print("The Capital of India is Delhi")
##
##    def about(self):
##        print("India is Devloping Country")
##
##class USA:
##    def language(self):
##        print("The Most used language is English")
##
##    def capital(self):
##         print("The Capital of USA is Washington")
##
##    def about(self):
##         print("USA is Devloped Country")
##
##
##i=India()
##u=USA()
##
##for country in(i,u):
##    country.language()
##    country.capital()
##    country.about()
   
##def func(obj):
##    obj.language()
##    obj.capital()
##    obj.about()
##
##func(i)
##func(u)


"""3.demonstrate strong typing method in polymorphism with example."""

##class India:
##    def language(self):
##        print("The most common language in INDIA is HINDI.")
##
##class America:
##    def language(self):
##        print("The most common Language in USA is ENGLISH.")
##
##
##class Russia:
##    def act(self):
##        print("The most Powerful country is Russia.")
##
##def function(obj):
##    if hasattr(obj,'language'):
##        obj.language()
##    if hasattr(obj,'act'):
##        obj.act()
##
##i=India()
##function(i)

##a=America()
##function(a)

##r=Russia()
##function(r)


"""4.write a program Russian Multiplication using class and object."""

##class Mult:
##    def russian(self,a,b):
##        res=0
##        while b>0:
##            if b&1:
##                res=res+a
##            a=a<<1
##            b=b>>1
##        return res
##obj=Mult()
##print(obj.russian(4,5))




"""5.write a program about ojas organization parent class is ojas
and child class is OILC write differnt batches as methods define batchs name with inheritance."""


##class Ojas(object):
##    def __init__(self):
##        print("Hello Guys")
##
##    def python(self):
##        print("I am from  OILC-303 Python Batch.")
##
##    def java(self):
##        print("I am from  OILC-203 Java Batch.")
##
##    def testing(self):
##        print(" I am from  OILC-703 Testing Batch.")
##    def idm(self):
##        print(" I am from  OILC-503 Idm Batch.")
##
##    def devOps(self):
##        print(" I am from  OILC-707 Devops Batch.")
##
##    def del_Boomi(self):
##        print(" I am from  OILC-403 Del_Boomi Batch.")
##
##
##class OILC(Ojas):
##    def __init__(self):
##        print(" I am From Child  class Constructor.")
##
##    def display(self):
##        print("All the Methods in Parent Class")
##
##o=OILC()
##o.python()

##o.java()
##o.idm()
##o.del_Boomi()
##    
