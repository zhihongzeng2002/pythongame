import numpy as np
import random

def create_board(size, value=''):
    board = np.full((size, size), value)
    return board

def input_player_selection():
    letter = ''
    while letter not in ['X', 'O']:
        letter = input('Do you want to be X, or O? ')
        letter = letter.upper()
    
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']
    
def who_go_first():
    ans = random.randint(0, 1)
    if ans:
        return 'computer'
    else:
        return 'player'

def make_move(board, letter, position):
    board[position[0], position[1]] = letter