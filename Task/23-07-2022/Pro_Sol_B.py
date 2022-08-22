"""1) using functools write a program on partialmethod, url_cache and total_ordering."""
"""@partial Method"""
##from functools import partial
##def multiply(x,y):
##    return x*y
##
##b=partial(multiply,2)
##print(b(4))

"""@total ordering"""
##from functools import total_ordering
##
##@total_ordering
##
##class Car(object):
##    def __init__(self,milage,model):
##        self.milage=milage
##        self.model=model
##
##    def __eq__(self,other):
##        return self.milage==other.milage
##
##    def __lt__(self,other):
##        return self.milage<other.milage
##
##
##c1=Car("Audi",700)
##c2=Car("BMW",800)
##
##print(c1==c2)
##print(c1<c2)
##print(c1<=c2)
##print(c1>=c2)
##
"""@lru cache"""

##from functools import lru_cache
##import time
##
### Function that computes fibonacci without lru_cache
##def fibonacci(n):
##    if n < 2:
##        return n
##    return fibonacci(n-1) + fibonacci(n-2)
##	
##
##starttime = time.time()
##
##print("The fibonacci number is",fibonacci(10))
##endtime = time.time()
##
##print("Time taken to execute fibonacci without lru_cache is", endtime-starttime)
##
### Function that computes fibonacci with lru_cache
##@lru_cache (maxsize=32)
##def fibonacci(n):
##    if n < 2:
##        return n
##    return fibonacci(n-1) + fibonacci(n-2) 
##	
##starttime = time.time()
##
##print("The fibonacci number is",fibonacci(10))
##endtime = time.time()
##
##print("Time taken to execute fibonacci with lru_cache is", endtime-starttime)
##print(fibonacci.cache_info())





















