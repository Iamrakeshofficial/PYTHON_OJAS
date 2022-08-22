""" Method Overriding"""


##class Add:
##	def result(self, a, b):
##		print('Addition:', a+b)
##		
##class Multi(Add):
##	def result(self, a, b):
##		print('Multiplication:', a*b)
##		
##m = Multi()
##m.result(10, 20)
##
##m = Add()
##m.result(10, 20)


##class Teacher(object):
##        def __init__(self,id,name):
##                self.id=id
##                self.name=name
##        def disp(self):
##                
##                print("My name is {} and Id is {}".format(self.name,self.id))
##
##
##
##class Student(Teacher):
##        def __init__(self,id,name):
##                 super().__init__(id,name)
##                
##        def disp(self):
##               
##                print("My Id is {} and Name is {}".format(self.id,self.name))
##
##
##
##
##s=Student(22,"Rakesh")
##s.disp()
##
##t=Teacher("Rakesh",22069)
##t.disp()



""" Method Overriding"""

##class Add:
##	def result(self, a, b):
##		print('Addition:', a+b)
##		
##class Multi(Add):
##	def result(self, a, b):
##		super().result(10, 20)				
##		print('Multiplication:', a*b)
##		
##m = Multi()
##m.result(10, 20)


##class Sub(object):
##        def result(self,x,y):
##                print("Sub is:",x-y)
##
##class Div(Sub):
##        def result(self,x,y):
##                super().result(x,y)
##                print("Division is:",x/y)
##
##d=Div()
##d.result(20,30)

















                




