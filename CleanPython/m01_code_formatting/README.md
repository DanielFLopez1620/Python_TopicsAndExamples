# About coding formatting

It is more than having a beautiful code, as you may notice that the better the structure of a code is, the better is understand and mantain it.

A clean code is one who allow us to communicate with other developers. Then, its importances is related also with agility, effectiveness and management, as with a maintainable and readable code you can go in a steady, constant and predictable way.

One important term that appears is a **technical debt** that refers to those bad decisions made previously that ended up affecting the project later, and as a debt it will become a greater problem the more time is passes and what is worse is that it can be a silent situtation.

In the case of Python, there are options like the **PEP-8** or cusotm project standards, but it is not only about following these rules as the objective is to be clear and clean, so the code can be understood easily with a single glance (as possible).

Now, let's take a look to the characteristic of the [PEP8](https://peps.python.org/pep-0008/):

- **Grepability:** To be able to use ```grep``` token with ease inside the code by implementing a condition to search variables, arguments and understand the code search.

  **Note:** ```grep``` is a command used to search for content in a text-based way by implementing coincidence, patterns and regular expressions. Its usage can be:

  ~~~bash
  grep 'word' file
  grep -F 'word' file1 file2 file3
  grep 'str1' 'str2' file
  cat file | grep 'word'
  grep --color 'data' file
  ~~~

  For more information, you can check on the [grep guide from CyberCity](https://www.cyberciti.biz/faq/howto-use-grep-command-in-linux-unix/).

- **Consistenty:** So the code looks uniform and it is easier to read.

- **Code quality:** Improve the understanding of the code with one glance and it will give you hints of potential bugs.

## Annotating your code

Good code is self-explanatory but also well-documented. So, focus on what it is supposed to do, not how.

Comments should be avoided while docummenting should be preferred, so you can add information of the data types, examples and important annotations.

In the case of types, this is pretty relevant in Python as it is dynamically typed.

### Docstrings

It is simple, they are string placed in the code with the intention of docummenting a certain part of code, so here you should just add explanation and not justification, then you shouldn't use them for comments.

Why not comments? Well... they can represent our failures to express our ideas in the code, they can mislead the interpretation of the code. There are still some exceptions, like errors in a third-party library that we need to highlight.

Why docstrings? It is simple, they documentate a component (module, class, method or function), where in Python one of the most important cases is related with type usage.

One important aspect of the docstring is that it not only becomes part of the code, but also becomes part of a class/object via is **__doc__** attribute

~~~bash
def my_func():
    "This is my function"
    return None

print(my_func.__doc__)
# It will display:
# 'This is my function'
~~~

This is also important when using tools for documentation, as the documentation then can be accessed at runtime or compilation, tools like **Sphinx** will create a basic doc of your project based on this aspects. Another important reason, is that the documentation should be ready and available for all the development team.

Also, keep in mind that the documentation is as important as a wiki, a user manual or even as a *README* file of a repository.

Sadly, some of its disadvantages remain, being the most harmful one, that the *docstring* have to be mantained manually and at constants period of times.

### Annotations

They were introduced with the PEP-3107 and the purpose is to hint about the arguments in functions and methods, so you can specify the expected type that requires to be defined.

~~~Python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
def insert_point(x: float, y: float) -> Point:
    """
    Insert a poin the the cartesian map
    """
    pass
~~~

As you note in the example above, the annotations help us understand that **x** and **y** are *float* variables, but this is only informative. Another important aspect is that you can specify the return type, by using the arrow operator **->** which is also informative.

In case you want to explore about the annotations of a certain element, you can use:

~~~Python
print(insert_point.__annotations__)
# It will display:
# {'x':float, 'y':float, 'return':__main__.Point}
~~~
