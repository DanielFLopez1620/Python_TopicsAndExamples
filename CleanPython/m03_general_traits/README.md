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

## Additional resources

- [PEP 316 | Python](https://peps.python.org/pep-0316/)

