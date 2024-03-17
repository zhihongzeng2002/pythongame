def fact(curr):
    #base case
    if (curr == 1):
        print("reached base case")
        return 1
    
    #general case
    print("doing factorial: " + str(curr) + " x " + str(curr - 1) + "!")
    return curr * fact(curr - 1)

print("factorial of 5 is:")
print(fact(5))