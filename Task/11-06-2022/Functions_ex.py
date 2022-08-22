'''1. What about two asterisks (**)?'''
##If you are uncertain about how many keyword arguments have to be passed to a function in the program,
##then you can use an argument with the double asterisks as a prefix to the argument
##which allows us to pass an arbitrary number of keyword arguments into our function.
##This allows the function to receive a dictionary of arguments and it can then access the items accordingly.

'''2.Write a function called fizz_buzz that takes a number.
-If the number is divisible by 3, it should return “Fizz”.
-If it is divisible by 5, it should return “Buzz”.
-If it is divisible by both 3 and 5, it should return “FizzBuzz”.
-Otherwise, it should return the same number.'''

##def fizz_buzz(n):
##    if n%3==0 and n%5==0:
##        print("FizzBuzz")
##    elif n%5==0:
##        print("Buzz")
##    elif n%3==0:
##         print("Fizz")
##    else:
##         print(n)
###main program

##a=int(input("Enter a Number:"))
##fizz_buzz(a)
'''3.Write a function called showNumbers that takes a parameter called limit.
It should print all the numbers between 0 and limit with a label to identify the even and odd numbers.
For example, if the limit is 3, it should print:
-0 EVEN
-1 ODD
-2 EVEN
-3 ODD '''
##def showNumbers(n):
##    for i in range(1,n+1):
##        if i%2==0:
##            print("-",i," even")
##        else:
##            print("-",i," odd")
###main Program
##a=int(input("Enter a Number:"))
##showNumbers(a)

'''4.Write a function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter).
For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20.'''

##def sum_multiples(n):
##    for i in range(1,n+1):
##        if i%3==0 or i%5==0:
##            print(i,end=" ")
###Main Program
##a=int(input("Enter the Number:"))
##sum_multiples(a)

'''5.Write a function that prints all the prime numbers between 0 and limit where limit is a parameter.

6.Write a function for checking the speed of drivers. This function should have one parameter: speed.
1.If speed is less than 70, it should print “Ok”.
2.Otherwise, for every 5km above the speed limit (70), it should give the driver one demerit point and print the total number of demerit points. For example, if the speed is 80, it should print: “Points: 2”.
3.If the driver gets more than 12 points, the function should print: “License suspended”

7. What is the result of “bag” > “apple”?

8.What is the result of f“{2+2}+{10%3}”?

9.Write a function calculation() such that it can accept two variables and calculate the addition and subtraction of it. And also it must return both addition and subtraction in a single return 

10. Create an inner function to calculate the addition in the following way
Create an outer function that will accept two parameters a and b
Create an inner function inside an outer function that will calculate the addition of a and b
At last, an outer function will add 5 into addition and return it.

11.Write a recursive function to calculate the sum of numbers from 0 to 10

12. Assign a different name to function and call it through the new name

13.Generate a Python list of all the even numbers between 4 to 30

14.Return the largest item from the given list

15.Create a function showEmployee() in such a way that it should accept employee name, and it’s salary and display both,
and if the salary is missing in function call it should show it as 9000.'''
