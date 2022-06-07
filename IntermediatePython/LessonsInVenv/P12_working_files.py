import os

def read_file(name):
    """
    A function to read a file with elements organized in a list. One per 
    line. It will display the content in the terminal.

    name --> Path and name of the file concatenated .
    """
    content = []
    with open(name, 'r', encoding="utf-8") as rf:
        for line in rf:
            if len(line.strip()) == 1:
                content.append(line)
            else:
                content.append(line[0])
    

def write_file(name,adding,format):
    """
    A function that will append or rewrite a file in format of list. The mode
    should be specified as 'a'(append) or 'w'(write).

    name --> Path and name of file concatenated.
    adding --> List of the text/info to add to the file.
    format --> Specify mode: Append/write.
    """
    with open(name, format, encoding="utf-8") as wf:
        for element in adding:
            wf.write(element)
            wf.write("\n")


def fill_doc(num):
    """
    Create a list filled with info with a maximun size specified.

    num --> Number of lines/spaces in the list.
    """
    text = []
    for i in range(num):
        info = input("Type a sentences or a word:")
        text.append(info)
    return text


def main():
    print(
    """
    There are many extensions for files... as you can see on your laptop/PC...
    
    But we can classify them in:
    - TEXT: Bits and bytes that represent text, like .txt or scripts.
    - BYNARY: Contain information related to images, videos, sound...


    To manage file, you can access them in three modes:
    * R --> Read.
    * W --> Write (Overwrite)
    * A --> Write (Add/Append)

    -->Basic line to manage file:
    with open("./path/of/file.txt", "<mode>") as <abr>:
        [Process with file]
    You can add a thir parameter, 'encoding="utf-8"' to specify region. 

    """
    )
    # Declaration of paths for the directory and file.
    file_path = os.getcwd()
    file_path = os.path.join(file_path, "IntermediatePython")
    file_path = os.path.join(file_path, "LessonsInVenv")
    direct = os.path.join(file_path ,"PracticeFiles")
    print(f"Directory: {direct}")

    # Creation of folder if it doesn't exist.
    try:
        if not os.path.isdir(direct):
            os.mkdir(direct, 0o777)
    except FileExistsError:
        print("Directory already exists...")

    # Specify the name of the file to read/write.
    print("READING/WRITING EXAMPLE: ")
    file_name = input("Type the name of the file to interact: ")
    final_path = os.path.join(direct,file_name)

    # Specify mode and do the correspondent action.
    opt = input("Do you want to read (r) or write (w) the file?: ")
    if os.path.isfile(final_path):
        if opt == 'r':
            read_file(final_path)
        elif opt == 'w':
            num = int(input("How many lines would you like to add?: "))
            info = fill_doc(num)
            write_file(final_path, info, 'a')
    elif opt == 'w':
        num = int(input("How many lines would you like to write?: "))
        info = fill_doc(num)
        write_file(final_path, info, 'a')
    else:
        print("File not found, please verify directory...")


if __name__ == "__main__":
    main()