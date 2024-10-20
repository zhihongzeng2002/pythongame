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
