print
(
"""
When you are programming, you can make mistakes, for example, 
by mispelling a variable or a function with a logic that doesn't
work. But there are more mistakes:
    * SYNTAX ERROR: This happens when you type something wrong and
    python cannot understand it, for example, you write 'prin()' 
    instaed of 'print()'.
    
    * EXCEPTIONS: You are testing your code, but... something went 
    wrong and something unexpected happened, here Python launches 
    an object 'Exception' to manage the alert, some of them are:
        - KeyBoardInterrupt: When you press Ctrl + C in terminal.
        - KeyError: When you try to access to a key not available.
        - IndexError: Common when you index a list in a wrong way.
        - ZeroDivisionError: I think you know math... a/0 --> Ind.
        - ImportError: You imported something, but... it fail.
    Some of them are very intuitive.

A traceback is the name of the error/exception message, this can
help you to localize the error, if it is part of the program.
Remember, when you ask to the user for info, there is always a
chance that an exception ocurrs.

If the object 'Exception' or 'Error' is not caught in a function
and it is launched in the main, Python will stop the program.
"""
)