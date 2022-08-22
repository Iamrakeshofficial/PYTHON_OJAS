
"""Why use generators when the return statement is already present?"""

##The most well-known feature of generators is their excellent memory efficiency.
##A standard function that returns a sequence will first construct the
##whole sequence in memory before returning the result.
##If the number of elements in the sequence is enormous, this is overkill.
##The generator implementation of such sequences, on the other hand,
##is memory-friendly and preferable since it only generates one item at a time.


"""Program to print the Power of two up to the given number."""

##def PowerTwoGen( max=0 ):
##   n = 1
##   while n < max:
##       yield 2 ** n
##       n += 1
##
##a = PowerTwoGen(6)
##for i in a:
##   print(i)
"""A simple generator for Fibonacci Numbers."""

##def fib(max):
##   p, q = 0, 1
##
##   while p < max:
##       yield p
##       p, q = q, p + q
##
##n = int(input("Enter the number up to : \n"))
##
##x = fib(n)
##print("Resultant Series up to", n, "is :")
##for i in x:
##   print(i)

"""to generate first n numbers"""

##def first(num):
##    n=1
##    while n<=num:
##        yield n
##        n=n+1
##
##values=first(5)
##for x in values:
##    print(x)
##
"""find the squares of number in a given range using generator expression."""
##g=(x*x for x in range(1000))
##print(next(g))
##print(next(g))
##print(next(g))
##print(next(g))
##print(next(g))
##

"""find the sqaure of a number in a given range using Generator expression."""

##Gen =(x ** 2 for x in range(4))
##print(next(Gen))
##print(next(Gen))

"""Print Even numbers using generator"""
##def even(x):
##    for i in range(x):
##        if i%2==0:
##            yield i
##
##result=even(8)
##for j in result:
##    print(j)
"""find the sum of squares of  Number using generator comprehension."""
##a = (x*x for x in range(5))
##print(sum(a))



"""Square of a list Using list Comprehension"""
##my_list = [1, 3, 6, 10]
##list = [x**2 for x in my_list]
##print(list)

""" same thing can be done using a generator expression
 generator expressions are surrounded by parenthesis () it will give generator object only"""

##my_list = [1, 3, 6, 10]
##generator = (x**2 for x in my_list)
##print(generator)

"""Square of a list using generator comprehension"""
##my_list = [1, 3, 6, 10]
##
##a = (x**2 for x in my_list)
##print(next(a))
##
##print(next(a))
##
##print(next(a))
##
##print(next(a))

"""Sending object to Generator"""


