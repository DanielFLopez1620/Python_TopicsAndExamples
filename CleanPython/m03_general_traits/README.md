# General Traits of Good Code

Software requires design, so it is not only about a clean code but also a clear design and structure (and also a robust implementation). Now, let's get started.

## Design by contract

Most of the time, the code is oriented to the users, then you may need to divide the responsibilities of the application into different layers. We also encapsulate functions and expose them by using a interface to use that particular functionality (over an API **Application Programming Interface**). So this components and layers should be tested to avoid unexpected behaviors.

Consider a simple case, where you expect to sum two numbers... but instead you receive characters... the function won't work properly, but you should ensure that before trying the operation, the correct types are passed. It is not only about documenting the correct types, but ensuring that the things are done properly.

This is why we can implement **DbC** (Design by Contract) which refers to parts agreeing on a contract that, if violated, will raise an exception (including a clear explanation on the reason). This should consider:

- **Preconditions:** Check everything is fine before executing the function, mostly related with params and data passed, also known as *constraint on the caller*.

- **Postconditions:** Validations done to the returned value, also referred to *constraint on the callee*.
