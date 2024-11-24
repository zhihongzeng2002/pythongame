import random

"""
generate number
Loop:
    Ask for guess
    check for clues
    if all digits are correct, exit
    if run out of guesses, exit
end game
"""

#get secret number
def get_number():
    dig = list("1234567890")
    random.shuffle(dig)
    return dig[:3]

#get answer
def get_guess():
#    valid = False
#    while True:
#        x = input()
#        allDigits = True
#        while i in x:
#            if i not in "1234567890":
#                allDigits = False
#        if len(x) == 3 and allDigits:
#            break
#
#    return x
    return input("Give me a three digit number")
#put some kind of check to make sure it is a 3 digit number

#check answer

"""
bagels - none are correct
Pico - one is correct but in the wrong place
fermi - one is correct and in the right place

arguments:
guess - string of 3 digits
secret - list of numbers
"""

def get_clue(guess, secret):
    if guess == "".join(secret):
        return "won"
    
    clues = []
    clueDict = {}
    
    for i in range(len(secret)):
        clueDict[i] = secret[i]

    for i in range(len(guess)):
        if guess[i] == clueDict[i]:
            clues.append("fermi")
        elif guess[i] in secret:
            clues.append("Pico")

    if len(clues) == 0:
        return "Bagels"
    else:
        return "".join(clues)

#the whole game
def bagels():
    x = """
bagels - none are correct
Pico - one is correct but in the wrong place
fermi - one is correct and in the right place

arguments:
guess - string of 3 digits
secret - list of numbers
"""
    print(x)
    secret = get_num()

    for i in range(3):
        guess = get_guess()
        clue = get_clue(guess, secret)
        if clue == "won":
            print("you win")
            return
        print(clue)

    print("you have no guesses left")
    return
