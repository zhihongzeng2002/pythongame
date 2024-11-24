import random

num_digit = 3
max_guess = 10

def introduction():
    print(f"""I am thinking of a {num_digit} number.
You have {max_guess} guesses to get it. The clues are:
Bagels: none of the digits are correct
Pico: one digit is correct, but in the wrong place
Fermi: one digit is correct is correct and in the right position""")

def get_random_num(size):
    nums = list(range(1,10))
    random.shuffle(nums)
    ans = ""
    for x in nums[:size]:
        ans += str(x)
    return ans

def secret_set(secret):
    secret_set = set()
    for i in secret:
        secret_set.add(i)

    return secret_set

def secret_dict(secret):
    ind = {}
    for i in range(len(secret)):
        ind[i] = secret[i]

    return ind

def get_input(size):
    ans = ""
    while len(ans) != size or not ans.isdigit():
        ans = input(f"Guess a {size} digit number: ")
    return ans

def get_clue(guess, secret, secretDict, secretSet):
    if guess == secret:
        return "won"

    clue = []
    for i in range(len(guess)):
        if guess[i] == secretDict[i]:
            clue.append("fermi")
        elif guess[i] in secretSet:
            clue.append("Pico")

    if not clue:
        return "bagels"
    else:
        return "".join(clue)

def bagels():
    introduction()

    secret = get_random_num(num_digit)
    secretSet = secret_set(secret)
    secretDict = secret_dict(secret)

    for i in range(max_guess):
        print(f"Guess {i + 1}")
        ans = get_input(num_digit)
        clue = get_clue(ans, secret, secretDict, secretSet)

        if clue == "won":
            print("You guessed the number!")
            return
        else:
            print(clue)

    print(f"You ran out of guesses, the number was {secret}")

if __name__ == "__main__":
    bagels()
