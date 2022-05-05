from random import randint, seed
from time import time
from currencyConverter import clearScreen

def createRandom(ind):
    """
    Select a character based on the random index given, and return a random char according to the section
    """
    seed(time())
    if ind == 1:
        return chr(randint(65,90))
    elif ind == 2:
        return chr(randint(97,122))
    elif ind == 3:
        return str(randint(0,9))
    elif ind == 4:
        return chr(randint(33,47))
    else:
        return '*'

def main():
    print("Welcome to the password generator!!!")
    password = ""
    large = int(input("How many characters do you want to use?: "))
    for i in range(large):
        seed(i)
        ind = randint(1,4)
        password += createRandom(ind)
    print("The created password is " + password)
    large = input("Type enter to delete it, after you save it...")
    password = " "
    clearScreen()
    print("Thanks for using the program...")

if __name__ == '__main__':
    main()

    