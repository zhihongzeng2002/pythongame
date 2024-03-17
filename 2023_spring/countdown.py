def countdown_iteration (count):
    for i in range(count, 0, -1):
        print(i)

def countdown_recursion (count):
    if (count == 0): #base case
        return

    #gerneral case
    countdown_recursion(count - 1)
    print(count)

countdown_recursion(10)