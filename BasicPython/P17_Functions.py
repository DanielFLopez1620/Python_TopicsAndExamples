"""
Author: Daniel Lopez
Info from: https://platzi.com/cursos/python/
"""

print(
    """*ABSTRACTION: You do not need to know all about something to use it,
for example, a car or a calculator.
Remember, it is important to understand how to use a program, library,
command...
*DESCOMPOSITION: "Divide and rule" with a common idea, simplify your code.
________________________________________
Now let's introduce the reason you are in this script:
\nFUNCTION: Definition:
def <name> (<params>):
    <body>
    return <value>
\nFUNCTION: Invoke:
<name>(<params>)
Now, let's see the code.
"""
)


def concatenetion(str1, str2):  # Function with two params
    str1 = str(str1)
    str2 = str(str2)
    return str1 + str2


def yourName(
    first, last, order=False
):  # Function with three params, one is a default param
    if not order:
        return last + " " + first
    else:
        return first + " " + last


word1 = input("Type your name: ")
word2 = input("Type your last name: ")
flag = input("Want to change the order of the name?(s/n): ")
print(f"NAME:\nConcatenation: {concatenetion(word1,word2)}")
if flag[0] == "n":
    flag = True
    print(f"Format: {yourName(word1,word2,flag)}")
else:
    print(f"Format: {yourName(word1,word2)}")
