def search(puzzle, word, x, y, i):
    #base case
    if (i >= len(word)): #base case if all letters are in grid
        return True
    if (x < 0 or y < 0 or x >= len(puzzle) or y >= len(puzzle[0])): #base case, if we go out of bounds
        return False
    if (word[i] != puzzle[x][y]): #base case, if one of the letters is mismatched
        return False
    
    #general case
    print("letter " + str(i) + " of word: " + word + " is: " + word[i])
    print("letter " + str(x) + ", " + str(y) + " of grid is: " + puzzle[x][y])
    return search(puzzle, word, x + 1, y + 1, i + 1)

puzzle = [["a", "b", "c"], \
          ["a", "b", "c"], \
          ["c", "a", "t"]]

for p in puzzle:
    print(p)

print(search(puzzle, "aaa", 1, 0, 0))