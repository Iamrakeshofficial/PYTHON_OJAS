##Dict Methods/Pre-defined Functions:
##===================================
##clear(...)
## |      D.clear() -> None.  Remove all items from D.
## |  
## |  copy(...)
## |      D.copy() -> a shallow copy of D
## |  
## |  get(self, key, default=None, /)
## |      Return the value for key if key is in the dictionary, else default.
## |  
## |  items(...)
## |      D.items() -> a set-like object providing a view on D's items
## |  
## |  keys(...)
## |      D.keys() -> a set-like object providing a view on D's keys
## |  
## |  pop(...)
## |      D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
## |      
## |      If the key is not found, return the default if given; otherwise,
## |      raise a KeyError.
## |  
## |  popitem(self, /)
## |      Remove and return a (key, value) pair as a 2-tuple.
## |      
## |      Pairs are returned in LIFO (last-in, first-out) order.
## |      Raises KeyError if the dict is empty.
## |  
## |  setdefault(self, key, default=None, /)
## |      Insert key with a value of default if key is not in the dictionary.
## |      
## |      Return the value for key if key is in the dictionary, else default.
## |  
## |  update(...)
## |      D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
## |      If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
## |      If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
## |      In either case, this is followed by: for k in F:  D[k] = F[k]
## |  
## |  values(...)
## |      D.values() -> an object providing a view on D's values
## 

'''1)clear():
----------
=>This is used for removing all the entires of dict objct.
=>Syntax:- dictobj.clear()'''

##Examples:
##-----------------------
##d1={'Apple': 25.67, 'Kiwi': 30, 'Sberry': 100.34, 'Mango': 80}

##print(d1)
##d1.clear()
##print(d1)

'''2)copy():
---------
=>This function is used for copying the content of one dict object into 
another dict object (shallow Copy)
=>Syntax:- dictobj2=dictobj1.copy()'''

##Examples:
##-------------------------
##d1={'Apple': 25.67, 'Kiwi': 30}

##print(d1,id(d1))
##d2=d1.copy()
##print(d2,id(d2))

'''3)get():
----------
=>This function is used for obtaining value of Value by passing value of 
Key.
=>If the value of Key does not exists then we get None
=>Syntax:- varname=dictobj.get(Key)'''
##Examples:
##---------
##d1={'Apple': 25.67, 'Kiwi': 30,'Orange':40}

##print(d1)
##v1=d1.get('Kiwi')
##print(v1)
'''4)items():
----------
=>This function obtains all (Key,value) from from dict object in the form 
tuple.
=>when we call items() upon empty dict object then we get empty list.
Syntax:- keyvalue=dictobj.items()'''
##-----------
##Examples:
##----------
##d1={'Apple': 25.67, 'Kiwi': 30, 'Sberry': 100.34, 'Mango': 80}

##rk=d1.items()
##print(rk)
##for rk in d1.items():
##    print(rk)

'''5)keys():
---------
=>This Function obtains list of keys from non-empty dict object.
=> when we call keys() upon empty dict then we get empty list
=>Syntax: keys=dictobj.keys()'''
##Examples:
##----------
##d1={'Apple': 25.67, 'Kiwi': 30, 'Sberry': 100.34, 'Mango': 80}

##print(d1)
##d1.keys()
##s=d1.keys()
##print(s)
'''6)pop():
--------
=>This function is used for removing (Key,Value) from dict object by passing 
Value of Key. 
=>If the Value of Key does not exists in dict object then we get KeyError.
=>Syntax:- dictobj.pop(key)'''
##Examples:
##---------
##d1={'Apple': 25.67, 'Kiwi': 30, 'Sberry': 100.34, 'Mango': 80}

##print(d1)
##print(d1.pop("Kiwi"))
##print(d1)

'''7)popitem():
------------
>This Function is used for removing the last (Key,Value ) from dict object
=>When we call popitem() upon empty dict object then we get KeyError
=>Syntax: dictobj.popitem()'''
##----------
##Examples:
##---------
##d1={'Apple': 25.67, 'Kiwi': 30, 'Sberry': 100.34, 'Mango': 80}

##print(d1)
##d1.popitem()
##
##print(d1)

'''8)setdefault():
---------------
setdefault():- The setdefault() method returns the value of the item with the specified key.
If the key does not exist, insert the key, with the specified value, see example below
Syntax=dictobj.setdefault()'''

##Example:
##--------
##d1={'Apple': 25.67, 'Kiwi': 30, 'Sberry': 100.34, 'Mango': 80}

##d1.setdefault('dragon')
##print(d1)
"""9)update():
-----------
 The update() method inserts the specified items to the dictionary.
The specified items can be a dictionary, or an iterable object with key value pairs."""

##Examples:
##---------
##d1={"Praveen":"Python","Kiran":"Java"}
##d2={"RS":"Django","DR":"C"}
##d3=d1.update(d2)
##print(d1)
##print(d2)
##print(d3)

'''10)values():
------------
=>This Function obtains list of values from non-empty dict object.
=> when we call values() upon empty dict then we get empty list
=>Syntax: values=dictobj.values()'''

##Examples:
##-----------------
##d1={'Apple': 25.67, 'Kiwi': 30, 'Sberry': 100.34, 'Mango': 80}
##print(d1)
##d1.values()
##s=d1.values()
##print(s)
##for val in d1.values():
##    print(val)
