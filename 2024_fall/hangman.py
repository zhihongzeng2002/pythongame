import random

posWords = ['sigma', 'delaware', 'paper', 'spiral', 'butter']
secret = random.choice(posWords)

guessed = ''
guesses = 5

while guesses > 0:
    g = input("Please guess a letter: ")
    guessed += g
    #check if guess is valid
    if g in secret:
        print("Letter was in the word")

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

    print("The letters guessed so far: " + guessed)

print("Game over")
