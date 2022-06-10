"""
Author: Daniel Lopez
Info from: https://platzi.com/cursos/python/
"""

print(
    """\nIt is a controled loop by an initial condition
for <var> in <list>:
    [Process]
"""
)
print("Example 1: Spelling:")
word = input("Type a word: ")
print("Spelling: ")
for letter in word:
    print(letter)
print("Example 2: Count vowels:")
word = input("Type a word: ")
vowels = 0
for letter in word:
    if letter == "a":
        vowels += 1
print(f"The word {word} has {vowels} 'a'(s) ")
