""" Button"""
##from tkinter import *
##window=Tk()
##btn=Button(window, text="Submit", fg='blue')
##btn.place(x=80, y=100)
"""Label"""
##from tkinter import *
##window=Tk()
##lbl=Label(window, text="Send", fg='red', font=("Helvetica", 16))
##lbl.place(x=60, y=50)

"""Entry"""

##from tkinter import *
##window=Tk()
##btn=Button(window, text="Submit", fg='blue')
##btn.place(x=80, y=100)
##lbl=Label(window, text="Label", fg='red', font=("Helvetica", 16))
##lbl.place(x=60, y=50)
##txtfld=Entry(window, text="Enter Numbers ", bd=5)
##txtfld.place(x=80, y=150)
##window.title('Python')
##window.geometry("300x200+10+10")
##window.mainloop()
"""Title"""
##import tkinter
##top=tkinter.Tk()
##top.title("Hello World")
##top.geometry("300x200+10+10")
##top.mainloop()
"""pack() """

##from tkinter import *
##top=Tk()
##top.title("Hello World")
##B1 = Button(top, text ="OK")
##L1=Label(top, text="Enter name", fg='blue')
##T1=Entry(top, text="This is Entry Widget", fg='red', bd=3)
##L1.pack(fill=X, padx=10)
##T1.pack(fill=X, padx=10)
##B1.pack(fill=X, padx=10)
##top.mainloop()
"""grid()"""

##from  tkinter import *
##import random
##top = Tk()
##for r in range(2):
##  for c in range(2):
##     Label(top, text='Label '+str(r+1)).grid(row=r, column=0)
##     Entry(top, bd=3).grid(row=r, column=1)
##top.mainloop()
"""place()"""
##from tkinter import *
##top = Tk()
##L1 = Label(top, text = "price")
##L1.place(x = 10,y = 10)
##E1 = Entry(top, bd = 3)
##E1.place(x = 60,y = 10)
##L2 = Label(top,text = "quantity")
##L2.place(x = 10,y = 50)
##E2 = Entry(top,bd = 3)
##E2.place(x = 60,y = 50)
##L3 = Label(top,text = "Amount")
##L3.place(x = 10,y = 150)
##E3 = Entry(top,bd = 3)
##E3.place(x = 60,y = 150)
##B = Button(top, text = "Calculate")
##B.place(x = 100, y = 100)
##top.geometry("250x200+10+10")
##top.mainloop()
"""bind() function: """

##from tkinter import *
##def hello(event):
##   print("Hello World")
##top=Tk()
##B = Button(top, text='Say Hello')
##B.bind('<Button-1>', hello)
##B.pack()
##top.mainloop()
