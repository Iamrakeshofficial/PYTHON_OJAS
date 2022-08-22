import datetime
date=input()
x=datetime.datetime.strptime(date,"%d-%m-%y")
print(x)
x=x.strftime("%d-%m")
print(x)
