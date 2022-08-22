##import re
##string='hello 12  hi 89.Howdy 34'
##pattern='\d+'
##result=re.findall(pattern,string)
##print(result)

##import re
##string='twelve:12 Eighty nine:89'
##pattern='\d+'
##result=re.split(pattern,string)
##print(result)

'''1.Write a Python program to check that a string contains
only a certain set of characters (in this case a-z, A-Z and 0-9).'''

import re
pattern='\w'
string='Vaddepa 123 RAkesh'
string2='Vadde@pa 23%$ Akweasd'
result=re.search(pattern,string)
print(result)
