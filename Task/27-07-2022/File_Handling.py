"""WRITE  A  Text File"""

##f=open("Rakesh.txt",mode="w")
##f.write("Hello Guys.\n")
##f.write("I am Groot.\n")
##f.write("Welcome to the Python World.")
##f.close()
##print("Wrote Successfully")

"""Read a Text File"""

##f=open("Rakesh.txt",mode="r")
##data=f.read()
##print(data)
##f.close()
"""Read a File in binary mode"""

##f=open("Rakesh.txt",mode="rb")
##data=f.read()
##print(data)
##f.close()

"""Check the file Operations in Read MOde"""

##f = open('Rakesh.txt', mode='r', encoding = 'utf-8')
##print('File Name:', f.name)
##print('File Mode:', f.mode)
##print('File Readable:', f.readable())
##print('File Writable:', f.writable())
##print('File Closed:', f.closed)
##f.close()
##print('File Closed:', f.closed)
"""Check the file Operations in Write MOde"""

##f = open('Rakesh.txt', mode='w', encoding = 'utf-8')
##print('File Name:', f.name)
##print('File Mode:', f.mode)
##print('File Readable:', f.readable())
##print('File Writable:', f.writable())
##print('File Closed:', f.closed)
##f.close()
##print('File Closed:', f.closed)

"""Check the file Operations in Append MOde"""

##f = open('Rakesh.txt', mode='a', encoding = 'utf-8')
##print('File Name:', f.name)
##print('File Mode:', f.mode)
##print('File Readable:', f.readable())
##print('File Writable:', f.writable())
##print('File Closed:', f.closed)
##f.close()
##print('File Closed:', f.closed)

"""Check the file Operations in Exclusive Creation MOde(x)
In this Method we can write thw data if file already existed then we get """
##f = open('Rake.txt', mode='x', encoding = 'utf-8')
##print('File Name:', f.name)
##print('File Mode:', f.mode)
##print('File Readable:', f.readable())
##print('File Writable:', f.writable())
##print('File Closed:', f.closed)
##f.close()
##print('File Closed:', f.closed)

"""Read and Write Mode"""

##f = open('Rakesh.txt', mode='r+', encoding = 'utf-8')
##print('File Name:', f.name)
##print('File Mode:', f.mode)
##print('File Readable:', f.readable())
##print('File Writable:', f.writable())
##print('File Closed:', f.closed)
##f.close()
##print('File Closed:', f.closed)

"""Write and Read Mode(w+)
In this mode the existing file data will be overriden with new data."""
##f = open('Rakesh.txt', mode='w+', encoding = 'utf-8')
##f.write("Tarakesh Rao Nagullapali")
##print('File Name:', f.name)
##print('File Mode:', f.mode)
##print('File Readable:', f.readable())
##print('File Writable:', f.writable())
##print('File Closed:', f.closed)
##
##f.close()
##print('File Closed:', f.closed)

##f = open('Rakesh.txt', mode='w+', encoding = 'utf-8')
##data=f.read()
##print(data)
##
##f.close()
"""Append And Read MOde"""

##f = open('Rakesh.txt', mode='a+', encoding = 'utf-8')
##print('File Name:', f.name)
##print('File Mode:', f.mode)
##print('File Readable:', f.readable())
##print('File Writable:', f.writable())
##print('File Closed:', f.closed)
##f.close()
##print('File Closed:', f.closed)

"""Binary ReadMOde"""

##f = open('rakesh.jpg', mode='rb')
##print('File Name:', f.name)
##print('File Mode:', f.mode)
##print('File Readable:', f.readable())
##print('File Writable:', f.writable())
##print('File Closed:', f.closed)
##data=f.read()
##print(data)
##f.close()
##print('File Closed:', f.closed)

"""Binary Write Mode"""

##f=open('rakesh.jpg',mode='wb')
##print(f.name)
##print(f.mode)
##print(f.readable())
##print(f.writable())
##print(f.closed)
l






















