name = str('mike')
number = int(input("How many letters are in the word? It is between 2 and 15: "))
while number != 4:
    number = int(input("How many letters are in the word? It is between 2 and 15: "))
    if number > 4:
        print("lower")
        print("You're wrong!")
    if number < 4:
        print("higher")
        print("You're wrong!")
    elif number == 4:
        print("Good JOB! finally!")
        break

