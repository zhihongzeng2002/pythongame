import random

BOARDWIDTH = 10
BOARDHEIGHT = 10

class piece():
    #code for piece class goes here
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.display = "X"

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

    def turn(self, x, y):
        self.move(random.randint(-1, 1), random.randint(-1, 1))

class playerPiece(piece):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.display = "O"
    
    def turn(self, x, y):
        self.move(x, y)
    
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
        b[p.y][p.x] = p.display

    return b

def main():
    board = createBoard()

    pieces = []
    pieces.append(playerPiece(0, 0))
    pieces.append(piece(5, 5))
    pieces.append(piece(3, 3))

    board = updateBoard(board, pieces)
    printBoard(board)

    while True:
        ans = input("Where would you like to move? (input as x y) ")
        if ans.upper() == "Q":
            print("Goodbye")
            break

        mov = ans.split()

        for p in pieces:
            p.turn(int(mov[0]), int(mov[1]))
        
        board = updateBoard(board, pieces)
        printBoard(board)
            

if __name__ == "__main__":
    main()
