from tictactoe import *

x = createBoard()
print(x)

printBoard(x)
print(getAvailableSpace(x))

#a = pickLetter()
#print(a)
#a = pickLetter()
#print(a)


print(checkRows(x, "x"))
print(checkRows(x, "o"))

x = [["x", "x", "x"],["", "", ""],["o", "o", "o"]]
printBoard(x)
print(checkWin(x, "x"))
print(checkWin(x, "o"))

x = [["x", "o", "x"],["", "", ""],["o", "o", "o"]]
printBoard(x)
print(checkWin(x, "x"))

x = [["x", "x", "o"],["x", "", "o"],["x", "o", "o"]]
printBoard(x)
print(checkWin(x, "x"))
print(checkWin(x, "o"))

x = [["x", "o", "x"],["", "", ""],["o", "o", "o"]]
printBoard(x)
print(checkWin(x, "x"))
print(getAvailableSpace(x))

x = [["x", "o", "x"],["", "x", ""],["o", "o", "x"]]
printBoard(x)
print(checkWin(x, "x"))
print(getAvailableSpace(x))

x = [["x", "o", "o"],["", "o", ""],["o", "o", "o"]]
printBoard(x)
print(checkWin(x, "o"))


x = createBoard()
print(getAvailableSpace(x))
getComputerMove(x, "o")
getComputerMove(x, "o")
getComputerMove(x, "o")
printBoard(x)
