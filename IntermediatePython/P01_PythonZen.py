import os
print("-"*20)
import this
print("-"*20)
print("\nRemember, this is the way!\nThe way of a python developer")
print("Also, you can use an interactive terminal of python with ", end=": ")
if os.name == "posix":
   print("python3 o python")
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
   print("py")