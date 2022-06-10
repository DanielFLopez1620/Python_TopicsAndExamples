"""
Author: Daniel Lopez
Info from: https://platzi.com/cursos/python/
"""

print(
    """\nA For loop can use other structures to make the repetition:
for <var> in range(<start>,<end>,<process>)
    [Process]
__________________________
Example: Reverse a string:
"""
)
word = input("Type a word: ")
reverse = ""
for num in range(len(word) - 1, -1, -1):
    reverse += word[num]
print(f"The word is {word} and its reverse is {reverse}.")
# Note that you can do this with slicing.
print(
    """
In general terms, there are two statments that you have to think about when
you are working with loops:
* break --> Force the exit of the loop.
* continue --> Generate a jump to the next iteration of the loop.
\nLet's see some examples:
__________________________
1. Stop the reading of a string if you see a coincidence:
"""
)
word = input("Type another word:")
for letter in word:
    if letter == "a":
        print("Letter 'a' found, reading stopped.")
        break
    print(letter)
print("_" * 20)
print("2. Print the numbers until 16, without the table of 3:")
ini = 0
while num < 16:
    num += 1
    if num % 3 == 0:
        continue
    print(num)
