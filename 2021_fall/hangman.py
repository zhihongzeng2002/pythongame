import random

def choose_word():
    wordlist = 'ant bear cat dog beer'.split(' ')
    print(wordlist)
    w = random.choice(wordlist)
    return w

def is_word_guessed(secrete_word, letter_guessed):
    for x in secrete_word:
        if x not in letter_guessed:
            return False
    return True

def get_guessed_word(secrete_word, letter_guessed):
    word = ''
    for x in secrete_word:
        if x in letter_guessed:
            word += x
        else:
            word += '_'
    return word

def guess_loop(secrete_word, max_guess):
    guessed = ''
    while max_guess > 0:
        print(f'You have {max_guess} guessed left')
        letter = input('Please guess a letter: ').lower()
        if letter in secrete_word:
            if letter in guessed:
                print('That letter has already been guessed')
            else:
                guessed += letter
                guessed_word = get_guessed_word(secrete_word, guessed)
                print(f'Good guess: {guessed_word}')

                if is_word_guessed(secrete_word, guessed):
                    print('Congrats, you won.\n')
                    return

        else:
            guessed_word = get_guessed_word(secrete_word, guessed)
            print(f'Oops. That letter is not in my word: {guessed_word}')
            max_guess -= 1
    print(f'Sorry, you ran out of guesses. My word is {secrete_word}')

from hangman_pictures import HANGMANPICS

def guess_loop_2(secrete_word): ###
    max_guess = len(HANGMANPICS) ###
    guessed = ''
    while max_guess > 1:  ###
        print(f'You have {max_guess-1} guessed left') ###
        print(HANGMANPICS[-max_guess])  ###
        letter = input('Please guess a letter: ').lower()
        if letter in secrete_word:
            if letter in guessed:
                print('That letter has already been guessed')
            else:
                guessed += letter
                guessed_word = get_guessed_word(secrete_word, guessed)
                print(f'Good guess: {guessed_word}')

                if is_word_guessed(secrete_word, guessed):
                    print('Congrats, you won.\n')
                    return

        else:
            guessed_word = get_guessed_word(secrete_word, guessed)
            print(f'Oops. That letter is not in my word: {guessed_word}')
            max_guess -= 1
    print(HANGMANPICS[-1])  ###
    print(f'Sorry, you ran out of guesses. My word is {secrete_word}')

            
def hangman(): ###
    secrete_word = choose_word()
    print('Welcome the game')
    guess_loop_2(secrete_word)   ###

if __name__ == '__main__':
    hangman()

    
            

