'''1. Write a Python program to check if every consecutive sequence of zeroes is
followed by a consecutive sequence of ones of same length in a given string. Return True/False.'''

##def test(str1):
##    while '01' in str1:
##        str1 = str1.replace('01', '')
##    return len(str1) == 0
##
##str1 = "01010101"
##print("Original sequence:",str1)
##print(test(str1))

'''2. Write a Python program to add more number of elements to a deque object from an iterable object.'''

##import collections
##
##num=(1,3,5,7,9)
##
##deque=collections.deque(num)
##print("Numbers are:",deque)
##
##num2=(11,13,15,17,19,21)
##deque.extend(num2)
##print("More Numbers are:",deque)

'''3.Reverse a list without using inbuit method and [::-1].'''

##def rev(l):
##    r = []
##    for i in l:
##        r.insert(0, i)
##    return r
##
##print(rev([10,20,30,40]))


'''4.cummulative sum of a list.'''

##def cumSum(s):
##   sm=0
##   cum_list=[]
##   for i in s:
##      sm=sm+i
##      cum_list.append(sm)
##   return cum_list
##
##a=[10,20,30,40,50]
##print(cumSum(a))


'''5.write one example for pickling and unpickling?'''

'''Pickling'''

##import pickle
##
##list = [11, 'Python', b'Love Python']
##
##with open("data.pickle","wb") as f:
##    pickle.dump(list,f)
##
##print("Pickling completed!")


'''Unpickling'''

##import pickle
##
##with open("data.pickle","rb") as f:
##
##    r=pickle.load(f)
##    print(r)




















