import sys #Import the sys library
def factorial(num):
    """
    Calculate the factorial by recursivity,

    num int > 0,
    return num!.
    """
    if num == 1:
        return 1
    return num * factorial(num - 1)


print("Recursivity: A function that calls itself, let's see the factorial example: ")
var = int(input("Type a number: "))
print(f"Factorial of {var} is {factorial(var)}")
print(f"You can see the limit of recursion with the command 'sys.getrecursionlimit()': {sys.getrecursionlimit()}")