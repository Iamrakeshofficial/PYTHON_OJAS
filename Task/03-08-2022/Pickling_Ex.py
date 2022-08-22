'''1). Consider a binary file “data.dat” which stores the record of “Hotel”
in the form of list containing Room_no, Price, Room_type.
Do the following task in a file

Write a function addrec() to add a record in a file.
Write a function disp() to display all the records from the file.
Write a function specific_disp(room_no) which takes room number as argument and display its details.
Write a function mod(room_no) which takes room number as argument and modify it’s details.
Write a function del(room_no) which takes room number as argument and delete it’s record from file “data.dat”'''

##import pickle
##
##def addrec():
##     L=[ ]
##     f=open("data","ab")
##     rn = int(input("Enter Room Number:"))
##     pr = int(input("Enter the price of room:"))
##     rt = input("Enter the type of room:")
##     L  = [rn, pr, rt]
##     pickle.dump(L, f)
##     print("Record added in the file")
##     f.close()
##     
##addrec() 

'''2). Write a menu driven program which shows all operations on Binary File
Add Record
Display All Record
Display Specific Record
Modify Record
Delete Record
Use “data.dat” file which stores the record of “Hotel” in the form of list containing Room_no, Price, Room_type.'''

##import pickle
##import os
##def main_menu():
##    print("1. Add a new record")
##    print("2. Display all record")
##    print("3. Display Specific record")
##    print("4. Modify a record")
##    print("5. Delete a record")
##    print("6. Exit")
##    ch = int(input("Enter your choice:"))
##    if ch==1:
##        addrec()
##    elif ch==2:
##        disp()
##    elif ch==3:
##        
##        specific_rec()
##    elif ch==4:
##        mod()
##    elif ch==5:
##        del()
##    elif ch==6:
##        print("Bye")
##    else:
##        print("Invalid Choice.")

'''3). Write a function dispname() in Python which will display only names of all the students from file “school.dat”.
Structure stored in “school.dat” is in the form of list containing information like,
[rollno, name, class, percentage]'''

##def dispname():
##  f=open("studen.txt","rb")
##  try:
##    while True:
##      d=pickle.load(f)
##      print("Name        : ", d[1],"\n")
##  except:
##    f.close()
##dispname()



'''4).Write a function disp12() in Python which will display records of class 12th students from file “school.dat”.
Structure stored in “school.dat” is in the form of list containing information like [rollno, name, class, percentage]'''



''''5).Write a function search(name) in Python which will display record of a student from file “school.dat” whose name is passed as an argument.
Structure stored in “school.dat” is in the form of list containing information like [rollno, name, class, percentage]'''

 '''6).Write a function rem() in Python which will delete the records of students from file “school.dat” who scored less than 30 percent marks.
 Structure of “school.dat” is in the form of list containing information like [rollno, name, class, percentage].'''
