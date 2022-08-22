# Single Inheritance
##class Father:					# Parent Class
##	money = 1000
##	
##	def show(self):
##		print("Parent Class Instance Method")
##		
##	@classmethod
##	def showmoney(cls):
##		print("Parent Class Class Method:", cls.money)
##		
##	@staticmethod
##	def stat():
##		a = 10
##		print("Parent Class Static Method:", a)
##		
##class Son(Father):				# Child Class
##	def disp(self):
##		print("Child Class Instance Method")
##
##s = Son()
##s.disp()
##s.show()
##s.showmoney()
##s.stat()

'''Single Inheritance'''
##class Teacher(object):
##    org="NIT"
##    def show(self,id):
##        self.id=id
##        print("I am from Parent Class and MY Id is:{}".format(self.id))
##
##    @classmethod
##    def show_Details(cls,name):
##        cls.name=name
##        print("I am from Parent Class and My Name is :{}\n My Organization is:{}".format(cls.name,cls.org))
##
##    @staticmethod
##    def abc():
##        a=10
##        print("I am From Parent class ",a)
##
##
##class Student(Teacher):
##    def display(self):
##        print(" I am from Child Class")
##
##s=Student()
##s.display()
##s.show(2)
##s.show_Details("Rakesh")
##s.abc()
##        

'''Single Inheritance With Constructor'''

# Constructor in Inheritance
##class Father:					# Parent Class
##	def __init__(self):
##		self.money = 1000
##		print("Father Class Constructor")
##		
##	def show(self):
##		print("Father Class Instance Method")
##		
##		
##class Son(Father):				# Child Class
##	def disp(self):
##		print("Son Class Instance Method", self.money)
##
##s = Son()
##s.disp()
##print("Father Instance Variable:", s.money)
##s.show()

##
##class Parent(object):
##    def __init__(self,id,name):
##        self.id=2260
##        self.name=name
##        
##        print("I am From Parent Class Constructor and My Id is :{}\n Name is:{}".format(self.id,self.name))
##
##    def show(self):
##        print("Parent Class Instance Method")
##
##class Daughter(Parent):
##    
##    def display(self):
##        print("I am from child class",self.id,self.name)
##
##s=Daughter(22,"A")
##s.display()
##s.show()


'''Single Inheritance Constructor With Parameters'''

##Constructor with Parameter in Inheritance
##class Father:					# Parent Class
##	def __init__(self, m):
##		self.money = m
##		print("Father Class Constructor")
##		
##	def show(self):
##		print("Father Class Instance Method")
##		
##		
##class Son(Father):				# Child Class
##	def disp(self):
##		print("Son Class Instance Method:", self.money)
##
##s = Son(1000)
##s.disp()
##print("Father Instance Variable:", s.money)
##s.show()

##class Animal(object):
##    def __init__(self,name):
##        self.name=name
##        print("Father Class Constructor")
##
##    def show(self):
##        print("Father Class Instance Method")
##
##class Parrot(Animal):
##    def disp(self):
##        print("Son class Instance Method",self.name)
##s=Parrot("P")
##s.disp()
##s.show()
##        

'''Single Inheritance with Constructor Overriding'''
### Constructor Overriding
##class Father:					# Parent Class
##	def __init__(self):
##		self.money = 1000
##		print("Father Class Constructor")
##		
##	def show(self):
##		print("Father Class Instance Method")
##		
##		
##class Son(Father):				# Child Class
##	def __init__(self):
##		self.money = 5000
##		self.car = 'BMW'
##		print("Son Class Constructor")
##		
##	def disp(self):
##		print("Son Class Instance Method")
##
##s = Son()
##print(s.money)
##print(s.car)
##s.disp()
##s.show()

##class Manager(object):
##    def __init__(self,id,salary):
##        self.id=id
##        self.salary=1000
##        print("I am From Father class Constructor")
##
##    def show(self):
##        print("Father class Instance Method")
##
##class Employee(Manager):
##    def __init__(self,id,salary,name):
##        self.salary=5000
##        self.name=name
##        print("I am from Child class Constructor")
##
##    def disp(self):
##        print(" I am from child class Instance Method")
##
##e=Employee(22,5000,"R")
##e.disp()
##

'''Constructor Overriding with Parameter'''

##class Father:					
##	def __init__(self, m):
##		self.money = m
##		print("Father Class Constructor")
##		
##	def show(self):
##		print("Father Class Instance Method")
##		
##		
##class Son(Father):				
##	def __init__(self, r):
##		self.money = r
##		self.car = 'BMW'
##		print("Son Class Constructor")
##		
##	def disp(self):
##		print("Son Class Instance Method")
##
##s = Son(2000)
##print(s.money)
##print(s.car)
##s.disp()
##s.show()

'''# Constructor Overriding with Parameter'''

##class Father:					# Parent Class
##	def __init__(self, m):
##		self.money = m
##		print("Father Class Constructor")
##		
##	def show(self):
##		print("Father Class Instance Method")
##		
##		
##class Son(Father):				# Child Class
##	def __init__(self, r):
##		self.money = r
##		self.car = 'BMW'
##		print("Son Class Constructor")
##		
##	def disp(self):
##		print("Son Class Instance Method")
##
##s = Son(2000)
##print(s.money)
##print(s.car)
##s.disp()
##s.show()

'''# Constructor with Super Method'''

##class Father:					
##	def __init__(self):
##		print("Father Class Constructor")
##		
##	def show(self):
##		print("Father Class Instance Method")
##		
##		
##class Son(Father):				# Child Class
##	def __init__(self):
##		super().__init__()		# Calling Parent Class Constructor
##		print("Son Class Constructor")
##		
##		
##	def disp(self):
##		print("Son Class Instance Method")
##
##s = Son()
##s.disp()
##s.show()

'''# Constructor Parameter with Super Method'''

##class Father:					
##	def __init__(self, m):
##		self.money = m
##		print("Father Class Constructor")
##		
##	def show(self):
##		print("Father Class Instance Method:", self.money)
##		
##		
##class Son(Father):				# Child Class
##	def __init__(self, j, m):
##		super().__init__(m)		# Calling Parent Class Constructor
##		self.job = j
##		print("Son Class Constructor")
##		
##		
##	def disp(self):
##		print("Son Class Instance Method", self.job)
##
##s = Son('Python', 1000)
##s.disp()
##s.show()



    
    
