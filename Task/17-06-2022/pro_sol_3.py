'''Given a string S and a character C (as string of length 1), return a string with the characters surrounding any occurrence of C reversed. 
For example, if S is "Hello beautiful world" and C is a space, return "Hellb oeautifuw lorld" 

take input as a string with many words,seperated by spaces,swap the last character of 1st word and 1st character of the next word.

hint: split the string into a list and loop the list and write if condition for whitespaces where occured,
if condition is True then swap the last character of the word
with 1st character of the next word. 

ex1: input=" ravi teja kumar"
    output="ravt iejk aumar"

ex2: input="happy new year" 
    output:happn yey wear" '''

##st = list('hello beautiful world')
##s = " "
##st1 = []
##for i in range(len(st)):
##  if st[i] == s:
##    st1.pop(i-1)
##    st[i-1],st[i+1] = st[i+1],st[i-1]
##    st1.append(st[i-1])
##    st1.append(s)
##    st1.append(st[i+1])
##    st1.pop(i+1)
##  else:
##    st1.append(st[i])
##print(''.join(st1))

