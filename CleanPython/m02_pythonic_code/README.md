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

And we can go further with slices, which is literally what it means, a slice (or fragment) of the list or array.

~~~Python
# Continuing with the previous example
>>> my_collection[1:3]
(20, 1620)
~~~

The convention of the slices implies that the beginning of the range is inclusive, and the ending of the range is exclusive. But it doesn't stop there, as you can use other interesting features.

~~~Python
>>> other_collection = (1, 2, 3, 5, 8, 13, 21, 34)
# Accessing from beginning to given limit
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

And in case, you want to skip a parameter, for example, to include the beginning as in ```[:3]```, you just use ```None``` in the slice.

## Creating sequences

The magic of getting elements of arrays or collections of elements is thanks to the ```__getitem__``` method, which is called when we use the brackets to access a certain element and it also checks the ```__len__``` methods to obtain the size and determinate if it is a valid access.

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

Some key points to consider here are:

- ```*values``` in the constructor definitions means that will take all the arguments passed by extension.

- ```_values``` is a representation of a private attribute for this class, which is still accessible outside but by convention should be access directly.

- We access to the ```__getitem__``` method inherited from the list class we are based on.

### Implementing a custom sequence

This implementation that doesn't rely on a built-in object must remember that the result of an indexing operation should be an instance of the same class and the slice should respect the range of the beginning until the end minus one position.

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

In the case of Python, we can use ```finally``` to add execution steps after a block is completed or exited, in the case of our previous example it should be easy as:

~~~Python
my_file = open(filename)
try:
    process_file(my_file)
finally:
    my_file.close()
~~~

But there are simplifiers mechanism like:

~~~Python
with open(filename) as fd:
    process_file(fd)
~~~

In the case of **with**, which was introduces in the PEP-343, it enters the context manager which will open the file and will close it at the end.

The context managers consist of two base methods ```__enter__``` and ```__exit__```, which, as you may suppose, act when entering and going outside the desired scope, in the case of the **with** it would be in the opening of the file and after the processing of the file. Even in the case where exception occurs, the ```__exit__``` will be called, so you can safely manage the clean up conditions.

An example for this is the case of a backup of a Data Base, where you can ensure a stop of the database, allow backup options and then run it again:

~~~Python
class BackUpDataBase:
    def __enter__(self):
        stop_db()
        return self
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        restart_db()

def main():
    with BackUpDataBase():
        backup_db()
~~~

When designing this type of implementation, consider what should be done before and after a certain block. And a good practice is to set up a return value in the ```__enter__```.

In the case of the ```__exit__```, the arguments passed refers to the exception type, exception value and exception traceback, which can be *None* if nothing happens. Also, in this context, do not consider a *True* return unless you have a good reason for that.

## More implementations for context managers

There are more cases than just ```__enter__``` and ```__exit__```, for example, we can use the ```contextlib``` module from the standard library.

This module contains helper functions and objects to implement context managers and use others already implemented to write more compact code.

We can start with the ```contextlib.contextmanager``` decorator, which converts the code on a function into a context manager, so you can implement enter/exit methods inside one by taking advantage of a generator function.

~~~Python
import contextlib

@contextlib.contextmanager
def handler_db():
    stop_db()
    yield
    start_db()

with handler_db():
    backup_db()
~~~

The *yield* is used to define a generator function, which returns a generator iterator that produces a sequence of values on demand rather than computing each of them at once. In other words, every word after the *yield* can be considered part of ```__exit__```.

The previous presentation allows an easier refactoring, re-usage of codes and an option to have a context manager that doesn't belong to any particular class.

Another tool from this library is the ```contextlib.ContextDecorator``` which is a mixin base class that provides the logic for applying a decorator to a function so it will make it run inside the context manager.

~~~Python
class dbhandler_decorator(contextlib.ContextDecorator):
    def __enter__(self):
        db_stop()
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        db_start()

@dbhandler_decorator()
def db_backup()
    run("backup")
~~~

As you may notice, you can create an inherit class to implement your own decorator and it will act as a context manager for the given function.

