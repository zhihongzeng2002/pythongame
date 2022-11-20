from tictactoe import *

print('----Test create board fuction\n')
board = create_board(3, ' ')
print(board)

# print('----Test input player selection\n')
# print(input_player_selection())

print('----Test who goes first\n')
print(who_go_first())
print(who_go_first())
print(who_go_first())

print('----Test making a move\n')
make_move(board, 'X', (0, 0))
print(board)
make_move(board, 'O', (2, 2))
print(board)

print('----Test get available move\n')
board[1,1] = 'O'
board[1,2] = 'X'
board[0,1] = 'O'
ans = get_available_move(board)
print(board)
print('available moves: {}'.format(ans))

# print('----Test get player move\n')
# board = create_board(3, ' ')
# print(board)
# get_player_move(board, 'E')
# print(board)
# get_player_move(board, 'E')
# print(board)

print('\n------- Test get_random_move')
board = create_board(3)
get_random_move(board, 'O')
print(board)

board = create_board(3)
get_random_move(board, 'O')
print(board)