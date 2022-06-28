"""
Author: Daniel Lopez
Info from: https://platzi.com/cursos/python-intermedio/
"""


def palindrome(word):
    return word == word[::-1]


def division(num1, num2):
    return num1 / num2


def main():
    print(
        """
    Now let's learn how to manage exceptions...
    The commands you will need are:
    * try:
        [Process]
    --> With a try, you can execute code that is running in a protected way,
    if an exception is called, it is 'encapsulated' and launched but it will
    be caught by the 'catch statmente'.

    * catch <Exception> as <ExpName>:
        [Plan B]
    --> If an exception is called, you can catch it by specifying the type, it
    will only caught the given exception, for example, if you have a
    ZeroDivisonError, it will not be caught by the IndexError block. Also, if
    the name of the exception is long, you can make an alias for it, like 'as
    FNF' in the case of FileNotFoundException.

    * catch Exception:
        [Plan Z]
    --> If you want to prevent every type of exception, these is the father
    block to achieve it. Just make sure it is at the end of the 'catch'
    statments. Butnote that it is not recommended to manage general
    exceptions.

    * raise <Exception>("Message/Traceback")
    --> You can also launch exception manually, because sometimes you know
    that somthing is an error, but Python doesn't. An example? You want to
    process data, but it doesn't work if the data that they send you is only a
    zero.

    * finally:
        [Do not forget]
    --> It is the last statment that runs, it does something whether an
    exception ocurred or everything went write. It is useful to close files or
    disconnect from databases.

    * assert <condition>, <Message error>
    -->
    NOW, let's see a practice and the code:

    """
    )
    follow = True
    while follow:
        print("-" * 60)
        try:
            # Division, here the exception is related with the input:
            print("This is a loop for palindrome and division...\nDIVISION:")
            num1 = float(input("Type the first number: "))
            num2 = float(input("Type the second number: "))
            value = division(num1, num2)
            print(f"The result of the division is: {value}")

            # Palindrome, here the exception depend on the string
            print("-" * 60 + "\nPALINDROME:")
            word = input("Type a word to verify if it is palindrome: ")
            # Verification with raise:
            if word is "" or word is " " or word.isspace():
                raise TypeError("You must type a word not a space")
            elif word.isdigit() or word.isnumeric():
                raise TypeError("Please type words, not numbers or symbols.")
                # Verification with assert:
            assert len(word) > 2, "Please type a longer word..."
            value = palindrome(word.lower())
            print(f"Is '{word}' a palindrome?: {value}")

        except ZeroDivisionError:
            print("Remember, the division by zero is indeterminated.")
        except TypeError as Typ:
            print(f"Data conflict ocurred...\n{Typ}")
        except KeyboardInterrupt:
            print("Be patient, you could have waited until the question...")
        except AssertionError as Asse:
            print(f"An affirmation has been vulnerated...{Asse}")
        except:
            print("Something unexpected happened, analyze the exception.")
        finally:
            print("Try/Except finished")
        ask = input("Do you want another try?(s/n): ")
        if ask == "n":
            follow = False
    print("Thanks for using the program...")


if __name__ == "__main__":
    main()
