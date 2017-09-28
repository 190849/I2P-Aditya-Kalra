name = str("mike")
number = float(input("How many letters are in the word? It is between 2 and 15: "))
while number != 4:
    number = float(input("Guess again!"))
    if number > 4:
        print("You're wrong!")
        print("lower")
        number += 1
    if number < 4:
        print("You're wrong!")
        print("higher")
while number == 4:
    print("Good Job!")
    break
print("Now you know that there are 4 letters in the word!")
first_letter = str(input("Try guess the first letter of the word! What do you think it is?"))
while first_letter != "m":
    first_letter = str(input("guess again!"))
while first_letter == "m":
    print("Good JOB!!!! you got the first letter")
    break
guess = str(input("Do you want to try guess the word? You have one chance!"))
while guess != name:
    print("Oops! You can guess again after you find out the next letter!")
    break


