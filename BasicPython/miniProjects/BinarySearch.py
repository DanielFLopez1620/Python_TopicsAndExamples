from numpy import result_type


def main():
    objective = int(input("Type a number: "))
    epsilon = 0.001
    down = 0.0
    up = max(1.0,objective)
    answer = (up + down)/2
    while abs(answer**2 -objective) >= epsilon:
        if answer**2 < objective:
             down = answer
        else:
             up = answer
        answer = (up + down)/2
    print(f"The square root of {objective} is equals to {answer}")
if __name__ == '__main__':
    main()