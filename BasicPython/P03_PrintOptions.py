"""
Author: Daniel Lopez
Info from: https://platzi.com/cursos/python/
"""

var = "sample text"
# First mode of concatenation
print("Text:", var)
# Second option:
print(f"Text: {var}")
# Third option:
print("Text {}".format(var))
# If you want to ommit the new line use:
print("Here a new line, ", end="->")
print("This is still in the same line", end="")
print("An another one")
# If you want to add a separation you use:
print(var, "->", var, "ready", sep="*")
