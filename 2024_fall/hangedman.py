import random
from hangman_pictures import HANGMANPICS

def getBlanks(word, guessed):
    s = ""
    for i in word:
        if i in guessed:
            s += i
        else:
            s += '_'

    return s

#get random word
wordlist = 'and bear cat dog'.split()
print(wordlist)
w = random.choice(wordlist)

guessed = ''
guessCount = 7

#loop while still have lives left
while guessCount > 0:
    #get input
    print(HANGMANPICS[7 - guessCount])
    print(f'You have {guessCount} guesses left')
    letter = input('Please guess a letter: ').lower()
    if letter in w:
        #already guessed
        if letter in guessed:
            print('That letter has already been guessed')
            continue
        else:
            guessed += letter

            #fill in blanks
            word = getBlanks(w, guessed)

            #check if won
            print(f'Good guess: {word}')
            won = True
            for x in w:
                if x not in guessed:
                    won = False

            if won:
                print('You won!')
                break
    else:
        #fill in blanks
        word = getBlanks(w, guessed)

        print(f'Oops, that letter is not in the word: {word}')
        guessCount -= 1
print('Game Over')
