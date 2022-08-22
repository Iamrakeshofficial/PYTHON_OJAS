'''1.Write a Python program to convert string element to integer inside a given tuple using lambda.
input tuple values:
(('233', 'ABCD', '33'), ('1416', 'EFGH', '55'), ('2345', 'WERT', '34'))
output tuple values:
((233, 33), (1416, 55), (2345, 34))'''

##t=(('233', 'ABCD', '33'), ('1416', 'EFGH', '55'), ('2345', 'WERT', '34'))
##l=[]
##for i in t:
##    m=list(i)
##    for j in m:
##        if j.isalpha():
##            m.remove(j)
##            l.append(tuple(m))
##print(tuple(l))



'''2. Write a Python program to extract year, month, date and time using Lambda.'''

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



'''3. Largest missing negative number 
you are given unsorted array A of N integers . you have to find the largest negative integer missing from the array.
example:1
input: A = -2 -1 0 1 2 
output:-3
example2:
input:-11 -10 -12
output:-11'''


##l=[-2,-1,0,1,2]
##l=[-11,-10,-12]
##l=[-1,1,-2,-3,4,5]
##neg=-1
##for i in l:
##    if neg not in l:
##        print(neg)
##        break
##    else:
##        neg=neg-1
##    

'''4. Roman Numerals
Write a program to convert a non-negative integer N to its Roman numeral representation. Roman numerals are usually written largest to smallest from left to right.
symbol value
I 1
V 5
X 10
L 50
C 100
D 500
M 1000
A number containing several decimal digits is built by appending Roman numeral equivalent for each, from highest to lowest, as in the following examples:
39 = XXX + IX = XXXIX.
246 = CC + XL + VI = CCXLVI.
789 = DCC + LXXX + IX = DCCLXXXIX.
2,421 = MM + CD + XX + I = MMCDXXI.
160 = C + LX = CLX
207 = CC + VII = CCVII
1,009 = M + IX = MIX
1,066 = M + LX + VI = MLXVI
1776 = M + DCC + LXX + VI = MDCCLXXVI
1918 = M + CM + X + VIII = MCMXVIII
Sample Input 1
2
Sample Output 1
II
Sample Input 2
1994
Sample Output 2
MCMXCIV'''


##n=int(input("enter a number to find Roman Numerals: "))
##num=[1,5,10,50,100,500,1000]
##rom=["I","V","X","L","C","D","M"]
##i=6
##
##while n>0:
##    div=n//num[i]
##    n=n%num[i]
##    
##    while div>0:
##        print(rom[i],end="")
##        div=div-1
##    i=i-1
##    

    

'''5.Group similar elements in a list:
Input : [1, 3, 5, 1, 3, 2, 5, 4, 2]
Output : [[1, 1], [2, 2], [3, 3], [4], [5, 5]]'''

##l=[1,3,5,1,3,2,5,4,2]
##l1=[]
##l2=[]
##for i in sorted(l):
##    if l.count(i)>=2:
##        l1.append([i,i])
##    else:
##        l1.append([i,])
##for i in l1:
##    if i not in l2:
##        l2.append(i)
##print(l2)
##        


