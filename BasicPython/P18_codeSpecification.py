print("It is a good practice to documentate your code, here you see an example for the function of product:")
def product(a,b):
    """Product of two numbers.

    param int a,
    param int b,
    returns product of a and b.
    """
    result = a * b
    return result
print("The structure of the doc should be short and useful, contains a description, the params and the return.")
print("If you want to see the documentation go to a python terminal and type help(<function>), you should \nsee the description")