print("A string is a group of characters... like any word")
my_str = "Hello"
name = "daniel"
print(f"""You can access to an element you specify, for example:
The first letter is {name[0]}
Note that the counts with lists always begins with zero
Now let's introduce you with some useful methods to transform strings
""")
print(f"Capitalize: {name} --> {name.capitalize()}\n")
name = "DaNieL"
print(f"LowerCase: {name} --> {name.lower()}\n")
name = "daniel"
print(f"Capitalize: {name} --> {name.upper()}\n")
print(f"Replace with an 'e': {name} --> {name.replace('a','e')}")
print("\nFinally, if you want to know the length of the string use: len(<list>):")
print(f"The length of {name} is equal to {len(name)}")