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


def fibonacci(num):
    if num == 0 or num == 1:
        return 1
    return fibonacci(num - 1) + fibonacci(num - 2)

print("Recursivity: A function that calls itself, let's see the factorial example: ")
var = int(input("Type a number: "))
print(f"Factorial of {var} is {factorial(var)}")
print(f"You can see the limit of recursion with the command 'sys.getrecursionlimit()': {sys.getrecursionlimit()}")
print("\nFinally, another example of recursivity is the Fibonacci series, as you can see next:")
var = int(input("What number you would like to see with Fibonacci: "))
print(f"Result:{fibonacci(var)}")