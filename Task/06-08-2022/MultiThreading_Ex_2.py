'''Creating a Thread by creating a Child class to Thread.'''
##from threading import*

##class Myclass(Thread):
##    def __init__(self):
##        Thread.__init__(self)
##        print("Child Thread Constructor")
##    def run(self):
##        print("Hello Guys")
##        
##m=Myclass()
##m.start()
##print("Main Thread")

##class Employee(Thread):
##    def __init__(self,name,age):
##        Thread.__init__(self)
##        
##        self.age=age
##        self.name=name
##        
##
##    def run(self):
##        print(f"My Name Is {self.name} and Age is {self.age}")
##
##
##e=Employee("Rakesh",23)
##e.start()
##print("MAin Thread")
##

''' Single Tasking Using Thread '''

##from threading import*

##class Myclass:
##    def solution(self):
##        self.task1()
##        self.task2()
##        self.task3()
##
##
##
##    def task1(self):
##        print("1st Task Completed.")
##
##
##    def task2(self):
##        print("2nd Task Completed.")
##
##    def task3(self):
##        print("3rd Task Completed.")
##
##
##
##m=Myclass()
##
##t=Thread(target=m.solution)
##t.start()


##class Student:
##    def __init__(self,name,id,cls):
##        self.name=name
##        self.id=id
##        self.cls=cls
##        self.half()
##        self.details()
##
##    def display(self):
##        print(f'''The Student Name is {self.name},
##                  Id is {self.id} and Class is {self.cls}''')
##
##
##    def half(self):
##        print("The Student Name is:",self.name)
##
##    def details(self):
##        print("The Student Name is {} and Id is {} ".format(self.name,self.id)) 
##        
##
##s=Student("Rakesh",22069,"IX")
##t=Thread(target=s.display)
##t.start()

''' Multitasking Using  Multithread'''

##from threading import*
##
##class Restaurant:
##    def __init__(self,t):
##        self.t=t
##
##
##    def food(self):
##        for i in range(1,6):
##            print(self.t,i)
##
##
##r=Restaurant("Take Order from Customer:")
##r1=Restaurant("Serve Order to Customer:")
##
##t1=Thread(target=r.food)
##t2=Thread(target=r1.food)
##
##t1.start()
##t2.start()

'''Multitasking  Using MultiThread in a Single Method '''

##from threading import*

##class Train:
##
##    def __init__(self,av_seat):
##        self.av_seat=av_seat
##       
##
##    def reserve(self,need_seat):
##        print("Available Seat:",self.av_seat)
##
##        if(self.av_seat>=need_seat):
##            name=current_thread().name
##            print("{} seat is reserved for {}".format(self.av_seat,name))
##            self.av_seat -=need_seat
##
##        else:
##            print("Sorry! All Seats are reserved")
##
##obj=Train(1)
##
##t1=Thread(target=obj.reserve,args=(1,),name="Rakesh")
##t2=Thread(target=obj.reserve,args=(1,),name="liza")
##
##t1.start()
##t2.start()


##class Bus:
##    def __init__(self,tkt):
##
##        self.tkt=tkt
##
##
##    def booking(self,r_tkt):
##        print("Avaialable Ticket:",self.tkt)
##
##        if(self.tkt>=r_tkt):
##            name=current_thread().name
##            print("{}  ticket is  booked by {}".format(self.tkt,name))
##            self.tkt -= r_tkt
##
##        else:
##            print("Sorry! All Tickets are Booked,")
##
##b=Bus(1)
##
##t1=Thread(target=b.booking,args=(1,),name="Tarak")
##t2=Thread(target=b.booking,args=(1,),name="Vaddepa")
##
##t1.start()
##t2.start()


'''Lock'''

