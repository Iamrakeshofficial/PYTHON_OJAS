
'''
1write a program to print the list of elements of prinicipal diaognal
input:
3 3
1  2 3
10 20 30
5  10 15
output:[1, 20, 15]'''


##import numpy as np
##a=np.array([[1,2,3],
##            [10,20,30],
##            [5,10,15]])
##d=np.diag(a)
##print(d)

'''
2.wap take a string sparate with space and done add,sub,mul,div?
eg:- input:-18 7
     output:-(25,12,126,2)'''

##a=input("Enter the Numbers with Space:").split(" ")
##b=int(a[0])
##c=int(a[1])
##add=b+c
##sub=b-c
##mul=b*c
##div=b//c
##z=add,sub,mul,div
##print(tuple(z))


'''

3.In this question, we will provide an integer int_1, we have already declared the calculate_sum 
function for you in solution.py. The initial int_1 of this function represents the initial value, 
and you need to calculate the form a + aa + aaa + aaaa value, and finally print the result.
input:5
output:6170'''

##a=input("Enter a Number:")
##k=0
##for i in range(1,5):
##    
##    temp=str(a)*i
##    k=k+int(temp)
##print(k)


'''
4.Please complete the code in solution.py to realize the function of get_sum. get_sum function receives an array parameter nums. Please use the lambda function to pass 
in two unknown number x and y for the get_sum function and take this lambda function as the return value of the get_sum function. For the parameter nums received by get_sum, 
if the length of the array num is an even number, return the sum of nums by x times. If the length of the array num is an odd number, return the sum of nums by -y times.
input:[1,2,3,4]
       2,3
output:20
'''
##a=[1,2,3,4]
##len_a=len(a)
##e=sum(a)
##print(e)
##b=input().split(",")
##c=int(b[0])
##d=int(b[1])
##
##if len_a%2==0:
##    print(e*c)
##else:
##    print(e*-d)
    




'''
5.Mathematicians have come up with a famous conjecture - the Collatz conjecture.
For any positive integer n, if n is even, make it n // 2.
If n is an odd number, make it 3 * n + 1.
If you follow this rule, you must end up with 1.
How many rounds of transformation will that number go through to become 1?
'''

##def collatz(num):
##    while num != 1:
##        print(num)
##        if num % 2 == 0:
##            num = int(num / 2)
##        else:
##            num = int(3 * num + 1)
##    else:
##        print(num)
##        print('Done!')
##
##
##def main():
##    num = int(input('Input an integer: '))
##    collatz(num)
##main()











