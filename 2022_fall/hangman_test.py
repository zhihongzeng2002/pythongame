from hangman import *

print(choose_word())
print(choose_word())

ans = is_word_guessed('beer', 'bre')
assert ans == True, 'fail is word guessed did not return True'

ans = is_word_guessed('beer', 'br')
assert ans == False, 'fail function did not return False'

ans = get_guessed_word('hangman', 'han')
assert ans == '_an__an', 'fail, function did not return correct blanks'