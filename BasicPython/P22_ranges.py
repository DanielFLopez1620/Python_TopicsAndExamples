def myIter(count):
    """A simplified for-loop
    count --> range used in a for loop
    """
    for i in count:
        print(i)


print("A range is another immutable type, like the tuples, but it is more optimized...")
count = range(1,10)
print("It's structure is range(begin,end,step), here we see an example: ")
print(f"\nCount: {count}\nType:{type(count)}\nID:{id(count)}")
myIter(count)
pairs = range(0,20,2)
print(f"\nPair numbers(Until 19): {pairs}")
myIter(pairs)