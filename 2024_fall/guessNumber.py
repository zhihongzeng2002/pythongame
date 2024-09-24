import random
x = random.randint(1,20)
for i in range(5):
    a = int(input("what number am I thinking of?"))
    if (a == x):
        print("you got it!")
        break
    elif (a < x):
        print("Guess is too low")
    else:
        print("guess is too high")

if a != x:
    print("better luck next time!")

