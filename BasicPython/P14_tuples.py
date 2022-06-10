"""
Author: Daniel Lopez
Info from: https://platzi.com/cursos/python/
"""

print(
    """
A tuple is another type that can storage many values, but it main
characteristic is that it is immutable.
Once you added an element, it cannot be changed.
    """
)
my_tuple = (1, 2, 3, 4)
print(f"Here we have our first tuple: {my_tuple}")
my_slice = my_tuple[1:3]
print(
    """
Before you discover that you cannot change the tuple, you can turn a list into
a tuple with 'tuple()'.
Just make sure that the list is correct and can be converted.
    """
    )
my_list = [2, 4, 6, 8, 10]
convertion = tuple(my_list)
print(f"{convertion} is a {type(convertion)}")
print(
    f"""
You can know the length of a tuple: len(my_tuple) = {len(my_tuple)} and you can
 also use slicing: [1:3]: {my_slice}"
    """
)
print("Now we will try to add a element...\nNOTE THIS WILL LAUNCH AN ERROR\n")
my_tuple.append(5)
my_tuple2 = ("h", "i", "!")
print(
    """
    When you add two or more tuples, you are not modifying it, you are creating
    a new one, it is like making a copy, because tuples are unmutable."
    """
)
sum_tuple = my_tuple + my_tuple2
print(f"{my_tuple} + {my_tuple2} = {sum_tuple}")
print("\nFinally, you can unpack a tuple by assigning multiple variables: ")
x, y = my_tuple[0:2]
print(f"The tuple {my_tuple[0:2]}, is unpacked in x: {x} and y:{y}")
