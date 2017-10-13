def userinput():
    num = int(input("your number"))
    return num


def processData (number):
    if number % 2 == 0: #divisible by 2
        return True
    elif number % 3 == 0: #divisible by 3
        return True
    elif number % 4 == 0: #divisible by 4
        return True
    elif number % 5 == 0: #divisible by 5
        return True
    elif number % 6 == 0: #divisible by 6
        return True
    elif number % 7 == 0: #divisible by 7
        return True
    else:
        return False

    

