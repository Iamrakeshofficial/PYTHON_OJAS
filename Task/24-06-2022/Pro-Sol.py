##def totalmarks(sname,cls, **infor):
##    print("-"*40)
##    print("Student Name:{}".format(sname))
##    print("Student Studying in :{}".format(cls))
##    print("-"*40)
##    print("\tSubjects\tMarks")
##    print("-"*40)
##    totmarks=0
##    percentage=0
##    for subj,marks in infor.items():
##        print("\t{}\t\t{}".format(subj,marks))
##        totmarks=totmarks+marks
##        percentage=totmarks/5
##
##        if(percentage>=90):
##            print("Grade: O")
##        elif(percentage>=80&percentage<90):
##            print("Grade:E ")
##        elif(percentage>=70&percentage<80):
##            print("Grade: A")
##        elif(percentage>=60&percentage<70):
##            print("Grade: B")
##        elif(percentage>=50&percentage<60):
##            print("Grade: C")
##        elif(percentage>=40&percentage<50):
##            print("Grade: D")
##
##        else:
##            print("Grade: F")
##          
##    else:
##        print("-"*40)
##        print("\tTotal Marks={}".format(totmarks))
##        print("\tPercentage={}".format(percentage))
##
###main program
##totalmarks("Rakesh Kumar Sahoo","X",Eng=67,Tel=66,Sci=88,maths=99,soc=88)


sname=input("Enter the Student Name:")
sclass=input("Enter the student class Name:")

while(True):
    sub1=int(input("Enter Student's English Marks."))
    if (sub1>=0)and(sub1<=100):
        break

while(True):
    sub2=int(input("Enter Student's Odia Marks."))
    if (sub2>=0)and(sub2<=100):
        break

while(True):
    sub3=int(input("Enter Student's Science Marks."))
    if (sub3>=0)and(sub3<=100):
        break

while(True):
    sub4=int(input("Enter Student's Math Marks."))
    if (sub4>=0)and(sub4<=100):
        break

while(True):
    sub5=int(input("Enter Student's Social Marks."))
    if (sub5>=0)and(sub5<=100):
        break

totmarks=sub1+sub2+sub3+sub4+sub5
percentage=(totmarks/500)*100

if ((sub1<35)or(sub2<35)or(sub3<35)or(sub4<35)or(sub5<35)):
    grade="F"
    status="FAIL"

else:
    if ((percentage>=90) and(percentage<=100)):
        grade="O"
        status="PASS"
    elif((percentage>=80) and(percentage<=90)):
        grade="E"
        status="PASS"
    elif((percentage>=70) and(percentage<=80)):
        grade="A"
        status="PASS"

    elif((percentage>=60) and(percentage<=70)):
        grade="B"
        status="PASS"

    elif((percentage>=50) and(percentage<=60)):
        grade="C"
        status="PASS"
    elif((percentage>=40) and(percentage<=50)):
        grade="D"
        status="PASS"

    else:
        grade="F"

print("="*40)
print("\t STUDENT MARKS  REPORT")
print("="*40)
print("\tStudent Name--{}".format(sname))
print("\tStudent Class--{}".format(sclass))
print("-"*40)
print("\tSubjects\tMarks")
print("-"*40)
print("\tEnglish\t{}".format(sub1))
print("\tOdia\t{}".format(sub2))
print("\tScience\t{}".format(sub3))
print("\tMaths \t{}".format(sub4))
print("\tSocial\t{}".format(sub5))
print("="*40)
print("\tTotal Marks=\t{}".format(totmarks))
print("\tPercentage=\t{}".format(percentage))
print("\tGrade=\t{}".format(grade))
print("\tStatus=\t{}".format(status))

