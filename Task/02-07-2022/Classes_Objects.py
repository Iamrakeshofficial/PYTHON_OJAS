'''1.Write a Python class to convert an integer to a roman numeral.'''

##class Myclass():
##    def roman_Num(self,num):
##        val = [1000, 900, 500, 400,100, 90, 50, 40,10, 9, 5, 4,1]
##        Char = ["M", "CM", "D", "CD","C", "XC", "L", "XL","X", "IX", "V", "IV","I"]
##
##        roman=" "
##        i=0
##        while num>0:
##            for j in range(num//val[i]):
##                roman+=Char[i]
##                num-=val[i]
##            i+=1
##        return roman
##n=int(input("Enter a Number to find Roman Value:"))
##print(Myclass().roman_Num(n))
            
##class Myclass():
##    def roman_num(self,num):
##        val=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
##        char=["M", "CM", "D", "CD","C", "XC", "L", "XL","X", "IX", "V", "IV","I"]
##        roman=" "
##        i=0
##        while num>0:
##            for j in range(num//val[i]):
##                roman+=char[i]
##                num-=val[i]
##
##            i+=1
##
##        return roman
##n=int(input("Enter a Number to find Roman Value:"))
##print(Myclass().roman_num(n))
   

'''2. Write a Python class to convert a roman numeral to an integer.'''

##class Myclass:
##    def roman_Num(self,s):
##        d={'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
##        n=0
##
##        for i in range(len(s)):
##            if i>0 and d[s[i]] > d[s[i-1]]:
##                n+=d[s[i]] -2*d[s[i-1]]
##            else:
##                n+=d[s[i]]
##        return n
##
##b=input("Enter Roman Numeral:")
##print(Myclass().roman_Num(b))
                




'''3.Write a Python class to find validity of a string of parentheses, '(', ')', '{', '}', '[' and '].
These brackets must be close in the correct order, for example
"()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid.'''

##class Valid:
##    def abc(str):
##        a=['()','{}','[]']
##
##        while any(i in str for i in  a):
##            for j in a :
##                str=str.replace(j,'')
##        return not str
##s=input("Enter :")
##if Valid.abc(s):
##    print(s,"-is Valid")
##else:
##    print(s,"-Invalid")
##


'''4.Write a Python class to get all possible unique subsets from a set of distinct integers.
Input : [4, 5, 6]
Output : [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]'''

##class Myclass:
##    def f1(self, s1):
##        return self.f2([], sorted(s1))
##
##    def f2(self, curr, s1):
##        if s1:
##            return self.f2(curr, s1[1:]) + self.f2(curr + [s1[0]], s1[1:])
##        return [curr]
##
##
##a = [10,20,30,40]
##print("Subsets: ")
# #print(Myclass().f1(a))


'''5.Write a Python class to find a pair of elements (indices of the two numbers) from a given array whose sum equals a specific target number.

Input: numbers= [10,20,10,40,50,60,70], target=50
Output: 3, 4  '''

##class Myclass(object):
##    def sum(self,nums,target):
##        result=dict()
##        pos=0
##
##        while pos<len(nums):
##            if (target-nums[pos]) not in result:
##                result[nums[pos]]=pos
##                pos+=1
##
##            else:
##                return[result[target-nums[pos]],pos]
##
##
##print(Myclass().sum([10,20,10,40,50,60,70],50))

##class Myclass(object):
##    def sum(self,num,target):
##        result=dict()
##        pos=0
##
##        while pos<len(num):
##            if (target-num[pos]) not in result:
##                result[num[pos]]=pos
##                pos+=1
##
##            else:
##                return[result[target-num[pos]],pos]
##
##
##print(Myclass().sum([10,20,10,40,50,60,70],50))


            

            
        


'''6.Write a Python class to find the three elements that sum to zero from a set of n real numbers.
Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
Output : [[-10, 2, 8], [-7, -3, 10]]  '''


##class Myclass:
##
##    def sum(self,nums):
##        
##        nums=sorted(nums)
##        result=[]
##        i=0
##
##
##        while i < len(nums) - 2:
##            j, k = i + 1, len(nums) - 1
##            while j < k:
##                if nums[i] + nums[j] + nums[k] < 0:
##                    j += 1
##                elif nums[i] + nums[j] + nums[k] > 0:
##                    k -= 1
##                else:
##                    result.append([nums[i], nums[j], nums[k]])
##                    j= j + 1
##                    k=k - 1
##                    while j < k and nums[j] == nums[j - 1]:
##                        j += 1
##                        while j < k and nums[k] == nums[k + 1]:
##                            k -= 1
##            i += 1
##        while i < len(nums) - 2 and nums[i] == nums[i - 1]:
##                  i += 1
##        return result
##
##
##print(Myclass().sum([-25, -10, -7, -3, 2, 4, 8, 10]))




'''7.Write a Python class to implement pow(x, n).'''

##class Myclass:
##    def pow(x,n):
##        return pow(x,n)
##
##
##print(Myclass.pow(2,3))

##class Myclass:
##    def pow(x,n):
##        return pow(x,n)
##
##print(Myclass.pow(2,4))

'''8.Write a Python class to reverse a string word by word. Go to the editor
Input string : 'hello .py'
Expected Output : '.py hello' '''

##class Reverse():
##    def reverse_Words(self,s):
##        return ' '.join(reversed(s.split()))
##
##
##print(Reverse().reverse_Words("hello .py"))

##class Reverse():
##    def reverse_Words(self,s):
##        return ' '.join(reversed(s.split()))
##
##print(Reverse().reverse_Words("hello .py"))


##class  Reverse():
##    def reverse_Words(self,s):
##        return ' '.join(reversed(s.split()))
##
##
##print(Reverse().reverse_Words("hello .py"))




'''9.Write a Python class which has two methods get_String and print_String.
get_String accept a string from the user and print_String print the string in upper case.'''

##class String:
##
##    def __init__(self):
##        self.s=" "
##
##    def get_String(self):
##        self.s=input("Enter a String:")
##
##    def print_String(self):
##        print(self.s.upper())
##
##s=String()
##
##s.get_String()
##s.print_String()
##


##class String:
##    def __init__(self):
##        self.s=" "
##
##    def get_string(self):
##        self.s=input("Enter a String.")
##
##
##    def print_string(self):
##        print(self.s.upper())
##
##
##s=String()
##
##s.get_string()
##s.print_string()




class Teacher(object):
    def __init__(self):
        print("I am from Parent class Constructor.")
        
    def disp(self):
        print("I am a Techer class Method.")

class Student(Teacher):
    def __init__(self):
        print("I am from Child Class Constructor")
    def disp_1(self):
        print("I am Student class Method.")

s=Student()
s.disp_1()






        
        
        



'''10.Write a Python class named Rectangle constructed by a length and width and
a method which will compute the area of a rectangle.'''


##class Rectangle():
##    def __init__(self,l,w):
##        self.length=l
##        self.width=w
##
##    def area(self):
##        return self.length*self.width
##l=int(input("Enter the Length:"))
##w=int(input("Enter the Width:"))
##n=Rectangle(l,w)
##
##print("The Area of The Rectangle Is:",n.area())
        
