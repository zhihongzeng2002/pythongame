import random
from hangman_pictures import HANGMANPICS

def choose_word():
    wordlist = 'ant bear cat dog beer'.split(' ')
    print(wordlist)
    w = random.choice(wordlist)
    return w

def is_word_guessed(secret_word, letters_guessed):
    for x in secret_word:
        if x not in letters_guessed:
            return False
    return True

def get_guessed_word(secret_word, letters_guessed):
    word = ''
    for x in secret_word:
        if x in letters_guessed:
            word += x
        else:
            word += '_'
    return word

def guess_loop(secret_word, max_guess):
    guessed = ''
    while max_guess > 0:
        print(f'you have {max_guess} guesses left')
        letter = input('Please guess a letter: ').lower()
        if letter in secret_word:
            if letter in guessed:
                print('that letter has already been guessed')
                continue
            else:
                guessed += letter
                guessed_word = get_guessed_word(secret_word, guessed)
                print(f'Good guess: {guessed_word}')
                if is_word_guessed(secret_word, guessed):
                    print('Congratulations, you win!')
                    return
        else:
            guessed_word = get_guessed_word(secret_word, guessed)
            print(f'That letter is not in the word: {guessed_word}')
            max_guess -= 1
    print('Sorry, you ran out of guesses.')

def guess_loop_pics(secret_word): #
    max_guess = len(HANGMANPICS) #
    guessed = ''
    while max_guess > 1: #
        print(f'you have {max_guess - 1} guesses left') #
        print(HANGMANPICS[-max_guess]) #
        letter = input('Please guess a letter: ').lower()
        if letter in secret_word:
            if letter in guessed:
                print('that letter has already been guessed')
                continue
            else:
                guessed += letter
                guessed_word = get_guessed_word(secret_word, guessed)
                print(f'Good guess: {guessed_word}')
                if is_word_guessed(secret_word, guessed):
                    print('Congratulations, you win!')
                    return
        else:
            guessed_word = get_guessed_word(secret_word, guessed)
            print(f'That letter is not in the word: {guessed_word}')
            max_guess -= 1
    print(HANGMANPICS[-1]) #
    print('Sorry, you ran out of guesses.')

def hangman(max_guess):
    secret_word = choose_word()
    print('Welcome to the game')
    guess_loop_pics(secret_word)

if __name__ == '__main__':
    hangman(5)
