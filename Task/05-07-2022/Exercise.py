'''1.write a python program using oops concept finding prime number or not.'''

##class Prime:   
##    def isPrime(self,number):
##        self.number=number
##        if self.number>1:
##            for i in range(2,self.number):
##                if (self.number%i)==0:
##                    print(self.number,"is not a Prime Number.")
##                    break
##            else:
##                print(self.number," is a Prime Number.")
##                   
##        else:
##            print(self.number," is Not a Prime Number.")
##
##    
##
##
##ob=Prime()
##ob.isPrime(int(input("Enter a Number:")))






'''2.write a program on instance method, static method, class method using some examples.'''

##class Student:
##    
##    org ="Ojas"
##    def __init__(self, name, age):
##        # instance variables
##        self.name = name
##        self.age = age
##
##    # instance variables
##    def show(self):
##        print(self.name, self.age, Student.org)
##
##    @classmethod
##    def change_School(cls, name):
##        cls.org = name
##
##    @staticmethod
##    def find_notes(subject_name):
##        return ['Hindi', 'English', 'Odiya']




'''3.write a program on single inheritance.'''

##class Animal:
##    def speak(self):
##        print("The dog is Speaking")
##
##class Dog(Animal):
##    def bark(self):
##        print("The Dog is Barking")
##
##b=Dog()
##b.speak()
##b.bark()
##        



'''4.write a python program using oops concepts find a fibonacci series.'''

##class fibonacci:
##    def __init__(self,num):
##        self.num=num
##
##    def printing(self):
##        a=0
##        b=1
##        for i in range(self.num):
##            c=a+b
##            a=b
##            b=c
##            print(c)
##
##result=fibonacci(int(input("Enter any Number:")))
##result.printing()




'''5.write a python program using oops concepts find armstrong number.'''
##class Check:
##    def __init__(self,n):
##        self.n=n
##    def Armstrong(self):
##        temp=self.n
##        sum1=0
##        while temp !=0:
##            r=temp%10
##            sum1+=r**3
##            temp//=10
##        if self.n==sum1:
##            print(self.n,"it is Armstrong number")
##        else:
##            print(self.n,"it is not Armstrong number")
##n=153
##obj=Check(n)
##obj.Armstrong()


