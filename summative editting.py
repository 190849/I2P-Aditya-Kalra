import sys #imported system so that I can use exit code later on in the code

#defining 3 variables that I will use in my functions to tell the user how many mistakes they made
mincorrectanswer = 0
sincorrectanswer = 0
hincorrectanswer = 0
numberofquizzes = 0
#overarching menu function


def quizzes():
    print("""Welcome to the quiz menu. These quizzess are designed to test your skills in 3 subjects.
    Hope you enjoy!""")
    quizlist = ["1. Math", "2. Science", "3. History"] #list of all of my quizes
    print ("The quizzes available to your are", quizlist)
    quiz = str(input("Which quiz would you like to take? 1, 2, or 3?"))
    while quiz == "1" or "2" or "3": #Using one while loop for the menu
        if quiz == "1":
            math()
        elif quiz == "2":
            science()
        elif quiz == "3":
            history()
        else:
            print("You have not selected any quiz. I guess you dont want to take a quiz right now ",name,".")
            print("Thank you for playing. If you would like to play later be sure to come back!")
            sys.exit()    #exitting the system if the user doesnt want play


#math function

def math():
    global mincorrectanswer
    mincorrectanswer = 0
    print("Welcome to the math quiz! Hope you enjoy this quick 5 questions quiz!")

    q1 = str(input("What is the square root of 144?")) #q1 = quesiton 1
    if q1 == "12":                #using if statements for the question answers
        print("Good job. Lets move onto the next question!")
    else:
        print("Oops. That doesnt seem to be right but it's okay! Lets move onto the next question!")
        mincorrectanswer = mincorrectanswer +1              #Adds 1 to the number of incorrect answers
    q2 = str(input("What is 99-95?"))
    if q2 == "4":
        print("Nice! Lets keep going!")
    else:
        print("Oh no! That's wrong!")
        mincorrectanswer = mincorrectanswer + 1
    q3 = str(input("What is the cube root of 125?"))
    if q3 == "5":
        print("Good stuff! Next question!")
    else:
        print("Sorry! That's not correct!")
        mincorrectanswer = mincorrectanswer + 1
    q4 = str(input("What is 30 * 22?"))
    if q4 == "660":
        print("good job! Move on!")
    else:
        print("Noooo! that's wrong!")
        mincorrectanswer = mincorrectanswer + 1
    q5 = str(input("What is 2 to the power of 4?"))
    if q5 == "16":
        print("nice!")
    else:
        print("Oh no! That's the wrong answer.")
        mincorrectanswer = mincorrectanswer + 1
    #printing the total number of questions wrong
    print("For this quiz you got", mincorrectanswer, "questions wrong.")
    #letting the user get back to the menu
    mathtestfinal = input("Would you like to return to the main menu and take another quiz? Please reply yes or no")
    #letting the user reply in lower and upper case letters
    mathtestfinall = str.lower(mathtestfinal)
    if mathtestfinall == "yes":
        quizzes()
    else:
        print("Bye! thank you for taking the math quiz!")
        sys.exit()

#science function

