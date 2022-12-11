import numpy as np
import random

def create_board(size, value = ' '):
    board = np.full((size, size), value)
    return board

def input_player_selection():
    letter = ''
    while letter not in ['X', 'O']:
        letter = input('Do you want to be X or O? ').upper()
    
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
        #print(available_move)
        ans = input(f'What is your next move (0-{height-1}, 0-{width-1})?')
        move = ans.split(',')
        move = [int(move[0]), int(move[1])]
        #print(move)
    
    make_move(board,letter,move)

def get_random_move(board, letter):
    print('computer move')
    available_move = get_available_move(board)

    #print(available_move)
    move = random.choice(available_move)
    make_move(board, letter, move)

def row_won(board, letter):
    height, width = board.shape
    for x in range(height):
        won = True
        for y in range(width):
            if board[x, y] != letter:
                won = False
                break
        if won:
            return True
    return False

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

def diag_won(board, letter):
    height, width = board.shape
    won = True
    for y in range(height):
        if board[y,y] != letter:
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
    return column_won(board, letter) or \
        row_won(board, letter) \
        or diag_won(board, letter)

def tictactoe(size = 3):
    print('Welcome to Tic Tac Toe!')
    player, computer = input_player_selection()
    print(f'you are {player}, and computer is {computer}')

    first = who_go_first()
    print(f'{first} will go first')

    board = create_board(size, ' ')

    turn = first

    while get_available_move(board):
        if turn == 'player':
            get_player_move(board, player)
            print(board)
            turn = 'computer'

            if game_won(board, player):
                print('You won the game.')
                return
        else:
            get_random_move(board, computer)
            print(board)
            turn = 'player'

            if game_won(board, computer):
                print('The computer won the game.')
                return
    
    print('The game is now over')

if __name__ == '__main__':
    tictactoe()