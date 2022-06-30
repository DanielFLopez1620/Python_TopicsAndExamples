# A list of employers with its personal data:
DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'HÃ©ctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def main():
    """ 
    A listcomprehension to specify the language of the developer,
    for example, python:
    """
    python_devs = [worker["name"] for worker in DATA 
                        if worker["language"] == "python"]
    
    print("-"*20 + "\nPYTHON DEVS:")
    for devs in range(len(python_devs)):
        print(f"Developer #{devs}: {python_devs[devs]}")

    """
    A list comprehension to classify the workers by the organization they belong,
    for example, Platzi:
    """
    platzi_workers = [worker["name"] for worker in DATA 
                        if worker["organization"] == "platzi"]
    
    print("-"*20 + "\nPLATZI WORKERS:")
    for worker in range(len(platzi_workers)):
        print(f"Worker: #{worker}: {platzi_workers[worker]}")

    """
    A filter and map used to specify a group, in the next case, for people older
    than 18 years:
    """ 
    adults = list(filter(lambda worker: worker["age"] >= 18, DATA))
    adults = list(map(lambda worker: worker["name"], adults))

    print("-"*20 + "\nADULTS:")
    for num in range(len(adults)):
        print(f"Worker #{num}: {adults[num]}")

    """
    A way to add a new category a a dictionary, in this case, if the person is
    older than 70 years old:
    """
    old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))
    
    print("-"*20 + "\nELDER PEOPLE:")
    for num in range(len(old_people)):
        print(f"Old person #{num}: {old_people[num]}")
    print("Remeber, for python 3.9 or older, you can add elements to a dict with '|'")


    """
    Another example to classify the developers by language, but using filter
    and map, for example, javascript developer
    """
    js_devs = list(filter(lambda developer: developer["language"] == "javascript", DATA))
    js_devs = list(map(lambda developer: developer["name"], js_devs))
    print("-"*20 + "\nJS DEVS:")
    for devs in range(len(js_devs)):
        print(f"Developer #{devs}: {js_devs[devs]}")

    #TODO: Finish the challenge of comprehension vs lambda and high func.
if __name__ == "__main__":
    main()