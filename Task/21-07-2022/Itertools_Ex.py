"""In Python, an iterator is an object used to iterate over iterable objects
such as lists, tuples, dictionaries, and sets.
An object is called iterable if we can get an iterator from it or loop over it.

A Python iterator object must implement two specific methods, __iter__() or iter() and __next__() or next() ,
which are referred to collectively as the iterator protocol.

Python iter()->

The iter() function in Python returns an iterator for the supplied object.
The iter() generates a thing that can be iterated one element at a time.
These items are handy when combined with loops such as for loops and while loops. 

Syntax:

iter( object , sentinel )

Python next()->

The next() function returns the next item from the iterator. The next() function holds the value one at a time. 

Syntax:

next( iterator , default )
"""
# Program to print the list using Iterator protocols

##X = [25, 78, 'Coding', 'is', '<3']
##a = iter(X)
##print(a)
##
##
##print(next(a))
##
##print(next(a))
##
##print(next(a))
##print(next(a))
##print(next(a))


##class MyNumbers:
##  def __iter__(self):
##   self.a = 1
##   return self
##
##  
##  def __next__(self):
##    
##    if self.a <= 5:
##       x = self.a
##       self.a += 1
##       return x
##
### Create the object of the class
##myclass = MyNumbers()
### get an iterator using iter()
##myiter = iter(myclass)

# printing the values using a for-in loop
##for x in myiter:
## print(x)
"""combination of 3 elements in a list using iterator."""
##import itertools
##a=[10,20,30,40,50]
##b=list(itertools.combinations(a,3))
##print(b)

"""groupby() in itertools"""

##import itertools
##lst = [("a", 5, 6), ("b", 2, 4), ("a", 2, 5), ("c", 2, 6)]

##def test(lst):
##    groups=itertools.groupby(lst,key=lambda x:x[1])
##    for key,group in groups:
##        print(key,list(group))
##
##test(lst)

"""dropwhile() in itertools"""

##import itertools
##lst=[2,4,6,8,10,12,13,14,15,16]
##
##def even(x):
##    return  x%2==0
##
##result=list(itertools.dropwhile(even,lst))
##print(result)


"""combinations() in itertools"""
##import itertools
##
##a=[10,20,30,40,50]
##b=list(itertools.combinations(a,4))
##print(b)

"""Compress() by itertools"""

##import itertools
##
##word =  'TARKESHRAO'
##selector = [1, 0, 1, 0, 0, 0, 0, 1, 1, 1]
##
##result=list(itertools.compress(word,selector))
##print(result)
##    
##for i in result:
##    print(i)
"""takewhile() By itertools"""
##from itertools import takewhile
##
##def character(str):
##    substring = 'o'
##    if substring in str:
##        return True
##    else:
##        return False
##        
##lst = ['lorem', 'ipsum', 'dolor', 'sit', 'amet']
##print(list(takewhile(character, lst)))
