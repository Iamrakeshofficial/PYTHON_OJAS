'''1).Write a Python program to remove and print every third number from a list of numbers until the list becomes empty.'''

##def remove(list):
##    pos=3-1
##    index=0
##    len_list=len(list)
##
##    while len_list>0:
##        index=(pos+index)%len_list
##        print(list.pop(index))
##
##        len_list-=1
##
##nums = [10,20,30,40,50,60]
##
##remove(nums)

'''2).Write a Python program to count the number of students of individual class.
Sample Output:
Counter({'VI': 3, 'V': 2, 'VII': 1})'''



'''3).Write a Python program to concatenate all elements in a list into a string and return it.'''


##def concat(list):
##    b=''
##    for element in list:
##        b+=str(element)
##    return b
##print(concat([10,20,30,40,50,60]))


'''4).Write a Python program to convert a float to ratio. 

Expected Output :

21/5 '''



'''5).Write a Python function that prints out the first n rows of Pascal’s triangle.'''


def pascal(num):
    row=[1]
    y=[0]
    for x in range(max(num,0)):
        print(row)
        row=[a+b for a,b in zip(row+y,y+row)]

    return num>=1

pascal(5)

        
