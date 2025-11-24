# General Traits of Good Code

Software requires design, so it is not only about a clean code but also a clear design and structure (and also a robust implementation). Now, let's get started.

## Design by contract

Most of the time, the code is oriented to the users, then you may need to divide the responsibilities of the application into different layers. We also encapsulate functions and expose them by using a interface to use that particular functionality (over an API **Application Programming Interface**). So this components and layers should be tested to avoid unexpected behaviors.

Consider a simple case, where you expect to sum two numbers... but instead you receive characters... the function won't work properly, but you should ensure that before trying the operation, the correct types are passed. It is not only about documenting the correct types, but ensuring that the things are done properly.

This is why we can implement **DbC** (Design by Contract) which refers to parts agreeing on a contract that, if violated, will raise an exception (including a clear explanation on the reason). This should consider:

- **Preconditions:** Check everything is fine before executing the function, mostly related with params and data passed, also known as *constraint on the caller*.

- **Postconditions:** Validations done to the returned value, also referred to *constraint on the callee*.

- **Invariants:** Highlighting the elements that remains constant.

- **Side-effects:** Include documentation on effect that may affect your code.

And this is hwo the contract is generated, with the objective in mind that if a error occurs, it is related with the preconditions or postconditions to ease the correction process. What does this mean? If a precondition fails, it is an error on the client. However, if the postcondition fails, the error is in the routine, class or supplier.

One comment, it is supposed that preconditions imply checking parts to avoid problems because running something before checking it would be inconvenient.

### Preconditions

Let's deepen in the items that must be checked before the element or function contracted, so it can work correctly.

The validations mostly refer to the data types of the passed info, it should not only depend on the information of the docstring and tools like **MyPy**, but rather, including the development of a complete review of them. This validation can be run before calling the function or inside the function, it can vary according your purposes. But you must know that the first approach is a **tolerant** one, while the second one is a **demanding** one.

It doesn't matter the principle if you keep in mind the **non-redundancy** principle (or better said as... do not do it twice or more).

### Postconditions

You must ensure the state of the response after the process has been done (assuming the preconditions were met satisfactory), always aiming to respect the contract and validating that all the clients will receive the proper output.

### Pythonic contract

The best way to achieve this is by providing control mechanism for our methods. Then, taking advantages of raises like ```RunTimeError``` or ```ValueError```. Also, you can choose to create your own proper exceptions.

Another consideration can be the isolation of the code, as much as you can. How? By creating smaller functions and decorators.

All of this to maintain the principles of this approach, recognize errors when the contract is broke.

### Simple example

Here is a illustrative example of DbC theory provided by Eiffel Software:

~~~Python
class DICTIONARY [ELEMENT]
feature
    put (x: ELEMENT; key: STRING) is
            -- Insert x so that it will be retrievable
            -- through key.
        require
            count <= capacity
            not key.empty
        ensure
            has (x)
            item (key) = x
            count = old count + 1
        end

    ... Interface specifications of other features ...

invariant
    0 <= count
    count <= capacity
end
~~~

You can see clearly the preconditions and postconditions, while having additional info on the invariant conditions.

## Defensive Programming

It refers to... defend until you cannot hold longer! Well... really not, but instead of a contract, it is an approach where the objects, functions and methods are able to protect themselves against invalid inputs.

Here you consider some scenarios where you might expect something to happen, and then implement a code that prevents it, which can include handling procedures, assertions or ensuring types.

### Error handling

The idea is to gracefully respond to expected error in an attempt to either continue the program execution or fails if it is better than the error propagates. It can include cases like:

- **Value Substitution:** When you make a substitution of a forbidden/conflicting value to a more proper one which can be a default, a well-known case, a sentinel value or a approximate approach but it must be carefully considered to avoid higher risks, so the option becomes a selection based on robustness and correctness.

    ~~~Python
    def get_info(port=1991)
        info = log(port)
        return info.compressed()
    ~~~

- **Exception Handling:** It is better to stop the program to avoid it continuous working with wrong data. This does not only refer to data passed as input, as the functions can have side-effects or there may be external factors affecting the code. So the function/method should communicate properly, clearly and unambiguously the problem and notify it to the rest of the application.

  As you may have guessed, the exceptions are the mechanism for these purposes, as the management can handle the different exceptions that arise. However, they can weaken encapsulation as you may prefer to declare all the exceptions possible but you should be aware than then the function isn't context-free and may have additional side effects worth considering in other elements or components. To handle them correctly, consider:

  - **Right level of abstraction:** The exception has to be consistent with the logic encapsulated on it. For this, you can compare the next cases:

    ~~~Python
    def read_file(path):
        try:
            with open(path, "r") as f:
                return f.read()
        except FileNotFoundError:
            # Incorrect as the file reader should consider this
            print("Error: File Not Found")
            return ""
    ~~~

    ~~~Python
    def read_file(path):
        with open(path, "r") as f:
            return f.read()
        # Correct as the exception is responsability of the file reader
    ~~~

    The first case is wrong, as it calls an exception out of context (the file can be checked before or the file reader alreay implements that logic). While the second case is correct as its allow the propagation of the situation.

## Additional resources

- [PEP 316 - Programming by Contract for Python | Python](https://peps.python.org/pep-0316/)
- [Design by Contract & its revelance in Game Programming | Medium](https://medium.com/@kaushik.swapnil5/design-by-contract-its-relevance-in-game-programming-de7c75558b64)
- [Building bug-free O-O software | Eiffel Software](https://www.eiffel.com/values/design-by-contract/introduction/)
