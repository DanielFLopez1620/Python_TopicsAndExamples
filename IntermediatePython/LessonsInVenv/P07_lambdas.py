def main():
    print(
    """
    Another type of function are the lambdas or anonymus function.
    The main difference of these one are that they are single line description.
    Structure: <name> = lambda <var>: <operation>
    Let's see an example with a the function palindrome:
    palindrome = lambda string.
    """
    )
    palindrome = lambda word: word == word[::-1] 
    word = input("Please, type a word to verify if it is a palindrome: ")
    print(f"Is palindrome? {palindrome(word)}")


if __name__ == '__main__':
    main()