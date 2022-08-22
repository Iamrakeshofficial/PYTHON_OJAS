''' Multiple Inheritance Without Constructor'''

##class Father:
##	def __init__(self):
##		print("Father Class Constructor")
##	def showF(self):
##		print("Father Class Method")
##		
##class Mother:
##	def __init__(self):
##		print("Mother Class Constructor")
##	def showM(self):
##		print("Mother Class Method")
##		
##class Son(Father, Mother):
##	def __init__(self):
##		print("Son Class Constructor")
##	def showS(self):
##		print("Son Class Method")
##		
##		
##s = Son()
##s.showF()
##s.showM()
##s.showS()

''' Multiple Inheritance with constructor'''

##class Father:
##	def __init__(self):
##		print("Father Class Constructor")
##	def showF(self):
##		print("Father Class Method")
##		
##class Mother:
##	def __init__(self):
##		print("Mother Class Constructor")
##	def showM(self):
##		print("Mother Class Method")
##		
##class Son(Father, Mother):
##	def __init__(self):
##		super().__init__()					# Calling Parent Class Constructor
##		print("Son Class Constructor")
##	def showS(self):
##		print("Son Class Method")
##		
##		
##s = Son()
##s.showF()
##s.showM()
##s.showS()

''' Multiple Inheritance'''
##class Father:
##	def __init__(self):
##		super().__init__()					# Calling Parent Class Constructor
##		print("Father Class Constructor")
##	def showF(self):
##		print("Father Class Method")
##		
##class Mother:
##	def __init__(self):
##		super().__init__()					# Calling Parent Class Constructor
##		print("Mother Class Constructor")
##	def showM(self):
##		print("Mother Class Method")
##		
##class Son(Father, Mother):
##	def __init__(self):
##		super().__init__()					# Calling Parent Class Constructor
##		print("Son Class Constructor")
##	def showS(self):
##		print("Son Class Method")
##		
##		
##s = Son()
##s.showF()
##s.showM()
##s.showS()

''' 3. multiple inheritance with constructor with parameters'''


##class Father:
##    def __init__(self,age):
##        self.age=age
##    def Driving(self):
##        print("Father age is")
##class Mother:
##    def __init__(self,weight):
##        self.weight=weight
##    def Cooking(self):
##        print("Mother Enjoys Cooking")
##class Child(Mother,Father):
##    def Playing(self):
##        print("the children wight is",self.weight)
##c = Child(65)
##c.Driving()
##c.Cooking()
##c.Playing()
##

''' 4. multiple inheritance with constructor overriding'''

##class Father:
##    def __init__(self):
##        self.age='56'
##    def Driving(self):
##        print("Father age is",self.age)
##class Mother:
##    def __init__(self):
##        self.age='45'
##    def Cooking(self):
##        print("Mother age is",self.age)
##class Child(Mother,Father):
##    def __init__(self):
##        self.age='20'
##    def Playing(self):
##        print("the children age is is",self.age)
##c = Child()
##c.Driving()
##c.Cooking()
##c.Playing()

''' 5. multiple inheritance with constructor ovr riding parameters'''

##class Father:
##    def __init__(self,m):
##        self.age=m
##    def Driving(self):
##        print("Father age is")
##class Mother:
##    def __init__(self,n):
##        self.age=n
##    def Cooking(self):
##        print("Mother age is")
##class Child(Mother,Father):
##    def __init__(self,a):
##        self.age=a
##        self.car='benz'
##    def Playing(self):
##        print("the children age is is",self.age)
##        print("the car is ",self.car)
##c = Child(26)
##c.Driving()
##c.Cooking()
##c.Playing()
##
''' 6. multiple inheritance with constructor super method'''

##class Father:
##    def __init__(self):
##        print("the father class constructor")
##    def Driving(self):
##        print("Father method is")
##class Mother:
##    def __init__(self):
##        print("the mother class constrotur")
##    def Cooking(self):
##        print(" it is Mother method")
##class Child(Father,Mother):
##    def __init__(self):
##        
##        super().__init__()
##    def Playing(self):
##        print("the children  method is")
##        
##c = Child()
##c.Driving()
##c.Cooking()
##c.Playing()



''' 7. multiple inheritance with constructor super
method wirh parameters'''

class Father:
    def __init__(self,m):
        self.money=m
        print("the father class constructor")
    def Driving(self):
        print("Father money is",self.money)
class Mother:
    def __init__(self,n):
        self.name=n
        print("the mother class constrotur")
    def Cooking(self):
        print(" it is Mother name is",self.name)
class Child(Father,Mother):
    def __init__(self,m,k):
        self.fees=k
        
        
        super().__init__(m)
    def Playing(self):
        print("the children  methodis",self.fees)
        
c = Child(2500,1200)
c.Driving()
c.Cooking()
c.Playing()








