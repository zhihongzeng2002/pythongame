from tictactoe import *

print('\n---Test create_board\n')
print(create_board(3, ' '))
print(create_board(2, 5))
print(create_board(4))

print('\n----Test who_go_first\n')
print(who_go_first())
print(who_go_first())
print(who_go_first())

print('\n----Test make_move\n')
board = create_board(3)
make_move(board, 'X', (0, 0))
print(board)
make_move(board, 'O', (2, 2))
print(board)

print('\n-----Test colu,mn_won\n')
board = create_board(3)
print(board)
ans = column_won(board, 'X')
print(ans)

board[0, 0] = 'X'
board[1, 0] = 'X'
board[2, 0] = 'X'
print(board)
ans = column_won(board, 'X')
print(ans)


print('\n----Test row_won\n')
board = create_board(3)
print(board)
ans = row_won(board, 'X')
print(ans)

board[0, 0] = 'X'
board[0, 1] = 'X'
board[0, 2] = 'X'
print(board)
ans = row_won(board, 'X')
print(ans)

print('\n----Test diag_won\n')
board = create_board(3)
print(board)
ans = diag_won(board, 'X')
print(ans)

board[0, 0] = 'X'
board[1, 1] = 'X'
board[2, 2] = 'X'
print(board)
ans = diag_won(board, 'X')
print(ans)

board = create_board(3)
board[0, 2] = 'X'
board[1, 1] = 'X'
board[2, 0] = 'X'
print(board)
ans = diag_won(board, 'X')
print(ans)

print('\n-----Test game_won\n')
board = create_board(3)
print(board)
ans = game_won(board, 'X')
print(ans)

board[0, 0] = 'X'
board[1, 0] = 'X'
board[2, 0] = 'X'
print(board)
ans = game_won(board, 'X')
print(ans)

print('\n ----- Test get_available_move\n)')
board = create_board(3)
board[0,0] = 'X'
board[1,1] = 'O'
board[2,2] = 'defewasxfewd'
ans = get_available_move(board)
print(board)
print('avaialable_moves: {}'.format(ans))

print('\n=-----get random move\n')
board = create_board(3)
get_random_move(board, 'O')
print(board)

get_random_move(board, 'O')
print(board)
