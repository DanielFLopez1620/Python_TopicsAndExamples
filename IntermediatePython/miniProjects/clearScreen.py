import os

def clearScreen():
    """
    Clear screen that depends on your Operating System (OS)
    """
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")
    return None