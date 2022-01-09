import numpy as np
import random
import copy

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

def get_player_move(board, letter):
    height, width = board.shape
    available_move = get_available_move(board)
    move = (-1, -1)
    while move not in available_move:
        ans = input(f'What is your next move (0-{height-1}, 0-{width-1})?')
        print(ans)
        move = ans.split(',')
        print(move)
        move = [int(move[0]), int(move[1])]
        print(move)
        print(move in get_available_move(board))
    make_move(board, letter, move)

def tictactoe(size=3):
    print('Welcome to Tic Tac Toe')
    player, computer = input_player_selection()
    print(f'you are {player} and the computer is {computer}')
    first = who_go_first()
    print(f'{first} goes first')
    board = create_board(size, '')
    turn = first
    #print(board)
    #print(get_available_move(board))

    while get_available_move(board):
        if turn == 'player':
            get_player_move(board, player)
            print(board)
            turn = 'computer'
            if game_won(board, player):
                print('congratulations, you won')
                return
        else:
            get_random_move(board, computer)
            print(board)
            turn = 'player'
            if game_won(board, computer):
                print('the computer has won the game')
                return
    print('the game is a tie')

def get_win_defense_move(board, letter, available_move, win_defense_flag):
    if win_defense_flag:
        target = letter
    else:
        if letter == 'O':
            target = 'X'
        else:
            target = 'O'

    for move in available_move:
        board_clone = copy.deepcopy(board)
        make_move(board_clone, target, move)
        if game_won(board_clone, target):
           make_move(board, letter, move)
           return True
    return False

def get_smart_move(board, letter):
    available_move = get_available_move(board)
    win_move = get_win_defense_move(board, letter, available_move, True)
    if win_move:
        return True
    return get_win_defense_move(board, letter, available_move, False)

def get_prefered_random_move(board, letter):
    available_move = get_available_move(board)
    height, width = board.shape
    prefered_move = [[int(height/2), int(width/2)], [0, 0], [0, width-1], [height-1, 0], [height-1, width-1]]
    move = None
    for p in prefered_move:
        if p in available_move:
            move = p
            break
    if move is None:
        move = random.choice(available_move)
    make_move(board, letter, move)

def tictactoe_smart(size = 3):
    print('Welcome to Tic Tac Toe')
    player, computer = input_player_selection()
    print(f'you are {player} and the computer is {computer}')
    first = who_go_first()
    print(f'{first} goes first')
    board = create_board(size, '')
    turn = first

    while get_available_move(board):
        if turn == 'player':
            print(get_available_move(board))
            get_player_move(board, player)
            print(board)
            turn = 'computer'
            if game_won(board, player):
                print('congratulations, you won')
                return
        else:
            if not get_smart_move(board, computer):
                get_prefered_random_move(board, computer)
            print(board)
            turn = 'player'
            if game_won(board, computer):
                print('the computer has won the game')
                return
    print('the game is a tie')

if __name__ == '__main__':
    tictactoe_smart()

