#iterator program

##l=[1,2,3,4,5]
##m=iter(l)
##print(next(m))
##print(next(m))
##print(next(m))
##print(next(m))
##print(next(m))
##print(next(m))

#decorator program

##def fun(a):
##    def fun1():
##        n=int(input())
##        count=0
##        for i in range(1,n+1):
##            if n%i==0:
##                count=count+1
##            if count==2:
##                print("it is prime")
##        else:
##             print("not")
##    return fun1
##@fun
##def fun3():
##    pass
##result=fun(fun3)
##result()
##


#generators program
##def fun():
##    l=["vicky","picky"]
##    for i in l:
##        yield i
##for i in fun():
##    print(i)
##   
##def simple():
##    yield 1
##    yield 2
##    yield 3
##for i in simple():
##    print(next(i))


##class a:
##    def __init__(self,a):
##        self.a=2
##        self._b=b
##    def s(self):
##        print("",self._b)
##b=a()
##b.s()

#multiple program

##class mother:
##    def __init__(self,name):
##        self.name=name
##    def m(self):
##        print("mother class",self.name)
##class father:
##    def __init__(self,age):
##        self.age=age
##    def f(self):
##        print("father",self.age)
##class son(mother,father):
##    def __init__(self,name,age,gender):
##        self.gender=gender
##    def sa(self):
##        mother.__init__(self,name)
##        father.__init__(self,age)
##        print("son",self.gender)
##s=son("uday",34,"male")
##s.m()
##s.f()
##s.sa()
##


#multilevel program


##class grandfather:
##    def __init__(self,a):
##        self.a=a
##    def g(self):
##        print("grand",self.a)
##class father(grandfather):
##    def __init__(self,b):
##        self.b=b
##    def f(self):
##        print("father",self.b)
##class son(father):
##    def __init__():
##

#array
##import array as arr
##a=['i'[1,2,3]]
##b=arr.array(a)
##print(b)


##l=[i for i in range(20) if i%2==0]
##print(l)
##
##
##s={i for i in range(10) if i>5,}
##
##d={1:"priya",2:"vicky"}
##d2


##l=1,2,4
##print(type(l))


##d={"one":{1:"I",2:"II"},"second":{1:"I",2:"II"}}
##d.key()
##print(d)
##
##
##l=[1,2,3]
##for i in l:
##    for i in range(n-1): 
##        for j in range(n+i):
