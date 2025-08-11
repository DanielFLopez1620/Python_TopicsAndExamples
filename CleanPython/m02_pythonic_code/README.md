# Pythonic Code

Here, we will explore more about clean coding with Python by exploring the usage of different elements and how can we use them better.

Let's start by talking about idioms, which is a particular way of writing code to perform a specific task. It also have a defined structure every time it is used and they are actually coded, and in Python it has a name: **Pythonic**.

Why is it better to do it this way? So it can perform better, it can be easier to understand, more compact to use and it can add efficiency to the process (even in reviewing stages).

So, let's begin to explore some of them:

## Indexes and slices

Arrays? Lists? Easy, you just access their elements by indexes. And as you may remember, Python has additional features for the access, for example, did you know that with negative indexes you can access the elements in reverse?

~~~Python
>>> my_collection = (16, 20, 1620, 261)
# Accessing last element
>>> my_collection[-1]
261
# Accessing the element before the last one
>>> my_collection[-2]
1620
~~~

And we can go further with slices, which is literaly what it means, a slice (or fragment) of the list or array.

~~~Python
# Continuing with the previous example
>>> my_collection[1:3]
(20, 1620)
~~~

The convention of the slices implies that the beginning of the range is inclusive, and the ending of the range is exclusive. But it doesn't stop there, as you can use other interesting features.

~~~Python
>>> other_collection = (1, 2, 3, 5, 8, 13, 21, 34)
# Accesing from beginning to given limit
>>> other_collection[:4]
(1, 2, 3, 5)
# Accessing from limit to the ending
>>> other_collection[5:]
(13, 21, 34)
# Obtaining everything again
>>> other_collection[::]
(1, 2, 3, 5, 8, 13, 21, 34)
# Given pattern of begin, end, step
>>> other_collection[1:6:2]
(2, 5, 13)
~~~

But, if you didn't know, all these cases implies the use of *slice* which is a Python build-in object which you can also use:

~~~Python
# Continuing the example above
>>> my_slice = slice(1:6:2)
>>> other_collection[my_slice]
(2, 5, 13)
~~~

And in case, you want to skip a parameter, for example, to include the beginning as in *\[:3\]*, you just use **None** in the slice.

## Creating sequences

The magic of getting elements of arrays or collections of elements is thanks to the *\_\_getitem\_\_* method, which is called when we use the brackets to access a certain element and it also checks the *\_\_len\_\_* methods to obtain the size and determinate if it is a valid access.

This means that you can implement your own access to sequences in custom classes, so let's check two approaches

### Implementing a wrapper on a class

This case just means that you are using a base class for your implementation, so most of the work is already done, and it would look like these:

~~~Python
class Iterable:
    def __init__(self, *values):
        self._values = list(values)
    
    def __len__(self):
        return len(self._values)
    
    def __getitem__(self, item):
        return self._values.__getitem__(item)
~~~

Some keypoints to consider here are:

- **\*values** in the constructor definitions means that will take all the arguments passed by extension.

- **\_values** is a representation of a private attribute for this class, which is still accesible outside but by convention should be access directly.

- We access to the **\_\_getitem\_\_** method inherited from the list class we are based on.

### Implementing a custom sequence

This implementation that doesn't rely on a built-in object must remember that the result of an indexing operation shouldl be an instance of the same class and the slice should respect the range of the beginning until the end minus one position.

In that case, a raw implementation can look like this:

~~~Python
class MySequence:
    def __init__(self, *items):
        self._data = items

    def __getitem__(self, index):
        if isinstance(index, slice):
            start, stop, step = index.indices(len(self))
            new_items = []
            i = start
            while (step > 0 and i < stop) or (step < 0 and i > stop):
                new_items += (self._data[i],)
                i += step
            return MySequence(*new_items)
        else:
            return self._data[index]

    def __len__(self):
        count = 0
        for _ in self._data:
            count += 1
        return count
~~~

## Context managers

A tool that can correctly respond to a pattern which can be every situation where we want to run some code with pre/pos conditions, for example, when we open a file we want to make sure they are closed after the processing (to prevent corruption and leaks) and you would have to remember to free the resources of allocation and so on...

In the case of Python, we can use **finally** to add execution steps after a block is completed or exited, in the case of our previous example it should be easy as:

~~~Python
my_file = open(filename)
try:
    process_file(my_file)
finally:
    my_file.close()
~~~
