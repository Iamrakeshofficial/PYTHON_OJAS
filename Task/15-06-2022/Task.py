'''1 write a program to print the kth largest number in the list.'''

##a= [23, 36, 12, 19, 10, 8, 66]

##b = sorted(a, reverse=True)
##print(b)
##
##k=4
##print ("kth largest element:", b[k-1])


'''2 write a function with name sum of cubes a to b that takes two integers and sum of the cubes from a to b.'''

##def sum_of_cubes(a,b):
##    s=0
##    for i in range(a,b+1):
##        x=i**3
##        s=s+x
##    return s
##a= int(input())
##b=int(input())
##print(sum_of_cudes(a,b))

'''3 write a program to remove duplicates numbers.'''

##my_list = [1,2,2,3,1,4,5,1,2,6]
##l = []
##for i in my_list:
##    if i not in l:
##        l.append(i)
##print(list(l))

'''4 write a program tht given function will return the second character in the word passed to the function.'''

##def second_character(a):
##    msg=a[1]
##    return msg
##a=input()
##print(second_character(a))

'''5) write a program to remove n key-value pairs from the dictionary if they present.'''

b={"name":"Rakesh","company":"IBM"}
a=input()
for i in a:
    if i in b:
        del b[i]
print(b)
