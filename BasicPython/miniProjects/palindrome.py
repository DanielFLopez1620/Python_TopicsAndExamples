def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False


def main():
    while(True):
        flag = input("Do you want to write a word to verify: Is it a palindrome? (s/n): ")
        if flag != 's':
            print("Thanks for using the program")
            break
        else: 
            word = input("Type the word you want to verify: ")
            is_palindrome = palindrome(word)
            if is_palindrome:
                print(f"\n{word} is a palindrome.\n")
            else:
                print("\nThe word it not a palindrome\n")

if __name__ == '__main__':
    main()