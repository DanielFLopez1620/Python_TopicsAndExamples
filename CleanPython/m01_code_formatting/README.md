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

One important aspect of the docstring is that it not only becomes part of the code, but also becomes part of a class/object via is **\_\_doc\_\_** attribute

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

So, the annotations become useful to generate documentation, run validations or even enforce checks in the code if required.

After this, we must highlight the PEP-484 which refers to the basics of the type hinting: "Python will remain a dynamically typed language, and the authors have no desire to ever make type hints mandatory, even by convention."

This means that the type hinting's purpose is to have a extra tool to check and assess the correct use of types throughout the code and help to prevent incompabilities. As here, some tools appear, like [Mypy](https://www.mypy-lang.org/).

So now... a question may appear in our heads...

### Annotations replace docstrings?

Well... previously, types were specified in docstrings, but now, annotations make it more compressed. However, the answer to the question is more complex....

So, let's keep in mind the next... types can be added by using annotations and even more information, mostly on nested/dynamic types can be added on the docstrings to improve the documentation, for example:

~~~Python
def pair_collectioning(received: dict) -> dict:
    """
    If the pairs are both valid strings, it will return valid dict pair.

    - received : A dict with:
    {
        "name": "Dan" <string>
        "gamertag": "Dan1620" <string>
    }
    
    - Returns a dictionary like:

    {"name": True/False}

    - Raises:
    - ValueError if the names doesn't match criteria
    """
    pass
~~~

Then, the final answer is... you can use both in order to improve your code and help understanding the implementations required behind params, args and functions or methods.

## Check and tools

Let's explore some useful resources to help you with the process of improving your code, where the questions to ask are:

- Is your code easy to understand to others?
- Does it shows in terms of the domain of the problem?
- Would a new member understand the code?

So, we have the next allies:

### [MyPy](http://mypy-lang.org/)

This tool can help you with type hinting to ensure a static type checking in Python. On one hand, it can tell you about mistypes usage or preventions. On the other hand, it can tell you abut bugs related with this type. Just keep in mind there are chances for false positives.

To install it you can use:

~~~bash
# With PIP
pip install mypy

# Or you can use the package manager of your machine (in my case Ubuntu):
sudo apt install python3-mypy
~~~

### [Pylint](https://www.pylint.org/)

It will help you with reviews on your code, by checking if your code follows the PEP-8 standard (pycodestyle), or other formats like Flake8. It also allows the option to be configurable, but the default setup is complete and strict as required.

You can install it with:

~~~bash
# With pip
pip install pylint

# Or you can use the package manager of your machine (in my case Ubuntu):
sudo pat install python3-pylint-common
~~~

Then just use the comand, **pylint** and the path of the ptyhon file to get the review. To further configure you can use the *pylintrc* file.

### Make

You can set up for automatic check with **Makefiles**, which are files that allow you to configure and set up the compiling, running, testing and related elements of a project. This mean that you can integrate the tools presented above

Let's check an example of a file *checklist*:

~~~Make
typehint:
mypy src/ tests/

test
pytest tests/

lint:
pylint src/ tests/

checklist: lint typehint test

.PHONY: typehint test lint checklist
~~~

After that, you just use the make and you are done:

~~~bash
make checklist
~~~

This will check for the compliance of the PEP8, then check types and finally run the tests.

### [Black](https://github.com/ambv/black)

Another useful tool that you can use to check the code and even it will give format by itself.
