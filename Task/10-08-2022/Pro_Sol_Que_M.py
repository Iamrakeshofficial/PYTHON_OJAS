'''Given a sentence as input print all the unique combinations of two words in lexicographical order
explanation:
if given sentence is raju plays cricket the possible combintion of two are (cricket,plays),(cricket,raju),(plays,raju).
input:
raju plays cricket
output:
cricket plays
cricket raju
plays raju'''


##s=input("Enter a String:").split()
##t=len(s)
##l=[]
##for i in range(t):
##    for j in range(i+1,t):
##        b=sorted([s[i],s[j]])
##        l+=[b]
##l.sort()
##
##for k in l:
##    print(k[0]+" "+k[1])

##import itertools
##s=input("Enter a String:").split()
##s.sort()
##result=itertools.combinations(s,2)
##t=sorted(result)
##for item in t:
##    for i in item:
##        print(i,end=" ")
##    print()
