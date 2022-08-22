# Operator Overloading
##
##class A:
##	def __init__(self, x):
##		self.x = x
##	def __add__(self, other):
##		return self.x + other.x
##			
##class B:
##	def __init__(self, x):
##		self.x = x
##		
##a = A(100)
##b = B(200)
##print(a+b)
##A.__add__(a, b)



##10+20		int.__add__(10, 20)
##'a'+'b'			str.__add__('a', 'b')
##a+b				A.__add__(a, b)




##class Employee(object):
##    def __init__(self,name,salary):
##        self.salary=salary
##        self.name=name


##    def details(self):
##        return f"The Name is{self.name}.Salary is{self.salary}"
##    def __str__(self):
##        return f"The Name is {self.name} and Salary is :{self.salary} and i am str method"
##    def __repr__(self):
##        return f"The Name is {self.name} and Salary is :{self.salary}"
##
##    def __unicode__(self):
##        
        
##        
##
##    def __add__(self,other):
##        return self.salary+other.salary
##
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
##e=Employee("Raj",13000)
##e1=Employee("Tarak",19000)
####print(str(e))
##print(e)
##
##print(e+e1)
##print(e-e1)
##print(e<e1)
##print(e<=e1)
##print(e>e1)


##class Flower(object):
##    def __stattr__(self,key,value):
##        self.__dict__[key]=value
##
##    def __getattr__(self,item):
##        return self.__dict__[item]
##
##    def __delattr__(self,item):
##        del self.__dict__[item]
##
##
##f=Flower()
##f.color='red'
##print(f.color)
##f.height='10cm'
##print(vars(f))
##print(f.height)
##del (f.height)
##print(f.height)
##print(vars(f))

##class C:
##    def __nonzero__(self):
##        return False
##
##c = C()
##print(bool(c))
##print(bool(C))


##class Person:
##    def __init__(self, name, age):
##        self.name = name
##        self.age = age
##
####    def __eq__(self, other):
####        return isinstance(other, Person) and self.age == other.age
##
##    def __hash__(self):
##        return hash(self.age)
##
##p=Person("Tarak",24)
####print(hash(p))
##p.__hash__()
##        
