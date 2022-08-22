'''ZeroDivisionError using try,except,else,finally block'''

##x =int(input("Enter x Value:"))
##y = int(input("Enter y Value:"))
##try:
##    
##    d = x/y
##    print(d)
##
##except ZeroDivisionError:
##    print("Please Enter Greater than Zero in denominator.")
##
##else:
##    print("I am from else block.")
##    
##finally:
##    
##    print('Rest of the Code')

'''Using Exception as Alias Name:'''

##x =int(input("Enter x Value:"))
##y = int(input("Enter y Value:"))
##try:
##    
##    d = x/y
##    print(d)
##
##except ZeroDivisionError as obj:
##    print(obj)
##
##else:
##    print("I am from else block.")
##    
##finally:
##    
##    print('Rest of the Code')

'''Multiple Exception'''

##x =int(input("Enter x Value:"))
##y = int(input("Enter y Value:"))
##try:
##    
##    d = x/o
##    print(d)
##
##except ZeroDivisionError:
##    print("Please Enter Greater than Zero in denominator.")
##
##except NameError as obj:
##    print(obj)
##
##else:
##    print("I am from else block.")
##    
##finally:
##    
##    print('Rest of the Code')

       #OR#

##x =int(input("Enter x Value:"))
##y = int(input("Enter y Value:"))
##try:
##    
##    d = x/o
##    print(d)
##
##except (ZeroDivisionError,NameError) as obj:
##    print(obj)
##
##else:
##    print("I am from else block.")
##    
##finally:
##    
##    print('Rest of the Code')


##a=10
##b=0
##try:
##    d=a/b
##    print(d)
##
##except:
##    print("Exception Handling:")
##
##print("Rest Of the program.")
##

'''How to create your own exception and manage it.'''

##class balance_Exception(Exception):
##    def __init__(self,arg):
##        self.msg=arg
##
##def check_Balance():
##    money=10000
##    withdraw=900
##    try:
##        balance=money-withdraw
##
##        if (balance<=200):
##            raise balance_Exception("Insufficient BAlanace.")
##        print(balance)
##
##    except balance_Exception as obj:
##        print(obj)
##
##check_Balance()
##



















            






















