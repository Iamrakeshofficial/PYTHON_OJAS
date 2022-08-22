'''Problem Statement: Write a program to build a simple Student Management System using Python which can perform the following operations in oops concepts 

1.Accept
2.Display
3.Search
4.Delete
5.Update'''

class Student:
    def __init__(self, name, roll, s1, s2):
        self.name = name
        self.roll = roll
        self.s1 = s1
        self.s2 = s2
    
    def accept(self, Name, Roll, score1, score2):
        obj = Student(Name, Roll, score1, score2)
        ls.append(obj)
   
    def display(self, obj):
        print("Name : ", obj.name)
        print("RollNo : ", obj.roll)
        print("Score1 : ", obj.s1)
        print("Score2 : ", obj.s2)
        print("\n")
    
    def search(self, rn):
        for i in range(ls.__len__()):
            if (ls[i].roll == rn):
                return i
            
    def delete(self, rn):
        i = obj1.search(rn)
        del ls[i]
    def update(self, rn, No):
        i = obj1.search(rn)
        rolln = No
        ls[i].roll = rolln;
ls = []

obj1 = Student('', 0, 0, 0)
print("\nOperations used, ")
print("\n1.Accept Student details\n"
      "2.Display Student Details\n" 
       "3.Search Details of a Student\n"
        "4.Delete Details of Student" 
      "\n5.Update Student Details\n6.Exit")
obj1.accept("A", 1, 100, 100)
obj1.accept("B", 2, 90, 90)
obj1.accept("C", 3, 80, 80)

print("\n")
print("\nList of Students\n")

for i in range(ls.__len__()):
    obj1.display(ls[i])
    
print("\n Student Found, ")
s = obj1.search(2)
obj1.display(ls[s])
obj1.delete(2)
print(ls.__len__())
print("List after deletion")

for i in range(ls.__len__()):
    obj1.display(ls[i])
obj1.update(3, 2)
print(ls.__len__())
print("List after updation")


for i in range(ls.__len__()):
    obj1.display(ls[i])
print("Thank You !")
