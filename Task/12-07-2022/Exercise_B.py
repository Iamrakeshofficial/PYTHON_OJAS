"""1) wap to print all elements in nested lists as shown in below
l = [1,2,[3,4,[5,6],7],8]
output = 1 2 3 4 5 6 7 8"""

##l = [1,2,[3,4,[5,6],7],8] 
##
##l1 = []
##
##def remove(l):
##    for i in l:
##        if type(i)==list:
##            remove(i)
##
##        else:
##            l1.append(i)
##
##remove(l)
##print("The all elements in the nested list are:",l1)


"""2) Python code to demonstrate working of
 Convert Nested dictionary to Mapped Tuple
Using list comprehension + generator expression

input:
test_dict = {'gfg' : {'x' : 5, 'y' : 6}, 'is' : {'x' : 1, 'y' : 4},'best' : {'x' : 8, 'y' : 3}}

output:
The grouped dictionary : [(‘x’, (5, 1, 8)), (‘y’, (6, 4, 3))]"""



##dict = {'Rakesh' : {'a' : 10, 'b' : 12}, 'Ramesh' : {'a' : 13, 'b' :40 },'Tarak' : {'a' : 45, 'b' : 3}}
##
##print("The original dictionary is : " + str(dict))
##
##res = [(key, tuple(sub[key] for sub in dict.values()))for key in dict['Rakesh']]
##
##print("\nThe grouped dictionary : " + str(res))




"""3) Convert list of dictionaries to dictionary of lists Using dictionary comprehension.

input:
[{'name': 'sravan', 'subjects': ['java', 'python']},
{'name': 'bobby', 'subjects': ['c/cpp', 'java']},
{'name': 'ojsawi', 'subjects': ['iot', 'cloud']},
{'name': 'rohith', 'subjects': ['php', 'os']},
{'name': 'gnanesh', 'subjects': ['html', 'sql']}]

output:
{'bobby': {'name': 'bobby', 'subjects': ['c/cpp', 'java']},
 'gnanesh': {'name': 'gnanesh', 'subjects': ['html', 'sql']},
 'ojsawi': {'name': 'ojsawi', 'subjects': ['iot', 'cloud']},
 'rohith': {'name': 'rohith', 'subjects': ['php', 'os']},
 'sravan': {'name': 'sravan', 'subjects': ['java', 'python']}}"""


##data = [
##    {'name': 'sravan', 'subjects': ['java', 'python']},
##    {'name': 'bobby', 'subjects': ['c/cpp', 'java']},
##    {'name': 'ojsawi', 'subjects': ['iot', 'cloud']},
##    {'name': 'rohith', 'subjects': ['php', 'os']},
##    {'name': 'gnanesh', 'subjects': ['html', 'sql']}
## 
##]

##dict = {}
##for item in data:
##    name = item['name']
##    dict[name] = item
##
##print(dict)

##print({key: [i[key] for i in data] for key in data[0]})





"""4) Python  code to demonstrate
# Least Frequent Character in String
The original string is :aaabbbcdddrrreeee
The minimum of all characters in aaabbbcdddrrreeee is : c"""

##string=input("Enter a String to find minimum of all charcters:")
##
##
##c = sorted(string)
##print(c)
##for i in c:
##    b = string.count(i)
##    print(b,i)
##    


"""5) wap to modify the existing method in a class after object creation (monkey pacthing)"""
##
##class Teacher(object):
##    def task(self):
##        print("Please Do all  the task and then come back to my class.")
##
##    def show(self):
##        print("I can show my skills.")
##
##t=Teacher()
##def show(self):
##    print("Hello Guys I would Like to see your skill")
##
##Teacher.show=show

##t.show()



























