



input("Do you want a marsbar?")
def yes_no():
    yes = set(['yes','y', 'ye', ''])
    no = set(['no','n'])

    while True:
        choice = raw_input(answer).lower()
        if choice in yes:
           print("okay you can eat it")
        elif choice in no:
           print("dont eat it theny")
        else:
           print ("Please respond with 'yes' or 'no'\n")


#functions
def f_ask_yes_no(question):
    """Ask a yes or no question"""
    vResponse = none
    while vResponse not in ("y","n"):
        vResponse = input(question).lower()
    return vResponse

#main program

vQuestion = "Would you like a Mars Bar?"
vAnswer = f_ask_yes_no(vQuestion)

if vAnswer == "y":
    print("Here is a mars bar.")
if vAnswer == "n":
    print("No Mars Bar for you")



