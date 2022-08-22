'''1.Write a Program to create a class by name Students, and initialize attributes like name, age, and grade while creating an object.''' 

##class Student:
##    def __init__(self,name,age,grade):
##        self.name=name
##        self.age=age
##        self.grade=grade
##
##    def details(self):
##        print("The Student name is :{},age is :{}and grade is :{}".format(self.name,self.age,self.grade))
##
##a=Student("Rakesh",23,"A")
##a.details()             
##

'''2.Write a Program to create an empty valid class by name Students, with no properties '''

##class Student:
##    pass
##
##ob=Student()
##print(ob)
##    

'''3.Write a program that prints the class name using its object.'''

##class Student:
##    pass
##
##ob=Student()
##print(type(ob))



'''4.Write a program, to create a child class Teacher that will inherit the properties of Parent class Staff'''

##class Staff(object):
##    def __init__(self,name,department):
##        self.name=name
##        self.department=department
##
##    def staffDetails(self):
##        print("The Staff Details: Name -{},Department - {}.".format(self.name,self.department))
##
##class Teacher(Staff):
##    def __init__(self,name,department,salary):
##        self.salary=salary
##
##        super(). __init__(name,department)
##
##
##a=Teacher("Rakesh","CSE",20000)
##a.staffDetails()

        

'''5.Create a Vehicle class without any variables and methods '''

##class Vehicle:
##    pass
##ob=Vehicle()

'''6.Create a child class Bus that will inherit all of the variables and methods of the Vehicle class '''
##
##class Vehicle(object):
##    def __init__(self,company,owner,price):
##        self.company=company
##        self.owner=owner
##        self.price=price
##
##
##    def details(self):
##        print("Company is :{}".format(self.company))
##        print("Owner is :{}".format(self.owner))
##        print("Price is :{}".format(self.price))
##
##
##class Bus(Vehicle):
##    def __init__(self,company,owner,price,color):
##        self.color=color
##
##
##        Vehicle.__init__(self,company,owner,price)
##
##obb=Bus("Volvo","Rakesh Kumar",15000000,"Blue")
##obb.details()

''' 7.Define a property that must have the same value for every class instance (object) '''

##class Employee(object):
##    org="Ojas"
##    def __init__(self,name,id,Department):
##        self.name=name
##        self.id=id
##        self.Department=Department
##
##    def details(self):
##        print("Name is:",self.name)
##        print("Id is :",self.id)
##        print("Department is:",self.Department)
##
##
##class Student(Employee):
##    pass
##
##class abc(Employee):
##    pass
##
##        
##ob=Student("Rakesh",22069,"Python")
##ob.details()


'''8. Check type of an object '''

##class Team:
##    def __init__(self,name,gender):
##        self.name=name
##        self.gender=gender
##
##    def details(self):
##        print("The Team Details: Name Is {},Gender is {}.".format(self.name,self.gender))
##
##ob=Team("Rakesh","Male")
##ob.details()
##print(type(ob))

'''9.Write a Python program that checks if one class is a subclass of another?'''


##class Teacher(object):
##    pass
##class Student(Teacher):
##    pass
##
##
##print(issubclass(Student,Teacher))
##




'''10.Determine if School_bus is also an instance of the Vehicle class'''

##class Vehicle(object):
##    def __init__(self,company,owner,price):
##        self.company=company
##        self.owner=owner
##        self.price=price
##
##
##    def details(self):
##        print("Company is :{}".format(self.company))
##        print("Owner is :{}".format(self.owner))
##        print("Price is :{}".format(self.price))
##
##class School_bus(Vehicle):
##    pass
##
##
##ob=School_bus("Volvo","Tarkesh",2000000)
##ob.details()
##print(isinstance(ob,Vehicle))


##
##class Vehicle:
##    pass
##
##class School_bus(Vehicle):
##    pass
##ob=School_bus()
##print(isinstance(ob,Vehicle))
##

            
        

 
