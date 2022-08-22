'''1.Create a class Teacher with name, age, and salary attributes,
where salary must be a private attribute that cannot be accessed outside the class.'''

##class Teacher:
##    def __init__(self,name,age,salary):
##        self.name=name
##        self.age=age
##        self.__salary=salary
##
##    def show_Details(self):
##        print("Name -{}\n Age -{}\nSalary -{}".format(self.name,self.age,self.__salary))
##
##ob=Teacher("Rakesh",23,15000)
##ob.show_Details()
##
##print(ob.name)
##print(ob.__salary)
        

'''2.Write a Python class Square, and define two methods that return the square area and perimeter.'''

##class Square:
##    def __init__(self,side):
##        self.side=side
##
##    def area(self):
##        print("The area of Square is:{}".format(self.side*self.side))
##
##    def perimeter(self):
##        print("The perimeter of Square is:{}".format(4*self.side))
##
##s=Square(20)
##s.area()
##s.perimeter()


'''3.How to copy all properties of an object to another object in Python?'''

##class MyClass(object):
##    def __init__(self):
##        super(MyClass, self).__init__()
##        self.f = 10
##        self.b = 20
## 
## 
##obj1 = MyClass()
##obj2 = MyClass()
## 
##obj1.f = 25
##obj2.__dict__.update(obj1.__dict__)
## 
##print(obj1.f)
##print(obj2.f)



'''4.Create a method called Factorial() which allows to calculate the factorial of an integer.
Test the method by instantiating the class.'''

##class Factorial:
##    def __init__(self,n):
##        self.n=n
##    def fact(self):
##        if self.n==0:
##            return 1
##        else:
##            return self.n* self.fact(self.n -1)
##
##f=Factorial(5)
##f.fact()

##class Factorial:
##
##    def fact(self,n):
##        if n == 0:
##            return 1 
##        else:
##            return n * self.fact(n - 1)
##
##f = Factorial()
##print(f.fact(4))

'''5.Create a student object via an instantiation on the Student class and then test the displayStudent method.'''

##class Student:
##    org="Ojas"
##    def __init__(self,name,id,gender):
##        self.id=id
##        self.name=name
##        self.gender=gender
##    def student_Details(self):
##        print("The Student Deatails are:\n Name:{}\nId:{}\nGender:{}\nOrg:{}".format(self.name,self.id,self.gender,self.org))
##
##s=Student("Rakesh",22069,"Male")
##s.student_Details()



        



