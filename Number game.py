import random
number = random.randint(1,100)

guess = int(input("guess"))
if number > guess:
    print("higher")
elif number < guess:
    print ("lower")
else:
    print("you win!")



