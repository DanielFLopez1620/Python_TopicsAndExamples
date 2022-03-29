print("""\nA loop is a statment that repeates a process, 
while <condition>:
    [Process1]
""")
indicator = 1
print("Example 1: Sum and verify condition")
while indicator < 5:
    print(f"{indicator} < 5 ")
    indicator += 1 # indicator = indicator + 1
print(f"Now {indicator} is equal 5")
print("-"*20)
print("Example 2: Verify input user: ")
user = 10
while user > 0:
    user = int(input("Type a negative number: "))
print(f"You wrote the number {user}")