"""
Author: Daniel Lopez
Info from: https://platzi.com/cursos/python-cs/
"""

my_list = [1, 2, 3, 4]
print(
    f"""
    You can define a list with [] which is a group of elements (int,
    string, float... or a combination of them):You can know its memory space
    with id(): {id(my_list)} for the data: {my_list}
    """
)
copy = list(my_list)
copy2 = my_list[::]
print(
    f"""Remember, it is better to clone list when you are working with them...
    You can use list() or make a 'slice' with [::] to make a copy and you will
    obtain different objects:
    my_list: {my_list} with id: {id(my_list)}
    copy: {copy} with id: {id(copy)}
    copy2: {copy2} with id: {id(copy)}
    """
)
print(
    """
    Quick tip... we have 'List comprehension' and it is faster when you want
    to create a list:
    """
)

example = [i for i in range(10)]
dup = [i * 2 for i in example]
twoprod = [i for i in example if i % 2 == 0]
print(
    f"""
    We have, for example, ... <list> = [i for i in range(<var>)] like:
    {example}
    Or you can add opperations ... <list> = [i * <num> for i <list/range>]
    like:
    {dup}
    Even, you can add conditions ... <list> = [i for i in <list> if (<condition>),
    for example:
    {twoprod}
    """
)
