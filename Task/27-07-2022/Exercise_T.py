"""1.write a python program in shutil module using copy method."""
##import os  
##import shutil  
##  
####os.mkdir('F:\java')  
##   
##print('Empty Folder:', os.listdir('F:\java'))  
##  
##  
##shutil.copy('F:\Assesment.py', 'F:\java')  
##  
##  
##print('File Copied Name:', os.listdir('F:\java'))  


"""2.write a pthon program in os module using rename method."""
##import os
##os.rename("F:\RAKESH","F:\Rocky")


"""3.write a python program in fibonacci series using outer and inner functions."""

##def Fibonacci_Series():
##    def inner():
##        a = 0
##        b = 1
##        for i in range(20):
##            sum =a+b
##            a=b
##            b =sum
##            print(b)
##    return inner()
##
##
##
##Fibonacci_Series() 


"""4.write a python program in heapq module."""
##import heapq
##
##list = [14, 23, 4, 43, 34, 9, 18, 1, 25, 8]  
##  
##  
##heapq.heapify(list)  
##print(list)  
##   
##heapq.heappush(list, 20)   
##print(list)  
##heapq.heappop(list)
##print(list)
##heapq.heapreplace(list,99)
##print(list)

"""5.write a python program in shallow copy and deep copy."""
##import copy
##
##old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
##new_list = copy.deepcopy(old_list)
##
##print("Old list:", id(old_list))
##print("New list:", id(new_list))

'''Shallow Copy'''
##import copy
##
##old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
##new_list = copy.copy(old_list)
##
##old_list[1][1] = 'AA'
##
##print("Old list:", old_list)
##print("New list:", new_list)

"""Deep copy"""

##import copy
##
##old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
##new_list = copy.deepcopy(old_list)
##
##old_list[1][1] = 'BB'
##
##print("Old list:", old_list)
##print("New list:", new_list)
