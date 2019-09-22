import random
import sys

print('Hello! What is your name?')
myName = input()

number = random.randint(1, 20)
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')

for i in range(6):
    guess = int(input('Take a guess. '))

    if guess == number:
        print('Good job, ' + myName + '! You guess my number in ' + str(i+1) + ' guesses!')
        sys.exit(0)

    elif guess < number:
        print('Your guess is too low.')

    else:
        print('Your guess is too high.')

print('Nope. The number I was thinking of was ' + str(number))
