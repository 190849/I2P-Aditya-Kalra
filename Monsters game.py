import sys

#Functions
def Wellcome():
    print("""You need food. You need food to survive. Theres a wide selection infront of you, but YOU HAVE NO MONEY!! You pick up a powerbar and look at the exit.
 You have to options: 1. Stash the power bar in your pockets and sneakily walk out the front door. 2. Ask the lady at the counter if you can just take it and hope for the best.""")
    choice = int(input("Which do you choose?"))
    if choice ==1:
        print("You made it out alive. You survived the monsters. Congrats")
        print("please play again", name,"!")
        sys.exit()
    if choice ==2:
        print("They said no and you died!")
        print("You lose!")
        print("please play again", name,"!")
        sys.exit()
    else:
        print("You didn't choose either option. Your lazy and weak. You die.")
        print("You lose!")
        print("please play again", name,"!")
        sys.exit()


#Main program 
name = input("Hello. Welcome to the game. What is your name?")

print("""
 Welcome to the HKIS monsters game""", name, """. You've woken up in a world full of monsters where HKIS is the only place you are safe.
 Once you leave HKIS, you must be strong enough to survive the monsters. Otherwise you will die!
""")

print(name, " you are currently extremely thirsty. If you don't get water soon you will DIE!")
first_choice = int(input("""You currently have two options. Option 1: Drink water from the fish pond for a cost of $0. Option 2: Take your ten HKD and go down to the cafeteria to try and buy water.
Which do you choose? 1 or 2?"""))


if first_choice == 1:
    print("Ooops. The water from the fish pond is extremely poisonous and kills you instantly!")
    print("You lose!")
    print("please play again", name,"!")
    sys.exit()

if first_choice == 2:
    print("You walk down to the cafeteria and buy a small bottle of water for $10. You now have no money.")

else:
    print("you didn't choose either of the options. You die of thirst. Congrats. you played yourself.")
    print("You lose!")
    print("please play again", name,"!")
    sys.exit()

print("You sit in the cafeteria for a while trying to figure out your next move. Nothing springs to mind so you decide to walk aruond")
print("Soon you realize you drank too much water and need the restroom. You walk into the gym to find a pair of running shoes")
print("You put the shoes on")

second_choice = int(input("""You have two choices once again.
Choice 1: You can try get strong enough to kill all the monsters in the HKIS GYM.
Choice 2: You can go for a run on the field to try and get fast enough to outrun the monsters. Which do you choose?"""))

if second_choice == 1:
    print("you hit the gym hard and get pretty big. You might actually survive...")


if second_choice == 2:
    print("Monsters are quick. Seriously quick. You try to get faster but it doesn't really work. You leave school and get eaten.")
    print("You lose!")
    print("please play again", name,"!")
    sys.exit()

if second_choice != 1:
    print("You didn't choose either option. Your lazy and weak. You die.")
    print("You lose!")
    print("please play again", name,"!")
    sys.exit()

print("You're big, but you need energy. You leave school and run into the wellcome.")
Wellcome()






