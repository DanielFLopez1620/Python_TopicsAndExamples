"""
Author: Daniel Lopez
Info from: https://platzi.com/cursos/python/
"""

print("A string is a group of characters... like any word")
my_str = "Hello"
name = "daniel"
print(
    f"""
You can access to an element you specify, for example:
The first letter is {name[0]}
Note that the counts with lists always begins with zero
Now let's introduce you with some useful methods to transform strings

Capitalize: {name} --> {name.capitalize()})

 """
)
name = "DaNieL"
print(f"LowerCase: {name} --> {name.lower()}\n")
name = "daniel"
print(
    f"""
UpperCase: {name} --> {name.upper()}
Replace with an 'e': {name} --> {name.replace('a','e')}
Finally, if you want to know the length of the string use: len(<list>):
The length of {name} is equal to {len(name)}
    """
    )
