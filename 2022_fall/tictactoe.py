import numpy as np
import random

def create_board(size, value = ''):
    board = np.full((size, size), value)
    return board

def input_player_selection():
    letter = ''
    while letter not in ['X', 'O']:
        letter = input('Do you want to be X or O?').upper()
    
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def who_go_first():
    ans = random.randint(0,1)
    if ans:
        return 'computer'
    else:
        return 'player'

def make_move(board, letter, position):
    board[position[0], position[1]] = letter

def get_available_move(board):
    height, width = board.shape
    move = []
    for y in range(height):
        for x in range(width):
            if board[y, x] == ' ':
                move.append([y, x])
    return move

def get_player_move(board, letter):
    height, width = board.shape
    available_move = get_available_move(board)
    move = (-1, -1)

    while move not in available_move:
        ans = input(f'What is your next move (0-{height-1}, 0-{width-1})?')
        move = ans.split(',')
    
    make_move(board,letter,move)