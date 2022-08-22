'''How to Print Main Thread.'''

##import threading
##t=threading.current_thread().getName()
##print(t)

'''Create a Thread Without Class'''

##from threading import Thread

##def disp():
##    print("Hello Guys")
##
##t=Thread(target=disp)
##t.start()


##def sisp(a,b):
##    print("Thread Running:",a,b)
##
##t=Thread(target=sisp,args=(10,20))
##t.start()


##def disp(a,b):
##    print("Running:",a,b)
##
##for i in range(5):
##    t=Thread(target=disp,args=(10,20))
##
##    t.start()
##    

##def rakesh():
##    for i in range(5):
##        print("Child Thread:")
##
##t=Thread(target=rakesh)
##t.start()
##
##def akash():
##for i in range(5):
##    print("Main Thread.")

##t=Thread(target=akash)
##t.start()

'''set thread name and get Thread Name'''

##from threading import*

##def disp():
##    print("Child Thread",current_thread())
##    print("Default Thread Name:",current_thread().getName())
##
##    current_thread().setName('Document Thread')
##
##    print("given New Thread Name:",current_thread().getName())
##
##    current_thread().name='Rakesh Thread'
##    print("Current Thread Name:",current_thread().name)
##t=Thread(target=disp)
##
##t.start()
##
##
##print("Main Thread",current_thread())
##print("Default Thread Name:",current_thread().getName())
##
##current_thread().setName('Tarak Thread')
##print("New Main Thread:",current_thread().getName())
##
##current_thread().name='Vaddepa Thread'
##print("Recent Thread Name:",current_thread().name)




##def rakesh():
##    pass
##
##t=Thread(target=rakesh)
##print("Default Child Thread:",t.getName())
##t.setName('Tarak Thread')
##print("New Child Thread NAme:",t.getName())
##t.name='Vadeppa Thread'
##print(t.name)

'''Creating Thread  by Inheriting Thread class'''

##from threading import*
##
##class Myclass(Thread):
##    pass
##
##t=Myclass()
##print(t.name)

'''Creating a Thread by Extending Thread Class using  run()'''

##from threading import*
##
##class MyThread(Thread):
##    def run(self):
##        for i in range(10):
##            print("Hello World")
##
##t=MyThread()
##t.start()
##
##for i in range(5):
##    print("Tarak")


       
'''Creating a Thread Without Extending Thread Class'''

##from threading import*
##class Test:
##    def disp(self):
##        for i in range(10):
##            print('Hello')
##
##
##
##obj=Test()
##t=Thread(target=obj.disp)
##t.start()
##
##for i in range(5):
##    print("Hello World")
    
  

'''Creating a Thread By not using any class using join()'''

##from threading import*
##
##def square(number):
##    for i in number:
##        print("Square VAlues:",i*i)
##
##
##def rakesh(number):
##    for i in number:
##        print("Double values:",2*i)
##
##number=[1,2,3,4,5]
##t1=Thread(target=square,args=(number,))
##t2=Thread(target=rakesh,args=(number,))
##
##t1.start()
##t2.start()
##t1.join()















        
        
