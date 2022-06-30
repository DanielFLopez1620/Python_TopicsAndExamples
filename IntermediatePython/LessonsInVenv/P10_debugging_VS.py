"""
Author: Daniel Lopez
Info from: https://platzi.com/cursos/python-intermedio/
"""


def list_mul(num):
    # A function that returns the multiples of a given number (with list_com)

    if num % 2 == 0:
        return 0
    return [num * i for i in range(1, 13)]


def for_mul(num):
    # A function that returns the multiples of a given number (with for loop)
    mul = []
    for i in range(1, 13):
        mul.append(num * i + i)
    return mul


def main():
    print(
        """
    Debugging is a useful tool, here you can run a code by step or and
    indicated line (specified by the user). So you can see the variables
    and it changes during the execution, here you should be able to see
    an error or mistake in a easier way.

    In VSCode, you can use it too, you should see on your left menu an
    icon with a bug and a pause button. If you clic it, you should see a
    'Execute and debugg', here you should specify the language (in this case,
    python).

    Do not forget to mark the lines you can to execute step by step, you must
    clic in the line, and then a red circle will appear. Or you simply can run
    it with all the lines, here you do not need to select lines, the file will
    be run step by step.

    Now you are ready to  clic on "Debugg". A new bar must appear here you can
     specify if you continue to the next step, pause or stop the execution.

    While debuggin, you should see in the left window the variables and its
     current state that will be changing as if it were running as usual.

    Take advantage of this tool to verify the logic of your program or just to
    check how to fix something because this is useful for larger projects when
    there are a lot of functions and modules connect or even when you have
    many loops on your code.

    Now try to use it in the next example:
    1) First, catch the error.
    2) Try to think a solution, it is simple.
    """
    )
    print("-" * 20 + "\nWelcome to the program of multiples (1-12): ")
    num = int(input("Please, type a number:"))
    try_mul = list_mul(num)
    your_mul = for_mul(num)
    print(f"Attempt 1:{your_mul}\nAttempt 2:{try_mul}")

    print("Did you see the mistake/error?")


if __name__ == "__main__":
    main()
