import random

BOARDWIDTH = 10
BOARDHEIGHT = 10

class piece():
    def __init__(self, x = 0, y = 0, display = "O"):
        self.x = x
        self.y = y
        self.display = display
    def clamp(self):
        if self.x < 0:
            self.x = 0
        elif self.x >= BOARDWIDTH:
            self.x = BOARDWIDTH - 1
        if self.y < 0:
            self.y = 0
        elif self.y >= BOARDHEIGHT:
            self.y = BOARDHEIGHT - 1
    def move(self, xMove, yMove):
        self.x += xMove
        self.y += yMove
        self.clamp()

class playerPiece(piece):
    def __init__(self, x = 0, y = 0):
        super().__init__(x, y, "X")
    def takeTurn(self, pos):
        self.move(int(pos[0]), int(pos[1]))

class enemyPiece(piece):
    def __init__(self, x = 0, y = 0):
        super().__init__(x, y, "E")
    def takeTurn(self, pos):
        self.move(random.randint(-1, 1), random.randint(-1, 1))

class horizontalPiece(enemyPiece):
    def clamp(self):
        if self.x < 0:
            self.x = BOARDWIDTH - 1
        elif self.x >= BOARDWIDTH:
            self.x = 0
    def takeTurn(self, pos):
        self.move(1, 0)

class verticalPiece(enemyPiece):
    def clamp(self):
        if self.y < 0:
            self.y = BOARDHEIGHT - 1
        elif self.y >= BOARDHEIGHT:
            self.y = 0
    def takeTurn(self, pos):
        self.move(0, 1)

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
    for i in range(2):
        pieces.append(enemyPiece(random.randint(0, 9), random.randint(0, 9)))
    pieces.append(horizontalPiece(5, 5))
    pieces.append(verticalPiece(5, 5))
    

    board = updateBoard(board, pieces)
    printBoard(board)

    while True:
        ans = input("Where would you like to move? (input as x y) ")
        if ans.upper() == "Q":
            print("Goodbye")
            break

        pos = ans.split()
        for p in pieces:
            p.takeTurn(pos)

        board = updateBoard(board, pieces)
        printBoard(board)
            

if __name__ == "__main__":
    main()
