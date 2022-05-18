def my_list_comp (limit):
    """
    Create a list using list comprehension with a for loop and if statement.
    limit --> The maximum range wanted, not the size of the list.
    return result --> List with the products of 4, 6 and 9.
    """
    result = [i*4 for i in range(0, limit) 
              if not (i*4 % 6) and not (i*4 % 9)]
    return result


def main():
    square = []
    square_n3 = []
    print(
        """
        There are many ways to assign and create variables and lists, you know,
        for example:
        1) Direct creation: <list> = [1,2,3,4]
        2) Using a for loop with append: <list>.append(<value>)

        But there is another way to create them, and in a shorter way...
        It is called list comprehension, you can use it while creating a single line
        description loop (and optional conditions), let's see it's structure...
        <list> = [i for i in range(<range>) if <condition>]

        Throughout this program you will see more about all the mentioned ways to
        create listed above:
        
        """)

    for i in range(1, 101):
        square.append(i**2)

    print(f"Squares: {square}")

    for num in square:
        if num % 3:
            square_n3.append(num)
            
    print(f"Squares with no 3 division: {square_n3}")
    
    square_lc = [i**2 for i in range(1, 101) if i**2 % 3]
    print(f"Squares using list comprehension: {square_lc}")
    
    product_469 = my_list_comp(2500)
    print(f"List with the product of 4, 6 and 9:\n{product_469} ")


if __name__ == "__main__":
    main()