def dict_creation(exp, limit):
    """
    """
    my_dict = {}
    for i in range(limit):
        my_dict[i] = i**exp
    return my_dict


def dict_com_creation(exp, limit):
    """
    A function that returns a dictionary with the number and 
    and the correspondent exponent.
    exp --> The exponent you want to receive as value
    limit --> The lenght of the dictionary.
    return dictionary: Number(key) and exponent(value)
    """
    return {i: i**exp for i in range(1,limit)}


def main():
    print("You already know how to create dict: ")
    print("Dict with the number and the third power:\n" + dict_creation(3,10))
    print(
    """
    But you can also make dicts comprehensions, following the next structure:
    <dict> = {key: value for value in iterable if condition}
    Here the condition is also optional. And you can work with them in the 
    main or in a defined function, let's see some examples:
    """)
    ex_dict = {i: i**3 for i in range(100) if not i % 3}
    print("Dict with the number and the third power:")
    print(ex_dict)
    print("Another example:")
    print(dict_com_creation(0.5,10))

    
if __name__ == "__main__":
    main()