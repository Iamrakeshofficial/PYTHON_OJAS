"""Write Program  to calculate area of different Figures such as circle,rectangle and square by 
using method overriding for implementing polymorphism."""

class Circle:
    
    def area(self, r): # Original Method--One Form
        self.ac=3.14*r**2
        print("Area of Circle={}".format(self.ac))
class Square(Circle):
    def area(self, s): # Overridden Method
        self.sa=s**2
        print("Area of Square={}".format(self.sa))

        print("-"*50)
        super().area(float(input("Enter Radious:")))
class Rect(Square):
    def area(self,l,b): # Overridden Method
        self.ar=l*b
        print("Area of Rect={}".format(self.ar))
        print("-"*50)
        super().area(float(input("Enter Side:")))
#main program
l,b=float(input("Enter Length:")), float(input("Enter Breadth:"))
ro=Rect()
ro.area(l,b)
