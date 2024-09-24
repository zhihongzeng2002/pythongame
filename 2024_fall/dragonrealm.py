import random
x = ""

while x != "no":
    a = random.randint(1,3)

    b = 0
    while not (b > 0 and b < 4):
        b = int(input("Which cave would you like to enter?"))

    if (b == a):
        print("you win!")
    elif (b < a):
        print("you lose")
    else:
        print("you ultra lose")

    x = input("Do you want to play again?")
    
