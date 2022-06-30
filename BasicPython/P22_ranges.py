"""
Author: Daniel Lopez
Info from: https://platzi.com/cursos/python-cs/
"""


def myIter(count):
    """A simplified for-loop
    count --> range used in a for loop
    """
    for i in count:
        print(i)


count = range(1, 10)
print(
    f"""A range is another immutable type, like the tuples, but it is more
    optimized...
    It's structure is range(begin,end,step), here we see an example:
    Count: {count}\nType:{type(count)}\nID:{id(count)}
    """
)
myIter(count)
pairs = range(0, 20, 2)
print(f"\nPair numbers(Until 19): {pairs}")
myIter(pairs)
