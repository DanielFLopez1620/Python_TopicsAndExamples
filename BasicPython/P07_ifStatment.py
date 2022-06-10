"""
Author: Daniel Lopez
Info from: https://platzi.com/cursos/python/
"""
print(
    """
---------------
if <condition>:
    [Process 1]
else:
    [Process 2]
---------------
It is a conditional block that executes the process 1 if the condition is
true, otherwise it executes the block 2. The condition should be a boolean
value or an operation with a boolean result.
DO NOT FORGET THE INDENTATION
__________________
*Example1 :
"""
)
num = int(input("Write your age: "))
if num > 18:
    print("You are an adult")
else:
    print("You are a child")
print("__________________\n*Example2:")
let = input("Do you want to see a letter?(y/n): ")
if let == "y" or let == "Y":
    print("A letter: D")
print("Ok... finished")
