# Definition of functions:
def substract(num1,num2):
    """Substract two numbers

    num1 int
    num2 int
    return num1 - num2
    """
    print("\nUsing the substract function...")
    return num1 - num2


def applyArithmetic(function,values):
    """Apply an arithmetic function with two params

    function int function with two parasm
    values [] int list
    return the result of the function param with float format
    """
    print("\nUsing the applyArithmetic function")
    result = function(values[0], values[1])
    return float(result)

print("You can use functions as arguments in other functions let's see and example:")
print("Let's practice with the values 3 and 5 for the declared function: \n" , applyArithmetic(substract,[3,5]))

duplicate = lambda word,num : str(word)*num 
print("There is another type of function called lambdas, that are functions in expression: ")
print(f"For example, let's use duplicate with 'Yes' and 3:\n{duplicate('Yes',3)}")