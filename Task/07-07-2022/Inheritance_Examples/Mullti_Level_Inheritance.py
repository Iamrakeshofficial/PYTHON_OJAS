''' Multi-level Inheritance Without Constructor'''
##class Father:
##	
##	def showF(self):
##		print("I am from Father Class Method")
##		
##class Son(Father):
##	
##	def showS(self):
##		print("I am from Son Class Method")
##		
##class GrandSon(Son):
##	
##	def showG(self):
##		print("I am from GrandSon Class Method")
##		
##g = GrandSon()
##g.showF()
##g.showS()
##g.showG()

'''Multi-level Inheritance With Constructor'''

##class Father:
##	def __init__(self):
##		print("I am from Father Class Constructor")
##	def showF(self):
##		print("I am from Father Class Method")
##		
##class Son(Father):
##	def __init__(self):
##		
##		print("I am from Son Class Constructor")
##	def showS(self):
##		print("I am from Son Class Method")
##		
##class GrandSon(Son):
##	def __init__(self):
##		
##		print("I am from GrandSon Class Constructor")
##	def showG(self):
##		print("I am from GrandSon Class Method")
##		
##g = GrandSon()
##g.showG()
##


''' Multi-level Inheritance With Constructor with super'''
##
##class Father:
##	def __init__(self):
##		print("I am from Father Class Constructor")
##	def showF(self):
##		print("I am from Father Class Method")
##		
##class Son(Father):
##	def __init__(self):
##		super().__init__()
##		print("I am from Son Class Constructor")
##	def showS(self):
##		print("I am from Son Class Method")
##		
##class GrandSon(Son):
##	def __init__(self):
##		super().__init__()
##		print("I am from GrandSon Class Constructor")
##	def showG(self):
##		print("I am from GrandSon Class Method")
##		
##g = Son()
##g.showF()

''' Multi-level Inheritance With Constructor with parameter'''

##class Parent:
##   def __init__(self,name):
##     self.name = name

##   def getName(self):
##     return self.name
##class Child(Parent):
##   def __init__(self,name,age):
##     Parent.__init__(self,name)
##     self.age = age

##   def getAge(self):
##     return self.age
##class Grandchild(Child):
##   def __init__(self,name,age,location):
##     Child.__init__(self,name,age)
##     self.location=location

##   def getLocation(self):
##     return self.location
##gc = Grandchild("Srinivas",24,"Hyderabad")
##print(gc.getName(), gc.getAge(), gc.getLocation())

'''Multilevel inheritance with constructor overriding'''

##class Car(object):
##
##    def __init__(self):
##        print("You just created the car instance")
##
##    def drive(self):
##        print("Car started...")
##
##    def stop(self):
##        print("Car stopped")
##
##class BMW(Car):
##
##    def __init__(self):
##        super().__init__()
##        print("You just created the BMW instance")
##
##    def drive(self):
##        super(Car, self).drive()
##        print("You are driving a BMW, Enjoy...")
##
##    def headsup_display(self):
##        print("This is a unique feature")
##
##class BMW320(BMW):
##
##    def __init__(self):
##        super().__init__()
##        print("You created BMW320 instance")
##
##    def drive(self):
##        super(BMW, self).drive()
##        print("You are enjoying BMW 320")
##
##
##c = Car()
##c.drive()
##c.stop()
##b = BMW()
##b.drive()
##b.stop()
##b.headsup_display()
##b320=BMW320()
##b320.drive()

'''Multi-levelinheritance with constructor overriding with parameter'''

##class xyz(object):
##        def__init__(self):
##                
##                print("hey, I am initialized , xyz")
##        def sub_xyz(self,b):
##                self.b=b
##                print("Printing from class xyz:",self.b)
##class xyz1(xyz):
##        def __init__(self):
##                print("hey, I am initialized, xyz1")
##                super().__init__()
##        def sub_xyz(self,b):
##                print("Printing from class xyz1:", self.b)
##                super().sub_xyz(b+1)
##class xyz2(xyz1):
##        def __init__(self):
##                print("hey, I am initialized, xyz2")
##                super().__init__()
##        def sub_xyz(self,b):
##                print("Printing from class xyz2:",self.b)
##                super().sub_xyz(self.b+1)
##c=xyz2()
##c.sub_xyz()

'''Multi-levelinheritance with constructor overriding with parameter'''

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
##class GrandSon(Son):
##        
##        def __init__(self, j):
##                self.money = j
##                self.car = 'Audi'
##                print("GrandSon Class Constructor")
##		
##        def disp(self):
##                print("GrandSon Class Instance Method")
##
##        
##
##s = GrandSon(2000)
##print(s.money)
##print(s.car)
##s.disp()
##s.show()


'''Multi-levelinheritance inheritance with constructor with super and parameter'''


class Father:					# Parent Class
	def __init__(self, m):
		self.money = m
		print("Father Class Constructor")
		
	def show(self):
		print("Father Class Instance Method:", self.money)
		
		
class Son(Father):				# Child Class
	def __init__(self, j, m):
		super().__init__(m)		# Calling Parent Class Constructor
		self.job = j
		print("Son Class Constructor")
		
		
	def disp(self):
		print("Son Class Instance Method", self.job)

class GrandSon(Son):
        def __init__(self, j, m,n):
                super().__init__(m,n)		# Calling Son Class Constructor
                self.name=n
                print("GrandSon Class Constructor")
		
		
        def disp(self):
                print("GrandSon Class Instance Method", self.name)

s = GrandSon('Python', 1000,"Rakesh")
s.disp()
s.show()

'''inheritance without constructor'''
'''inheritance with constructor'''
'''inheritance with parameter and constructor'''
'''inheritance with constructor overriding'''
'''Multi-levelinheritance with constructor overriding with parameter'''
'''inheritance with constructor with super'''
'''Multi-levelinheritance inheritance with constructor with super and parameter'''




