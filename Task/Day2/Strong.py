m=int(input("Enter Minimum Range:"))
n=int(input("Enter Maximum Range:"))
for num in range(m,n):
    string=str(num)
    strong=0
    for i in string:
        fact=1
        for j in range(1,int(i)+1):
            fact=fact*j
            strong=strong+fact
    if strong ==num:
        print(num)
