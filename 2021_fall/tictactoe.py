import numpy as np
import random

def create_board(size, value = ''):
    board = np.full((size, size), value)
    return board

def input_player_selection():
    letter = ''
    while letter not in ['X', 'O']:
        letter = input('Do you want to be X or O? ')
        letter = letter.upper()
    if letter == 'X':
        return ['X' , 'O']
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

def column_won(board, letter):
    height, width = board.shape
    for x in range(width):
        won = True
        for y in range(height):
            if board[y, x] != letter:
                won = False
                break
        if won:
            return True
    return False

def row_won(board, letter):
    height, width = board.shape
    for y in range(height):
        won = True
        for x in range(width):
            if board[y, x] != letter:
                won = False
                break
        if won:
            return True
    return False

def diag_won(board, letter):
    height, width = board.shape
    won = True
    for y in range(height):
        if board[y, y] != letter:
            won = False
            break
    if won:
        return True

    won = True
    for y in range(height):
        if board[y, height - 1 - y] != letter:
            won = False
            break

    return won

def game_won(board, letter):
    return column_won(board, letter) or row_won(board, letter) or diag_won(board, letter)

def get_available_move(board):
    height, width = board.shape
    move = []
    for y in range(height):
        for x in range(width):
            if board[y, x] == '':
                move.append([y,x])
    return move

def get_random_move(board, letter):
    print('computer move')
    available_move = get_available_move(board)
    move = random.choice(available_move)
    make_move(board, letter, move)
