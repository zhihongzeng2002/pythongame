def madlibs():
    inputFile = "test.txt"
    outputFile = "output.txt"
    
    file = open(inputFile, "r")
    text = file.read()
    words = text.split()
    file.close()

    file = open(outputFile, "w")
    for w in words:
        #if w is (adjective) or (noun) or (verb)
            #ask for w and write it
        #else
            file.write(w + " ")
    file.close()

madlibs()
