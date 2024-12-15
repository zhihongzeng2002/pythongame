def madlibs():
    inputFile = "test.txt"
    
    file = open(inputFile, "r")
    text = file.read()
    words = text.split()
    file.close()

    print(words)

madlibs()
