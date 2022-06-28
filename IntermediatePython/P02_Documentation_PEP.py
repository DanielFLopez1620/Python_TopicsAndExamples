"""
Author: Daniel Lopez
Info from: https://platzi.com/cursos/python-intermedio/
"""
print(
    """
Sometimes you may feel stuck with a command, in these cases, you can visit the
official documentation for Python 3: https://docs.python.org/3/
There is another option, for example, if you have a command and you don't know
something about it use: help(). Let's see an example with help(print):
"""
)

help(print)

print(
    """

Another important thing you must know about python is the PEP. A standart to
improve the readabilidty of Python code, because as Guido Van Rossum said:
"Code is read much more often that it is writen"
You can see PEP8 here: #https://www.python.org/dev/peps/pep-0008
But, let's see a short version of PEP8 conventions:
1. Naming conventions:
    - Never use l, o, I.
    - For functions or methods use lowercase separet by underscore:  my_func
    - For variable use lowercase: counter
    - For a class use the camel case: MyModel
    - For constants use uppercase separeta by underscore: MY_LONG
    - For package and modules use always lowercase: program.py
2. How to choose names:
    - Always choose an explicit name of variable.
    - Do not use personal abreviations.
3. Code Layout:
    - Do not extend a line more than 79 characters.
    - Surround function/classes with two blank lines.
    - Surround methods witha single blank line.
    - Surround clear steps inside a function to make it clear.
4. About lines:
    - Avoid line wrapping.
    - Remember lines not longer than 79 characters.
    - Respect the identation of a function, conditional or loop.
    - Break binary operatiors by putting the operator before the variable
    in the new line.
5. Identation:
    - Use 4 consecutive spaces for an identation.
    - Prefer spaces over tabs.
    - Do not fix tab with spaces.
    - To highlight the identation use comments of the steps.
6. Closing Brace:
    - Line up the closing brace with the first non-whitespace line.
    - Line up the brace where the construct starts.
7. Comments:
    - The comments should respect the identation level.
    - Use # for each line you want to comment
    - For inline comments refer to the line statment, do not explain the
    obvious and use two or more spaces to separate the comment.
    - Use docummentation strings to explain the function (resume, params
    and returns).If it is only one line, close it in the same line.
8. Adding (or not) whitespaces:
    - Surround binary, assignment and comparison operators with a single
    whitespace on either side.
    - With slices, if you use operations, respect the previous line.
    - Avoid spaces before a comma, semicolon, colon or next/before a
    braces, parentheses or bracket.
9. Programming recommendations:
    - Do not comare Boolean values with True or False.
    - Empty sequences are false in the if statements.
    - Do not use a variable to compare with None.
    - Use string methods rather than slicing.
Extra: Tools to get help:
    - Linters: Programs that analyze code and flag errors, like:
    pycodestyle (PEP8), flake8.
    - Autoformatters: Programs that refactor your code to conform
    with PEP8 automatically, for example, black

You do not need to memorize these, but make sure you follow the zen of python
and some of the recommedations present in PEP8, or the PEP format you are
using to improve your code and projects.

"""
)
