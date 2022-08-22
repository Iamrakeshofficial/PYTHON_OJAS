''' Write a  Python Program using Multithreading ,
Consider a couple who is having a Joint account and both are having their ATM cards.
They come to different ATMs and try to withdraw some amount at the same time.
Let’s say the total balance in the account is 500 and Wife tries to withdraw 450
and the husband tries to withdraw 100. When they swipe the card for withdrawing money,
the balance shown will be 500. Two threads will be created for the transaction,
out of which only one thread should be successful and the other should fail.
If both the threads get successful then its a loss to the bank.
So, the threads should be in synchronization so that one fails and the other wins.'''

##from threading import *
##class Joint_acc:
##    def __init__(self,avail_bal):
##        self.avail_bal=avail_bal
##        self.l=Lock()
##
##    def reserve(self,curr_bal):
##        self.l.acquire(blocking=True)
##        print(" Available Balance is:",self.avail_bal)
##        if self.avail_bal >=curr_bal:
##             name=current_thread().name
##             print(f"{curr_bal} is  withdraw by {name}")
##             self.avail_bal-=curr_bal
##        else:
##            print("OOp's Insufficient Balance")
##        self.l.release()
##        
##j=Joint_acc(500)
##t1=Thread(target=j.reserve,args=(450,),name='Wife')
##t2=Thread(target=j.reserve,args=(100,),name='Husband')
##t1.start()
##t2.start()
##t1.join()
##t2.join()
