print("""
Let's introduce to concepts, raise and assert that are related with exceptions and the flow of the program...
* raise [exception] --> It launches the specified exception when this line is reached, no matter what is still happening.
* assert [condition] , [message] --> It is an affirmation, if it is false, stop the program and shows the given message.

Remember, you can use AssertionError to manage an error launched by 'assert'
""")
try:
    number = int(input("Do not type zero (0): "))
    if number == 0:
        raise ZeroDivisionError
    print("Thanks for following the instruction")
except ZeroDivisionError:
    print("Why would you do that?!")
except:
    print("Something unexpected happened")
word = input("Do no write 'hello': ")
assert type(word) == "hello", f"{word}: Why did you ignore the message?!"
print("OK, thanks :)")