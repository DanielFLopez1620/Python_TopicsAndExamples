"""
Author: Daniel Lopez
Info from:
  1) https://platzi.com/cursos/python-cs/
"""

from turtle import clear
from currencyConverter import clearScreen


def exhaustiveEnumeration(obj):
    """
    It is called "guess and check"
    Here you want to check an objective, that is find the square root using
    multiplication.
    """
    answer = 0
    while answer**2 == obj:
        answer += 1
    if answer**2 == obj:
        return answer
    else:
        print("The square root wasn't found with exhaustive enumeration....")
        return None


def aproximationOfSolutions(obj):
    """
    Aproximation using an 'epsilon', which have an error range.
    Here we use it to find the square root using multiplication.
    """
    epsilon = 0.01
    step = epsilon**2
    answer = 0.0
    while abs(answer**2 - obj) >= epsilon and answer <= obj:
        answer += step
    if abs(answer**2 - obj) >= epsilon:
        print("The square root wasn't found with aproximation of solutions.")
        return None
    else:
        return answer


def BinarySearch(obj):
    """
    Efficient method for searching results while it cuts the range of
    iteration by two.
    Here we used to find the square root of a number.
    """
    epsilon = 0.001
    down = 0.0
    up = max(1.0, obj)
    answer = (up + down) / 2
    while abs(answer**2 - obj) >= epsilon:
        if answer**2 < obj:
            down = answer
        else:
            up = answer
        answer = (up + down) / 2
    return answer


def searchMenu():
    """
    Prints the available methods of search
    """
    print("---------------------------------")
    print("|      Available searches       |")
    print("---------------------------------")
    print("| 1) Exhaustive Enumeration     |")
    print("| 2) Aproximation of Solution   |")
    print("| 3) Binary Search              |")
    print("| 4) Exit program               |")
    print("---------------------------------")


def main():
    while True:
        searchMenu()
        value = int(input("Type an option of search: "))
        obj = float(input("Which number are you searching for? The sqrt of:"))
        clearScreen()
        if value == 1:
            print("You have chosen: Exhaustive Enumeration:")
            ans = exhaustiveEnumeration(obj)
            if ans != 0:
                print(f"The answer is {ans}")
        elif value == 2:
            print("You have chosen: Aproximation of a solution:")
            ans = aproximationOfSolutions(obj)
            if ans != 0:
                print(f"The answer is {ans}")
        elif value == 3:
            print("You have chosen: Binary Search: ")
            ans = BinarySearch(obj)
            print(f"The answer is {ans}")
        elif value == 4:
            print("Thanks for using the program\nSaving and shuting down...")
            break
        else:
            print("Invalid option, please try again...")


if __name__ == "__main__":
    main()
