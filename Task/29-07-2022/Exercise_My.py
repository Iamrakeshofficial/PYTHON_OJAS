'''1. Write a Python program to create a file where all letters of English alphabet are
listed by specified number of letters on each line.'''
##f=open("Exercise.txt",mode="w")
##f.write(

'''2.Write a Python program to combine each line from first file with the corresponding line in second file.'''
f1=open("Essay.txt"


'''3.Write a Python class named Student with two attributes student_id, student_name.
Add a new attribute student_class. Create a function to display the entire 
attribute and their values in Student class.'''

##class Student(object):
##    company="Ojas"
##    def __init__(self,id,name):
##        self.id=id
##        self.name=name
##
##    def student_Details(self):
##        print("The Student Id is {} and Name is {}.".format(self.id,self.name))
##        print("The Company Is {}.".format(self.company))
##
##s=Student(22069,"Rakesh")
##s.student_Details()
        
        

'''4. Write a Python program to convert an array to an ordinary list with the same items. 
Original array: array('i', [1, 3, 5, 3, 7, 1, 9, 3])
Convert the said array to an ordinary list with the same items:
[1, 3, 5, 3, 7, 1, 9, 3]'''


##from array import*
##n=array('i', [1, 3, 5, 3, 7, 1, 9, 3])
##print(f"The Original Array List:",n)
##
##l1=n.tolist()
##print(f"The Ordinary List:",l1)

'''5. Write a Python program to print yestarday date,day before yestarday and next 5 days starting from today.'''
##
##from datetime import*
##
##today = date.today()
##print("Today is: ", today)
##print("Next Five Days From Today Are:")
##for i in range(0,5):
##    print(today+timedelta(days=i))
##
##yesterday = today - timedelta(days = 1)
##print("Yesterday was: ", yesterday)
##
##dayafterYesterday=today-timedelta(days=2)
##print(f"Day After Yesterday Was:",dayafterYesterday)

