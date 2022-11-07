import numpy as np

def create_board(size, value = ''):
    board = np.full((size, size), value)
    return board
