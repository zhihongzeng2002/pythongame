def madlibs():
    inputFile = "test.txt"
    outputFile = "output.txt"
    
    file = open(inputFile, "r")
    text = file.read()
    words = text.split()
    file.close()

    file = open(outputFile, "w")
    for w in words:
        if w == "(adjective)" or w == "(noun)" or w == "(verb)":
            x = input("please give me a " + w + ":")
            file.write(x + " ")
        else:
            file.write(w + " ")
    file.close()

madlibs()
