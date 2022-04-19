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


def menu():
    """
    Display the menu of the program of currency conversion
    """
    print("""
    ------------------------------------------
    |       Conversión to make               |
    ------------------------------------------
    | 1. Colombian pesos to dolars           |
    | 2. Colombian pesos to euros            |
    | 3. Colombian pesos to mexican pesos    |
    | 4. Dolars to Colombian pesos           |
    | 5. Euros to Colombian pesos            |
    | 6. Mexicans pesos to Colombian pesos   |
    | 7. Exit                                |
    ------------------------------------------
    """)
def main():
    dolar = 3771.83
    euro = 4081.0
    mex_peso = 187.0
    stay = True
    current = 0.0
    conversion = 0.0
    while(stay):
        menu()
        opt = int(input("What conversion do you want to do?: "))
        clearScreen()
        if opt == 7:
            print("Thanks for using the program...")
            break
        elif opt > 0 and opt < 7:
            if opt == 1:
                print("Access to conversion: Colombian pesos to dolars")
                current = float(input("How many Colombian pesos do you have?: "))
                conversion = current / dolar
                print(f"You have {conversion} dolars")
            elif opt == 2:
                print("Access to conversion: Colombian pesos to euros")
                current = float(input("How many Colombian pesos do you have?: "))
                conversion = current / euro
                print(f"You have {conversion} euros")
            elif opt == 3:
                print("Access to conversion: Colombian pesos to mexican pesos")
                current = float(input("How many Colombian pesos do you have?: "))
                conversion = current / mex_peso
                print(f"You have {conversion} mexican pesos")
            elif opt == 4:
                print("Access to conversion: Dolars to colombian pesos")
                current = float(input("How many dolars do you have?: "))
                conversion = current * dolar
                print(f"You have {conversion} colombian pesos")
            elif opt == 5:
                print("Access to conversion: Euros to colombian pesos")
                current = float(input("How many euros do you have?: "))
                conversion = current * euro
                print(f"You have {conversion} colombian pesos")
            else:
                print("Access to conversion: Mexican pesos to colombian pesos")
                current = float(input("How many Mexican pesos do you have?: "))
                conversion = current * mex_peso
                print(f"You have {conversion} colombian pesos")
        else:
            print("Invalid option...")
    

if __name__ == '__main__':
    main()