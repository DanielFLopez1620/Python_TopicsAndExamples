print("""
Another iterable type is the dictionary, its structure is:
<dict> = {"key1":"value1","key2":"value2",...}
Its main characteristic is that it is not always organized but you can iterate and use it
""")
my_dict = {"One":1,"Two":2,"Three":3}
print(f"Our dictionary is {my_dict}")
print(f"Now let's see some keys, we have the key: 'Two', the value is: {my_dict['Two']}")
my_dict["Four"] = 4
print(f"You can add elements with my_dict[<key>] = value :\n{my_dict}")
print("Now let's see some examples of iteration with for loop:\nEXAMPLE 1: Listing keys...")
con = 1
for keys in my_dict.keys():
    print(f"Key #{con} = {keys}")
    con += 1
print("EXAMPLE 2: Lisiting values...")
con = 1
for values in my_dict.values():
    print(f"Value #{con} = {values}")
    con += 1