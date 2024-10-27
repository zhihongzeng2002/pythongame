def createBoard():
    board = [["", "", ""],["", "", ""],["", "", ""]]
    return board

def pickLetter():
    pick = input("do you want to be x or o: ")

    #return if player picks x
    if (pick == "x"):
        return ["x", "o"]
    else:
        #return if player picks y
        return ["o", "x"]

def printBoard(board):
    for row in board:
        print(row)

def checkRow(board, row, letter):
    won = True
    for x in range(3):
        if board[row][x] != letter:
            won = False

    return won

def checkRows(board, letter):
    for row in range(3):
        won = checkRow(board, row, letter)
        if won == True:
            return True

    return False

def checkCol(board, col, letter):
    won = True
    for x in range(3):
        if board[x][col] != letter:
            won = False

    return won

def checkCols(board, letter):
    for col in range(3):
        won = checkCol(board, col, letter)
        if won == True:
            return True

    return False

def checkDiag(board, letter):
    won = True
    for i in range(3):
        if board[i][i] != letter:
            won = False

    if won == True:
        return won

    won = True
    for i in range(3):
        if board[i][2-i] != letter:
            won = False

    return won

def checkWin(board, letter):
    if (checkRows(board, letter) or checkCols(board, letter)\
        or checkDiag(board, letter)):
        return True
    return False
