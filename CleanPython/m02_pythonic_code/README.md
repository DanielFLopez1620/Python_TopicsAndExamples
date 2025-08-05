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