def primeNumbers(limit):
    """
    Return all the prime numbers until the given limit
    """
    for i in range(2,limit + 1):
        flag = False
        for j in range(2,i):
            if i % j == 0:
                flag = True
                break
        if not flag:
            print(i)
    return None

if __name__ == '__main__':
    number = int(input("Welcome to the prime numbers program, which is the limit you want to use?: "))
    primeNumbers(number)
    print("Thanks for visiting the program...")