def science():
    global sincorrectanswer
    sincorrectanswer = 0
    print("You chose the science quiz! Good luck!")
    #q1s stands for question 1 science. I am following the same format as the math function
    q1s = input("What is the name of the element with the chemical symbol ‘He’?")
    #need to allow the user to respond in any case
    q1ss = str.lower(q1s)
    if q1ss == "helium":
        print("Good job! Onto the next question!")
    else:
        print("Oh no! that's the wrong answer.")
        sincorrectanswer = sincorrectanswer + 1     #once again keeping track of the number of questions the user gets wrong
    #Have to repeat the same format for the rest of the questions
    q2s = input("What is the biggest planet in our solar system?")
    q2ss = str.lower(q2s)
    if q2ss == "jupiter":
        print("Great! Next question!")
    else:
        print("No! that's the wrong answer.")
        sincorrectanswer = sincorrectanswer + 1
    q3s = input("Does a bowling ball fall faster than a ping pong ball? Yes or no?")
    q3ss = str.lower(q3s)
    if q3ss == "no":
        print("Nice work! Next question!")
    else:
        print("Oops! that's the wrong answer.")
        sincorrectanswer = sincorrectanswer + 1
    q4s = input("Is HCl an acid or a base?")
    q4ss = str.lower(q4s)
    if q4ss == "acid":
        print("Correct! Next question!")
    else:
        print("That's the wrong answer.")
        sincorrectanswer = sincorrectanswer + 1
    q5s = input("Is the world round or flat?")
    q5ss = str.lower(q5s)
    if q5ss == "round":
        print("That was the last question!")
    else:
        print("Wrong answer.")
        sincorrectanswer = sincorrectanswer + 1
    #Questions done. Time for feedback and an option to quit or go back to the main menu
    print("For the science quiz, you got", sincorrectanswer, "questions wrong", name)
     #letting the user get back to the menu
    sciencetestfinal = input("Would you like to return to the main menu and take another quiz? Please reply yes or no")
    #letting the user reply in lower and upper case letters
    sciencetestfinall = str.lower(sciencetestfinal)
    if sciencetestfinall == "yes":
        quizzes()
    else:
        print("Bye! thank you for taking the science general knowledge quiz!")
        sys.exit()

#history function

def history():
    global hincorrectanswer
    hincorrectanswer = 0
    print("Welcome to the History quiz! Good luck!")
    #q1h stands for question 1 history. I am following the same format as the math function
    q1h = input("When was America discovered? A. 1990, B. 1492, C. 1665")
    #need to allow the user to respond in any case
    q1hh = str.lower(q1h)
    if q1hh == "b":
        print("Good job! Onto the next question!")
    else:
        print("Oh no! that's the wrong answer.")
        hincorrectanswer = hincorrectanswer + 1     #once again keeping track of the number of questions the user gets wrong
    #Have to repeat the same format for the rest of the questions
    q2h = input("Who was the British Prime minister during WWII? A. Winston Churchill, B. James Corden, C. George III")
    q2hh = str.lower(q2h)
    if q2hh == "a":
        print("Great! Next question!")
    else:
        print("No! that's the wrong answer.")
        hincorrectanswer = hincorrectanswer + 1
    q3h = input("What continent did Dr. Livingstone explore? A. Asia, B. Africa, C. South America")
    q3hh = str.lower(q3h)
    if q3hh == "b":
        print("Nice work! Next question!")
    else:
        print("Oops! that's the wrong answer.")
        hincorrectanswer = hincorrectanswer + 1
    q4h = input("Which country was the last to abolish slavery? A. USA, B. England, C. Brazil")
    q4hh = str.lower(q4h)
    if q4hh == "c":
        print("Correct! Next question!")
    else:
        print("That's the wrong answer.")
        hincorrectanswer = hincorrectanswer + 1
    q5h = input("Who was the leader of the nazi party? A. Hitler, B. Stalin, C. Bush")
    q5hh = str.lower(q5h)
    if q5hh == "a":
        print("That was the last question!")
    else:
        print("Wrong answer.")
        hincorrectanswer = hincorrectanswer + 1
    #Questions done. Time for feedback and an option to quit or go back to the main menu
    print("For this history quiz, you got", hincorrectanswer, "questions wrong", name)
     #letting the user get back to the menu
    historytestfinal = input("Would you like to return to the main menu and take another quiz? Please reply yes or no")
    #letting the user reply in lower and upper case letters
    historytestfinall = str.lower(historytestfinal)
    if historytestfinall == "yes":
        quizzes()
    else:
        print("Bye! thank you for taking the history general knowledge quiz!")
        sys.exit()








#where the game actually starts


#Welcome user to the game and ask for name?
name = input("Hi! Welcome to my quiz. What is your name?")
print ("Hope you are ready! This is a pretty tough quiz. Good luck!")

#call the function
quizzes()
