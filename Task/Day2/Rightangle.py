n=int(input("Enter Number Of Rows For Right angle Triangle:"))
alphabet=65
for i in range(0,n):
    for j in range(0,i+1):
        print('%c' %(alphabet+j),end='')
    print()