##from threading import*
##
##class Bus:
##    def __init__(self,tkt):
##
##        self.tkt=tkt
##        self.l=Lock()
##
##
##    def booking(self,r_tkt):
##        self.l.acquire()
##        print("Avaialable Ticket:",self.tkt)
##
##        if(self.tkt>=r_tkt):
##            name=current_thread().name
##            print("{}  ticket is  booked by {}".format(r_tkt,name))
##            self.tkt -= r_tkt
##
##        else:
##            print("Sorry! All Tickets are Booked,")
##        self.l.release()
##
##b=Bus(2)
##
##t1=Thread(target=b.booking,args=(1,),name="Tarak")
##t2=Thread(target=b.booking,args=(1,),name="Vaddepa")
##t3=Thread(target=b.booking,args=(1,),name="Bhagavaan")
##
##t1.start()
##t2.start()
##t3.start()
##t1.join()
##t2.join()
##t3.join()
##print("MAin Thread")



'''RLock'''

##from threading import*
##
##class Bus:
##    def __init__(self,tkt):
##
##        self.tkt=tkt
##        self.l=RLock()
##        print(self.l)
##
##
##    def booking(self,r_tkt):
##        self.l.acquire()
##        self.l.acquire()
##        print("Avaialable Ticket:",self.tkt)
##
##        if(self.tkt>=r_tkt):
##            name=current_thread().name
##            print("{}  ticket is  booked by {}".format(r_tkt,name))
##            self.tkt -= r_tkt
##
##        else:
##            print("Sorry! All Tickets are Booked,")
##        self.l.release()
##        self.l.release()
##
##b=Bus(2)
##
##t1=Thread(target=b.booking,args=(1,),name="Tarak")
##t2=Thread(target=b.booking,args=(1,),name="Vaddepa")
##t3=Thread(target=b.booking,args=(1,),name="Bhagavaan")
##
##t1.start()
##t2.start()
##t3.start()
##t1.join()
##t2.join()
##t3.join()
##print("MAin Thread")

'''Semaphore'''

##from threading import*
##
##class Bus:
##    def __init__(self,tkt):
##
##        self.tkt=tkt
##        self.l=BoundedSemaphore(3)
##        print(self.l)
##
##
##    def booking(self,r_tkt):
##        self.l.acquire()
##        print(self.l._value)
##        print("Avaialable Ticket:",self.tkt)
##
##        if(self.tkt>=r_tkt):
##            name=current_thread().name
##            print("{}  ticket is  booked by {}".format(r_tkt,name))
##            self.tkt -= r_tkt
##
##        else:
##            print("Sorry! All Tickets are Booked,")
##        self.l.release()
##
##b=Bus(2)
##
##t1=Thread(target=b.booking,args=(1,),name="Tarak")
##t2=Thread(target=b.booking,args=(1,),name="Vaddepa")
##t3=Thread(target=b.booking,args=(1,),name="Bhagavaan")
##
##t1.start()
##t2.start()
##t3.start()
##t1.join()
##t2.join()
##t3.join()
##print("MAin Thread")


'''Dead Lock'''

##from threading import*
##
##l1=Lock()
##l2=Lock()
##
##def book_tkt():
##    l1.acquire()
##    print("Bookticket Locked on Plan")
##    print("Bookticket Wants to lock class")
##    l2.acquire()
##    print("Bookticket locked seat.")
##    l2.release()
##    l1.release()
##    print("Booking Ticket Done.")
##
##
##def cancel_tkt():
##	l2.acquire()
##	print('Cancelticket Locked on Class')
##	print('Cancelticket Wants to lock Plan')
##	l1.acquire()
##	print('Cancelingticket locked seat')
##	l1.release()
##	l2.release()
##	print('Canceling ticket done')
##
##
##t1=Thread(target=book_tkt)
##t2=Thread(target=cancel_tkt)
##t1.start()
##t2.start()
	

##from threading import *
##l1 = Lock()
##l2 = Lock()
##
##def bookticket():
##	l1.acquire()
##	print('Bookticket Locked on plan')
##	print('Bookticket wants to lock Class')
##	l2.acquire()
##	print('Bookingticket locked seat')
##	l2.release()
##	l1.release()
##	print('Booking ticket done')
##	
##def cancelticket():
##	l2.acquire()
##	print('cancelticket Locked on Class')
##	print('cancelticket wants to lock Plan')
##	l1.acquire()
##	print('cancelingticket locked seat')
##	l1.release()
##	l2.release()
##	print('canceling ticket done')	
##	
##t1 = Thread(target=bookticket)
##t2 = Thread(target=cancelticket)
##t1.start()
##t2.start()














        