This implementation allows independence (the decorator doesn't know about the functions aspect and vice-versa) which is good but it can also be a downgrade as you cannot use the elements returned by ```__exit```. Also, the decorator logic is only defined once and can be reused many times.

To finish this sections, let's explore another tool from *contextlib*.

Let's use the *contextlib.suppress* which is a *util* package that enters a context manager which allows the management of certain provided exceptions (so it acts similar a *try* / *except*) with a calling in the *suppress* method to make the management more explicit.

~~~Python
import contextlib

with contextlib.suppress(DataConversionException):
    enter_data(json_input)
~~~

## Properties, attributes, and different types of methods for objects

In Python, everything is public (the underscore is just a notation to indicate a private intention), so it is different of what you are use to use with other language (public, private and protected).

So, let's explore more about the conventions in Python for the elements present in a class or code that you should consider:

### Underscores

As the brief comment before, underscores can have meaning in the context of Python.

~~~Python
class Cupboard:
    def __init__(self, drawers, id)
        self._drawers = drawers
        self.id = id
~~~

Both attributes of the class are accessible, but by convention the elements that start with a single underscore (```_```) should be kept as private.

To access private elements, you should use **getters** and **setters** properly, this as a way for secure read/write operations. Also, the elements that remain exposed should be relevant to an external caller object.

~~~Python
class Cupboard:
    def __init__(self, drawers, id)
        self._drawers = drawers
        self.__hidden = 20
        self.id = id

    def getDrawers(self):
        print("# of drawers is:", self._drawers)
~~~

Now, what about a double underscore ```__```, it implies that it is private and that no other object can modify it. If you try to access to it, it will display an **AttributeError**. The real reason behind this behavior is the **name mangling** that creates a different name for the attribute based on ```_<class_name>__<attr_name>``` and then you can access it (everything is public in Python).

However, keep in mind that double underscores aren't the Pythonic way.

### Properties

You may be used to implement the regular attributes just to hold values, but you may also require to compute based on the state of the object and the value of the other attributes, so you can implement properties, which are access control tools defined to interact with attributes.

Let's be honest here... they are the **getters** and **setters** you know from other languages.

~~~Python
import re

USERNAME_FORMAT = re.compile(r"^[A-Za-z0-9_]{3,20}$")


def is_valid_username(candidate: str) -> bool:
    return re.match(USERNAME_FORMAT, candidate) is not None


class User:
    def __init__(self, name: str):
        self._username = None
        self.username = name

    @property
    def username(self) -> str:
        return self._username

    @username.setter
    def username(self, new_name: str):
        if not is_valid_username(new_name):
            raise ValueError(
                f"Can't set '{new_name}' because it's not a valid username "
                "(must be 3–20 characters, letters/numbers/underscore)."
            )
        self._username = new_name



u = User("test_user")
print(u.username)
u.username = "invalid name"
~~~

We just watched an implementation to check a valid alphanumeric username. We have a ```@property``` defined that acts as a getter. This implementation reflects the case of respecting a private attribute an only using the valid interfaces to access it.

To go further, we have the setter that have a companion *@username.setter* which indicates the usage of the already defined property (yes, you have to define the property first). This approach allows to run validations before updating the value, in the case presented with a validation function for the regex code.

Just as a reminder, prefer this approach of properties and avoid to use named methods (```get...``` or ```set...```) to be more Pythonic.

Now, let's introduce another term the CC08 or better as **command and query separation** which refers simply that a method of an object should either answer or do something but do not both (so not get/set on the same boat please). As our aim is to be as concise and short as possible for better abstraction, readable and reusable code.

## Iterables obj

For... for... our iterable friend with arrays, tuples, sets, dicts... but it is all? Well... no.

Python has its own *iteration protocol*, so when using ```for e in elements:``` it checks:

- If the object itself has ```__next__``` or ```__iter__``` methods.

- If the sequence has ```__len__``` and ```__getitem__``` methods.

So, what does Python interpreter consider when using iterable objects, it aims to call ```iter()``` which as you may suppose use ```__iter__``` in the background, but it will also require ```__next__```.

~~~Python
class Countdown
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return CountdownIterator(self.start)

class CountdownIterator:
    def __init__(self, start):
        self.current = start

    def __iter__(self)
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return value

def main()
    for num in Countdown(5):
        print(f"Counting down: {num}")

if __name__ == __main__()
    main()
~~~

As you may notice, when implementing the iterations you should consider when to step and raise a ```StopIteration```.

Before, moving on there is another consideration to keep in mind, it is about what the iter should do else than just returning ```self```, let's check another example with a date range container

~~~Python
from datetime import timedelta

class DateRangeContainerIterable:
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

    def __iter__(self):
        current_day = self.start_date
        while current_day < self.end_date:
            yield current_day
            current_day += timedelta(days=1)

def main():
    for d in DataRangeContainerIterable(date(2025,9,20), date(2025, 9, 24)):
        print(d)
~~~

So, it is a good idea to work with container iterables when dealing with generators, so you prefer memory efficient (yields one value at a time),allows multiple iterations, use single iterator exhaustion.

### Creating iteration sequences

If you do not implement and ```__iter__``` and still try to iterate, it will search for a ```__getitem__```, and if it isn't found, well you get a ```TypeError```.

But as we presented before, to create a sequence we just need the implementation of ```__len__``` and ```__getitem__```. So, this implementation should be carefully planned. Why? Because if you need to pass element by element it will consume more resources.

So, let's create a sequence to illustrate our current focus:

~~~Python
class CountDownRange:
    def __init__(self, start_value, end_value, step)
        self.start_value = start_value
        self.end_value = end_value
        self.step = step

    def __iter__(self):
        current = self.start_value
        while current + step < self.end_value
            yield current
            current += step
~~~

As you may suppose now, when having a loop based range, it will call ```__iter__``` again until the range is completed.

Let's go deeper with sequences, and explore more about them... to the question... of not using ```__iter__``` and ```__getitem```, then the approach of the sequence would be:

~~~Python
class CountDownRangeVariation:
    def __init__(self, start_value, end_value, step)
        self.start_value = start_value
        self.end_value = end_value
        self.step = step
        self._range = self._create_range()

    def _create_range(self):
        result = []
        current = self.start_value
        while current + step < self.end_value
            result.append(current)
            current += step
        return result

    def __getitem__(self, num):
        return self._range[num]

    def __len__(self):
        return len(self._range)
~~~

You may doubt it but... even with this last implementation, you can use negative indexes as the work is delegated to the base implementation of a *list*.

Before you decide which sequence to implement, make sure to test and compare the CPU and memory usage if each implementation.

## Container objects and content

Now... what containers do have in common? Of course, the ```__contains__``` method. Yeah... I didn't answer that first too. But let's proceed to learn more.

The Python implementation that calls this method can be ```in```:

~~~Python
<element> in <container>
~~~

Which is reflected as:

~~~Python
<cointainer>.__contains__(<element>)
~~~

Let's explore a more detailed example:

~~~Python
import string

class PasswordPolicy:
    def __init__(self, min_length=8, require_digit=True, require_symbol=True):
        self.min_length = min_length
        self.require_digit = require_digit
        self.require_symbol = require_symbol

    def __contains__(self, password: str):
        if(len(password) < self.min_length>)
            return False
        if self.require_digit and not any(ch.isdigit() for ch in password):
            return False
        if self.require_symbol and not aby(ch in string.punctuation for ch in password):
            return False
        return True

policy = PasswordPolicy()

print("Pa$$sw0rd" in policy)
print("Password" in policy)
~~~

As you just checked, the ```in``` implementation can also be used to check policies, going further than containers, for example, to review characteristics and conditions of the data before considering it is inside a group or element.

## Dynamic attributes for objects

This is possible bu considering the implementation of ```__getattr__```. How? Check the next example:

~~~Python
class ClassWithAttrs:
    def __init__(self, attribute):
        self.attribute = attribute

    def __getattr__(self, attr):
        if attr.startswith("fallback_")
            name = attr.replace("fallback_", "")
            return f"[fallback resolved] {name}"
        raise AttributeError(
            f"{self.__class__.__name__} has no attribute {attr}")

special = ClassWithAttrs("value")
print(special.attribute)
~~~

So, you can use the ```__getattr__``` definition to  get transformation on the class to include new values. Do not forget to implement the **raise** as it is required by the method. And also, do not forget to consider multiple cases when adding attributes this way.

## Callable objects

Objects as functions? Sounds crazy but can help you sometimes. How? Bu using decorators or (as we will focus) using the method ```__call__```.

This method will be called when you try to execute an object as if it were a regular function, the arguments will be passed too. Why to implement this? One common application is related with states.

Keep in mind that the implementation is:

~~~Python
object(*args, **kwargs)
# Also transformed into:
object.__cal__(*args, **kwargs)
~~~

Let's proceed with the example:

~~~Python
class ToggleCount:

    def __init__(self):
        self._state = False
        self._counter = 0

    def __call__(self):
        self._state = not self._state
        if(self._state != False)
            self._counter += 1

    def get_counter(self)
        return self._counter

~~~

## Remember the magic methods
