'''1) WAPP to reverse internal content of every second word present in the given String.'''

##n=input("Enter a String which contain more than one word:")
##l=n.split()
##l1=[]
##i=0
##while i<len(l):
##    if i%2==0:
##        l1.append(l[i])
##    else:
##        l1.append(l[i][::-1])
##    i=i+1
##    output=' '.join(l1)
##print(output)


'''2) WAPP for the following requirements
    input->a3z2b4
    output->aaabbbbzz(sorted string).'''

##s=input("Enter a String which contains alphanumeric values:")
##string=''
##for ch in s:
##    if ch.isalpha():
##        x=ch
##    else:
##        d=int(ch)
##        string=string+x*d
##output=''.join(sorted(string))
##print(output)
    

'''3)WAPP  to extract year ,month,date and time using lambda Function.'''

##import datetime
##now = datetime.datetime.now()
##print(now)
##year = lambda x: x.year
##month = lambda x: x.month
##day = lambda x: x.day
##time = lambda x: x.time()
##print(year(now))
##print(month(now))
##print(day(now))
##print(time(now))

'''4)WAPP to find the values of length six in given list using lambda Function.'''

##weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
##days = filter(lambda day: day if len(day)==6 else '', weekdays)
##for d in days:
##  print(d)
'''5)WAPP to find factorial of number using closure Function.'''

##def My_Function(num):
##    fact = 1
##    def factorial(fact):             
##        
##        for i in range(1,num+1):
##            fact = fact*i
##       
##        return fact
##    return factorial(fact)
##    
##n=int(input("Enter a Number:"))
##result=My_Function(n)
##print("The Factorial of {} is {}".format(n,result))
