import random

BOARDWIDTH = 10
BOARDHEIGHT = 10

class piece():
    #code for piece class goes here
    def __init__(self):
        return

def createBoard():
    return [["_"] * BOARDWIDTH for i in range(BOARDHEIGHT)]

def printBoard(board):
    for i in range(BOARDHEIGHT):
        for j in range(BOARDWIDTH):
            print(board[i][j], end = ' ')
        print()
    print()

def updateBoard(board, pieces):
    b = createBoard()
    for p in pieces:
        print("piece")

    return b

def main():
    board = createBoard()

    pieces = []

    board = updateBoard(board, pieces)
    printBoard(board)

    while True:
        ans = input("Where would you like to move? (input as x y) ")
        if ans.upper() == "Q":
            print("Goodbye")
            break

        board = updateBoard(board, pieces)
        printBoard(board)
            

if __name__ == "__main__":
    main()
