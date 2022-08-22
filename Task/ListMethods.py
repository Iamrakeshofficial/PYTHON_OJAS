##List Methods:
##===============

## |  append(self, object, /)
## |      Append object to the end of the list.
## |  
## |  clear(self, /)
## |      Remove all items from list.
## |  
## |  copy(self, /)
## |      Return a shallow copy of the list.
## |  
## |  count(self, value, /)
## |      Return number of occurrences of value.
## |  
## |  extend(self, iterable, /)
## |      Extend list by appending elements from the iterable.
## |  
## |  index(self, value, start=0, stop=9223372036854775807, /)
## |      Return first index of value.
## |      
## |      Raises ValueError if the value is not present.
## |  
## |  insert(self, index, object, /)
## |      Insert object before index.
## |  
## |  pop(self, index=-1, /)
## |      Remove and return item at index (default last).
## |      
## |      Raises IndexError if list is empty or index is out of range.
## |  
## |  remove(self, value, /)
## |      Remove first occurrence of value.
## |      
## |      Raises ValueError if the value is not present.
## |  
## |  reverse(self, /)
## |     
## |  sort
'''1) append():'''
'''---------------------'''
'''=>This Function is used for adding the values to the list at end of existing''' 
'''elements of list.'''
'''=>Syntax:- listobj.append(element)'''
##Example:
##--------------
##l1=[1,2,4]
##l1.append(3)
##print(l1)

'''2) clear():'''
'''----------------'''
'''=>This function is used for removing / deleting all the elements of list '''
'''object'''
'''=>Syntax:- listobj.clear()'''
##Examples:
##l1=[10,20,30,40,50]
##l1.clear()
##print(l1)

'''3)copy():
--------
=>This Function is used copying the content of one list object into another 
list object ( implementing shallow copy)
-----------------
Syntax:- listobj2=listobj1.copy()'''
##Examples:
##--------
##lst1=[10,"Python","Rossum",34.56]

##lst2=lst1.copy()
##print(lst1)
##
##print(lst2)
##lst1.append(True)
##print(lst1)
'''4)count():
----------------
=>This function is used for counting / finding number of occurences of the 
specified element .
=>If the specified element does not exists in list object then we get 0.
Syntax:- listobj.count(element)
--------------------------'''
##Examples:
##--------------------------
##lst=[10,20,"python",10,"python",10,30,20,10]
##print(lst.count(10))
'''5)Extend():
-----------
This function is used for extending functionality of source list object 
with destination list object 
=>Syntax: sourcelistobject.extend(destination list obj)'''
##Examples:
##---------
##lst1=[10,20,30]
##lst2=["Java","python","DS","AI"]
##lst1.extend(lst2)
##print(lst1)

'''6)Index():
----------
This function is used for obtaining an index of the First occurence of 
specified eleement 
=>If element does not exists in list object then we get ValueError.
------------------
Syntax:- listobj.index(element)'''
##Examples:
##---------
##lst=[10,20,"python",10,"python",10,30,20,10]
##print(lst.index(10))
##print(lst.index(20))

'''7)insert():
-----------
=>This Function is used for inserting a Value at a perticyulat exiting index 
by passing Index and Element.
----------------
=>Syntax: listobj.insert(index,element)'''
##----------
##Examples:
##----------
##l1=[10,20,30,40,-45]
##print(l1)
##l1.insert(2,"Python")
##print(l1)
'''8)pop():
--------
=>This function is used for removing last element of list object (last 
indexed element) 
=>when we call pop() on empty list object then we get IndexError.
Syntax:-listobj.pop()'''

##Examples:
##--------
##lst=[10,"Python","Rossum",34.56,True]
##print(lst)

##print(lst.pop())
'''9)remove():
-----------
=>This Function is used removing / deleting First Occurence of the specified 
element
=>If the element is not present in list then we get ValueError
Syntax:- listobj.remove(element)'''
##Examples:
##---------
##l1=[10,"Python","Java",10,23.45,"PYTHON"]

##print(l1)
##l1.remove(10)
##
##print(l1)
'''10)reverse():
-------------
>This function is used for obtaining reverse of elements of list object 
=>Syntax:- listobj.reverse()
---------------------------'''
##Examples:
##---------
##lst1=[10,"Python","Rossum",34.56]
##print(lst1)
##lst1.reverse()
##print(lst1)

'''11)sort():
----------
=>This function is used for sorting the given homogeneous data of list object 
either Ascending Order or in decending order.
=>Syntax: listobj.sort(reverse=False / True )
------------------
=>If reverse=False then sort() sorts the data in Ascending order
=>If reverse=True then sort() sorts the data in Decending order
=>If we don't write reverse=False then ity similar to sort() and sorts the 
data in Ascending order
'''
##Examples:
##---------
lst2=[10,20,30,-23,45,2,67,34]
print(lst2)
lst2.sort()
print(lst2)
lst2.reverse()
print(lst2)
