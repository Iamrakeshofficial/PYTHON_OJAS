'''1) Find number of small words in a string and their length?
eg:-This is an offical page
output:- is-2 
         an-2'''

##s=input("Enter a String to Find Small Words:")
##l=s.split()
##l1=[]
##
##print("The Original String words are{}:".format(s))
##print(l)
##for i in l:
##    if i not in l1 and len(i)<=2:
##        l1.append(i)
##        print(i,"-",l.count(i))
##    
##    
        
 

'''2) Find palindrome in a given string small and large words?
eg:- mom and dad speak malayalam with nitin
mom
dad
malayalam'''

##
##l=[]
##string="mom and dad speak malayalam with nitin"
##l2=string.split()
##for i in l2:
##    if i==i[::-1]:
##        l.append(i)
##        
##print("The  Palindrome Words in the Given String are:{}".format(l))

'''3) Find the digit is binary or not?
eg:-1011
is binary number
24:-
its is not a binary '''


##num = int(input("please give a number : "))
##while(num>0):
##    j=num%10
##    if j!=0 and j!=1:
##        print("num is not binary")
##        break
##    num=num//10
##    if num==0:
##        print("num is binary") 

'''4)Write a program to print the emojis.
😀
😘
🤗
😪
😷'''

##print("\U0001f600")
##print('\U0001f618')
##print("\U0001f917")
##print("\U0001f62A")
##print("\U0001F637")
##

##5)WAP Login email page ?
##
##example:- email_id='Prudhvi1998@gamil.com'
##          password='Rolex123'
##
##if email_id and password True 
##
##output:- prudhvi your email-id successfully open
##
##if email_id or password False
##
##Prudhvi your enter wrong password try agin .


##username = input("Please enter your username : ")
##password = input("Please enter your password : ")
##print ("Greetings," , username, "you are now logged in now with a password")
##
##command = input("Please type a command :")
##if command == "log off":
##    print ("You have now been logged off again",username)
##    username == ""
##    password == ""
##
##username = input("Please enter your username : ")
##password = input("Please enter your password : ")
##
##while (username != "username" and password != "password"):
##
##    print (" Sorry username and password incorrect please re-enter for validation ")
##    username = input("Please enter your username : ")
##    password = input("Please enter your password : ")
##
##else:
##    print ("Greetings," , username, "you are now logged in now with your password")
