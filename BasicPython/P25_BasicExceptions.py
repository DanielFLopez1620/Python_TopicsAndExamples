"""
Author: Daniel Lopez
Info from: https://platzi.com/cursos/python-cs/
"""

print(
    """
    There is always a chance that someone -- an error
    --------------------------------------------------------------------------
    But you can use a structure to manage exceptions:
    try:
        [Process]
    except [exception]:
        [Process]
    except:
        [General Exception Process]
    finally:
        [Process to finish]
    This could be helpful if you want a robust program that doesn't stop when
     an exception occurs.
    --------------------------------------------------------------------------
    """
)
try:
    print("Let's try a division by zero")
    value = 5 / 0
    print(value)
except ZeroDivisionError as e:
    print("It is impossible to return a value for this operation.")
except:
    print("Something unexpected happened")
finally:
    print(
        """
        If you want to know more abou exceptions, go to:
        https://docs.python.org/3/library/exceptions.html
        """
    )
