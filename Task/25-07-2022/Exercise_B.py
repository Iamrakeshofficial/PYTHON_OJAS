"""1) wap to create class and create two objects from that class and add those two objects
using _add_ (operator overloading)."""

##class Employee(object):
##    def __init__(self,name,salary):
##        self.name=name
##        self.salary=salary
##
##    def emp_Details(self):
##        print("The Name of the Employee is {} and Salary is {}".format(self.name,self.salary))
##
##    def __add__(self,other):
##        return self.salary+other.salary
##
##e1=Employee("Bhagavaan",12000)
##e2=Employee("Tarak",13000)
##print(e1+e2)

"""2) wap to create a generator by using send method."""

##def func():
##    while True:
##        val = yield
##        yield val*10
##
##
##g=func()
##next(g)
##print(g.send(1))
##next(g)
##print(g.send(10))
##next(g)
##print(g.send(100))

"""3) wap to create the generator comprehension."""

##g = (x for x in range(10))
##print(sum(g))

"""4) print a function n number of times using decorator.""" 


"""5) write a python program to check the how many instance variables are there in a class."""


##class Employee(object):
##    def __init__(self,name,id):
##        self.name=name
##        self.id=id
##        
##    def details(self):
##        print("The Name Of the Employee is {} and Id is {}".format(self.name,self.id))
##
##
##
##e=Employee("Rakesh",22069)
##e.details()
##print("The Instance Variable in The Given class are",e.__dict__)
##for key,value in e.__dict__.items():
##    print(key,value)
##        
