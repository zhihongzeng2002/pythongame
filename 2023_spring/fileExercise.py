#if you are looking for the madlibs code, it should be in madlibs2.py
#this is the exercise code

file = open("letters.txt")

x = file.readlines()

for i in x:
    print(i)

file.seek(0)

x = file.read(5)
print(x)
file.seek(0)

x = file.read()
print(x)

file.close()

file = open("output.txt", "w")
file.write("abc\n")

i = ["1", "2", "3", "\n", "hello world"]
file.writelines(i)

file.close()