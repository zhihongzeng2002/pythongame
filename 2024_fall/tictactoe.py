import random

#creates a blank 3x3 board
def createBoard():
    board = [["", "", ""],["", "", ""],["", "", ""]]
    return board

#asks the player to pick a letter
#returns a list containing the player's letter and the computer's letter
def pickLetter():
    pick = input("do you want to be x or o: ")

    #return if player picks x
    if (pick == "x"):
        return ["x", "o"]
    else:
        #return if player picks y
        return ["o", "x"]

#prints the board in a grid format
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

#checks to see if letter has a winning position/three in a row on the board
#returns true if the letter has won, returns false if not
def checkWin(board, letter):
    if (checkRows(board, letter) or checkCols(board, letter)\
        or checkDiag(board, letter)):
        return True
    return False

#gets all the available spaces on the board
#returns a list of all the blank spaces on the board
def getAvailableSpace(board):
    blankSpaces = []
    for x in range(3):
        for y in range(3):
            if board[x][y] != "x" and board[x][y] != "o":
                blankSpaces.append([x, y])
    return blankSpaces

#generates a random move, adds it to the board
def getComputerMove(board, letter):
    x = 0
    y = 0
    while True:
        x = random.randint(0, 2)
        y = random.randint(0, 2)

        blankSpaces = getAvailableSpace(board)

        if [x,y] in blankSpaces or len(blankSpaces) == 0:
            break

    #add the move to the board
    board[x][y] = letter

#get player move
def getPlayerMove(board, letter):
    while True:
        x = int(input("input x coordinate: "))
        y = int(input("input y coordinate: "))

        blankSpaces = getAvailableSpace(board)

        if [x,y] in blankSpaces or len(blankSpaces) == 0:
            break
        else:
            print("not valid space")

    #add the move to the board
    board[x][y] = letter

def tictactoe():
    print("Welcome to TicTacToe!")

    #decide who is x and who is o
    pick = pickLetter()
    player = pick[0]
    computer = pick[1]

    #create board
    board = createBoard()
    printBoard(board)

    #decide who goes first (random)
    turn = random.choice(pick)

    #check for available spaces
    blanks = getAvailableSpaces(board)

    #actual game loop
    while len(blanks) > 0:

        #if player turn, get player move
        if turn == player:
            getPlayerMove(board, player)

        #if computer turn, get computer move
        elif turn == computer:
            getComputerMove(board, computer)

        printBoard(board)

        #check who won
        if checkWin(board, player) == True:
            print("The Player won!")
            break
        elif checkWin(board, computer) == True:
            print("The Computer won!")
            break

        #change turn to the other player
        if turn == "x":
            turn = "o"
        else:
            turn = "x"

        #check for available spaces
        blanks = getAvailableSpaces(board)

        #go back to start of the loop

    print("Game over")
