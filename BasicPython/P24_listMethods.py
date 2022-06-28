"""
Author: Daniel Lopez
Info from:
  1) https://platzi.com/cursos/python-cs/
  2) https://www.geeksforgeeks.org/list-methods-python/
"""

print("It is time to show more list methods for python:")
example = [1, 2, 3, 4]
print(
    f"""
    * <list>.insert(pos, element): Insert the element in the position given:
         example.insert(3,4): {example.insert(1,5)}
    * <list>.append(element): Insert the element in the last position:
         example.append(5): {example.append(6)}
    * <list>.pop(pos): Delete the value in the position given:
         example.pop(3): {example.pop(3)}
    * <list>.remove(element): Delete the first coincidence of the param given:
         example.remove(1): {example.remove(1)}
    * <list>.index(element): Return the position of the element (if it exists):
         example.index(5): {example.index(5)}
    You can also specify between range to give the index:
    index(element,begin,end)
    * <list>.count(element): Return  the coincidences of the param:
         example.count(1): {example.count(1)}
    * <list>.sort(): Organize the list (least to greatest):
         example.sort(): {example.sort()}
    You can reverse the order for sort if you set .sort(reverse = True)
    or just use <list>.reverse()
    """
)
copy = example.copy()
print(
    f"""
    * Example: {example} and Copy: {copy}
    * <list>.copy(): Generates a copy of a list:\nWe have: id(example):
    {id(example)} and id(copy): {id(copy)}
    * Finally, if you want to clear an array you use <list>.clear():
     Example: {example.clear()}
     """
)
