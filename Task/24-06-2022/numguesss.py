import random
n=random.randint(1,99)

print(n)
count=0
while n!="guess":
    if count==5:
        print("You Lost the Game")
        break
    guess=int(input("Enter a Number between 1 to 99:"))
    if guess<n:
        print("Guess is Low")

    elif guess>n:
        print("Guess is High")

    else:
        print("You Guessed it.")
        break
    count+=1
