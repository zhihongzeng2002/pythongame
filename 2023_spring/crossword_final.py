def searchDirection(puzzle, word, x, y, h, v, i):
    if (i >= len(word)): #base case, we finished checking the word
        return True
    if (x >= len(puzzle[0]) or x < 0 or y >= len(puzzle) or y < 0): #base case, out of bounds
        return False
    if (puzzle[y][x] != word[i]): #base case, letter mismatch
        return False
    
    return searchDirection(puzzle, word, x + h, y + v, h, v, i + 1)

def searchWord(puzzle, word):
    for y in range(len(puzzle)): #loop through every letter in the grid
        for x in range(len(puzzle[0])): #check right, down, left, up directions
            if (searchDirection(puzzle, word, x, y, 0, 1, 0) or \
            searchDirection(puzzle, word, x, y, 1, 0, 0) or \
            searchDirection(puzzle, word, x, y, 0, -1, 0) or \
            searchDirection(puzzle, word, x, y, -1, 0, 0)):
                return True
    return False #if searched through entire grid, and word wasn't found, return false

puzzle = [["a", "b", "c"], \
          ["a", "b", "c"], \
          ["c", "a", "t"]]

for p in puzzle:
    print(p)

print(searchWord(puzzle, "aaa"))