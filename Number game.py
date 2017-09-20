import random

number = random.randint(1,1000)


i = 9

while i>8:
    guessnumber=int(input("please guess a number"))
    if guessnumber>number:
        print("lower")
    elif guessnumber<number:
        print("higher")
    elif guessnumber == number:
        print("You win")
        break



