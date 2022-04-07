print("""You need to know about the scope, when you have declared variables and you need to access them,
 you must be in the correct contest, for example...
 ____________________________
def <function>(<var>):
    <var> += "!"  #Private context of a variable in a function
    return <var>
<var> = "Hi" #Public context of a variable
print(f"Value in funtion: {<funtion>(<var>}")  --> Hi!
print(f"Value outside: {<var>}")  --> = Hi
 ____________________________
 Let's see a running example:
""")
def scopeVis (value): #Example function
    value = str(value) + " :)"
    return value

value = 1
print(f"Value of the variable in the function: '{scopeVis(value)}'")
print(f"Value of the variable in the main is: '{value}'")
print("\nFinally if you need a global variable use 'global <var>' inside a fucntion but it is not recommended.")