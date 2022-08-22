'''1.write a program Example 9: Pascal's Triangle'''

##rows = int(input("Enter the number of rows : "))
##for i in range(0, rows):
##    coff = 1
##    for j in range(1, rows-i):
##        print("  ", end="")
##    
##    for k in range(0, i+1):
##        print("  ", coff, end="")
##        coff = int(coff * (i - k) / (k + 1))
##    print()

'''2.write a program to count number of chareters and print accending and desending order.

input:RameshRam
output:a-2,e-1,h-1,m-2,R-2,s-1- assending
decending :s-1,R-2m-2,,h-1,e-1a-2,'''

##n=input("Enter a String to Print the Characters:")
##
##print("The original string is :{}".format(n))
##
##l=[]
##for i in n:
##    if i not in l:
##        l.append(i)
##for i in l:
##    print("The characters are in the given string:",i,"-",n.count(i))
##
##for i in sorted(l):
##    print("The Asceding Characters are:",i,"-",n.count(i))
##
##    
##for i in sorted(l)[::-1]:
##    print("The Desceding Characters are:",i,"-",n.count(i))


'''3.Python Program to Find HCF or GCD'''

##n1 = int(input("Enter first number: "))  
##n2 = int(input("Enter second number: "))
## 
##i = 1
##while(i <= n1 and i <= n2):
##    if(n1 % i == 0 and n2 % i == 0):
##        gcd = i
##    i = i + 1
## 
##print("The H.C.F. of {} and {} is {} ".format(n1, n2, gcd))



'''4.Write a Python program to find the list with maximum and minimum length using lambda.'''
##
##l=[10,9,8,7,6,5,4,3,2]
##Max=lambda x:max(l)
##Min=lambda y:min(l)
##print(Max(l))
##print(Min(l))


'''5.Write a Python program to count the same pair in two given lists. use map() function. '''

##from operator import eq
##def count_same_pair(nums1, nums2):
##    result = sum(map(eq, nums1, nums2))
##    return result
##
##nums1 = [1,2,3,4,5,6,7,8]
##nums2 = [2,2,3,1,2,6,7,9]
##
##print("Original lists:")
##print(nums1)
##print(nums2)
##print("\nNumber of same pair of the said two given lists:")
##print(count_same_pair(nums1, nums2))

