print("Let's see the slicing and some booleans methods:\nSLICING:")
example = "Python is awesome"
print(f"example[3:6] = {example[3:6]}")
print(f"example[2:8] = {example[2:8]}")
print(f"example[3:6:-1] = {example[3:6:-1]}")
print(f"example[::-1] = {example[::-1]}")
print(f"example[::2] = {example[::2]}")
print("-"*30)
print("BOOLEAN METHODS:")
#Examples strings:
str1 = "HELLO"
str2 = "h1"
str3 = "hi :)"
str4 = "1234"
str5 = " "

print(f"'{str1}' is alpha?: {str1.isalpha()}")
print(f"'{str4}' is alpha?: {str4.isalpha()}\n")

print(f"'{str2}' is numeric?: {str1.isnumeric()}")
print(f"'{str4}' is numeric?: {str4.isnumeric()}\n")

print(f"'{str2}' is alphanumeric?: {str2.isalnum()}")
print(f"'{str3}' is alphanumeric?: {str3.isalnum()}\n")

print(f"'{str1}' is uppercase?: {str1.isupper()}")
print(f"'{str2}' is uppercase?: {str2.isupper()}\n")

print(f"'{str1}' is lowercase: {str1.islower()}")
print(f"'{str2}' is lowercase?: {str2.islower()}\n")

print(f"'{str5}' is space: {str5.isspace()}")
print(f"'{str4}' is alpha?: {str4.isspace()}\n")



