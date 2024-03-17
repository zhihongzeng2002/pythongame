def getList(inputStr):
    w = inputStr.split()
    return w

def lib(output, words):
    l = len(words)
    i = 0
    wordCheck = ["(plural-noun)", "(noun)", "(adjective)", "(verb)"]

    while(i < l):
        if(words[i] in wordCheck):
            w = input("Input a " + words[i] + ": ")
            output.write(w + " ")
            i += 1
        else:
            output.write(words[i] + " ")
            i += 1

if __name__ == "__main__":
    inputFile = "madlibs.txt"
    outputFile = "output.txt"
    
    file = open(inputFile, "r")
    words = getList(file.read())
    file.close()

    file = open(outputFile, "w")
    lib(file, words)
    file.close()