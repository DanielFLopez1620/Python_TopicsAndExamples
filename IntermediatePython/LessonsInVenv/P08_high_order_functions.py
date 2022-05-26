from functools import reduce #Import a high order function 

def main():
    list_example = [1, 2, 3, 4]

    # Search and filter the odd number:
    lc_odd = [i for i in list_example if i%2 != 0]
    odd = list(filter(lambda x:x%2  != 0, list_example)) 

    # Convert the list to its squares:
    lc_squares = [i**2 for i in list_example]
    squares = list(map(lambda x: x**2, list_example))

    # Reduce a list by multiplying all the elements:
    lc_multiplication = 1
    for num in list_example:
        lc_multiplication *= num
    multiplication = reduce(lambda a, b: a* b, list_example)

    # Information: 
    print(
    f"""
    A high order function is a function that has another function as a parameter,
    * FILTER: You use it to classify data, an example is:
        odd = list(filter(lambda x:x%2) != 0, my_list)
        Let's see a similar uses between a list_comprehension and a filter:
        - Example list: {list_example}
        - List comprehension: {lc_odd}
        - Filter function: {odd}

    * MAP: You can map a list and generate a process, for example:
        squares = list(map(lambda x: x**2, my_list))
        Let's see a similar uses between a list_comprehension and mapping:
        - Example list: {list_example}
        - List comprehension: {lc_squares}
        - Filter function: {squares}

    * REDUCE: Simplify a list or make it smaller, this one requires an importation:
        multiplication = reduce(lambda a, b: a* b, my_list)
        Let's see a similar uses between a list_comprehension and a reduction:
        - Example list: {list_example}
        - List comprehension: {lc_multiplication}
        - Filter function: {multiplication}

    DO NOT FORGET TO CHECK THE STRUCTURE IN THE CODE!!!
    """)

if __name__ == "__main__":
    main()
