import random
from hangman_pictures import HANGMANPICS

def blankSpace(s, g):
    out = ''
    
    for x in s:
        if x in g:
            out += x
        else:
            out += "_"

    return out

posWords = ['sigma', 'delaware', 'paper', 'spiral', 'butter']
secret = random.choice(posWords)

guessed = ''
guesses = 7

while guesses > 0:
    print("Number of guesses left: " + str(guesses))
    print(HANGMANPICS[7 - guesses])
    
    g = input("Please guess a letter: ")
    guessed += g
    #check if guess is valid
    if g in secret:
        print("Letter was in the word")

        #print out the blanks
        out = blankSpace(secret, guessed)
                
        print(out)

        #check if all letters in word have been guessed
        won = True
        for x in secret:
            if x not in guessed:
                won = False

        if won:
            print("You guessed the word!")
            break
            
    else:
        print("Letter was not in the word")
        guesses -= 1

        #print out the blanks
        out = blankSpace(secret, guessed)
                
        print(out)

    print("The letters guessed so far: " + guessed)

print("Game over")
