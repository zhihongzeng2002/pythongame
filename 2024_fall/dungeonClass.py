import random

BOARDWIDTH = 10
BOARDHEIGHT = 10

class piece():
    #code for piece class goes here
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x = self.clamp(self.x + x, 0, 9)
        self.y = self.clamp(self.y + y, 0, 9)

    def clamp(self, i, minVal, maxVal):
        if i < minVal:
            return minVal
        elif i > maxVal:
            return maxVal
        else:
            return i

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
        b[p.y][p.x] = "X"

    return b

def main():
    board = createBoard()

    pieces = []
    pieces.append(piece(0, 0))
    pieces.append(piece(5, 5))
    pieces.append(piece(3, 3))

    board = updateBoard(board, pieces)
    printBoard(board)

    while True:
        ans = input("Where would you like to move? (input as x y) ")
        if ans.upper() == "Q":
            print("Goodbye")
            break

        mov = [1, 1]

        for p in pieces:
            p.move(random.randint(-1, 1), random.randint(-1, 1))
        
        board = updateBoard(board, pieces)
        printBoard(board)
            

if __name__ == "__main__":
    main()
