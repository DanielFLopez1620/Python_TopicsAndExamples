"""
Author: Daniel Lopez
Info from: https://platzi.com/cursos/python-intermedio/
"""


def main():
    print("Do you remember how to define a list and a dictionary?")
    ex_list = [1, 2, 3, 4]
    ex_dict = {"One": "1", "Two": "2"}
    print("Yes, for list you use [] and for dictionaries {}")
    print(f"List example: {ex_list}\nDict example: {ex_dict}s")

    supper_list = [ex_dict, {"Three": "3", "Four": "4"},
                    {"Five": "5", "Six": "6"}]
    supper_dict = {
        "numbers ": ex_list,
        "integers": [-1, 5, -10, 30],
        "floats": [2.2, -6.5, 3.14],
    }

    print(
        f"""
    You can combine list and dictionaries, for example, we have:
    * supper_list:
    {supper_list}
    * supper_dict:
    {supper_dict}
    You define them like you normally do, but instaed of an element you use
    a dict or a list, and you can iterate for them and even inside the
    anidated elements, for example, using two for loop to show the next:
    """
    )
    for key, value in supper_dict.items():
        print(f"Key({key}): Value({value})")
        if type(value) == type(list()):
            for i in range(len(value)):
                print(f"    Inside element #{i+1}: {value[i]} ")

    print("Remember that it is better to use 'isinstance()'")     

    print("\nOr you can iterate inside the elements of a dict inside a list:")
    for dic in supper_list:
        print("\nDictionary:")
        if type(dic) == type(ex_dict):
            for key, value in dic.items():
                print(f"Key({key}: Value({value})")


if __name__ == "__main__":
    main()
