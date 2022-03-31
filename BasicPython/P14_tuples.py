print("A tuple is another type that can storage many values, but it main characteristic is that it is immutable...")
my_tuple = (1,2,3,4)
print(f"Here we have our first tuple: {my_tuple}")
my_slice = my_tuple[1:3]
print("\nBefore you discover that you cannot change the tuple, you can turn a list into a tuple with 'tuple()'")
my_list = [2,4,6,8,10]
convertion = tuple(my_list)
print(f"{convertion} is a {type(convertion)}")
print(f"You can know the length of a tuple: len(my_tuple) = {len(my_tuple)} and you can also use slicing: [1:3]: {my_slice}")
print("Now we will try to add a element...\n\nNOTE THIS WILL LAUNCH AN ERROR...\n")
my_tuple.append(5)