'''Lock ->
==========
The Lock object can be held by only one thread at a time. If any other thread wants the same lock then it will have to wait until the other one releases it.
It’s similar to waiting in line to book a train ticket, public telephone booth etc.

acquire() method: A Thread can acquire the lock by using acquire() method
l.acquire()
release() method: A Thread can release the lock by using release() method.
l.release()

Note: Only the thread currently holding the lock is allowed to call the release() method thread,
otherwise we will get Runtime Error saying, RuntimeError: release unlocked lock'''

##from threading import*
##l=Lock()
##
##def wish(name,age):
##    for i in range(1):
##        l.acquire()
##        print("Good Morning,",name)
##        print("Your age is:",age)
##        l.release()
##
##t1=Thread(target=wish,args=("Rakesh",23))
##t2=Thread(target=wish,args=("Akash",21))
##t1.start()
##t2.start()
