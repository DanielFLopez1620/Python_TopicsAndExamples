"""
Author: Daniel Lopez
Info from: https://platzi.com/cursos/python/
"""

print(
    """
---------------
if <condition>:
    [Process 1]
elif <condition2>
    [Process 2]
else:
    [Process 3]
---------------
Here we have a nested condition, if the first one is false, then it
evaluates the second condition, with this it determines if it executes
the Process 2 or Process 3.
DO NOT FORGET THE INDENTATION
_______________
Example:
    """
)
num = int(input("Enter a number: "))
if num > 0:
    print(f"{num} is positive.")
elif num < 0:
    print(f"{num} is negative.")
else:
    print("The number is zero.")
print(
    """
    You can generated nested conditions as you need or want, but remember
    to keep your code clean and simple, you' will learn more about these
    in the furute.
    """
)
