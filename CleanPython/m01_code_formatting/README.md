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
