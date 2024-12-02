#Game of rock paper scissors
import random

def computerChoice():
    selection = random.randrange(1,3)
    if selection == 1:
        return "Rock"
    if selection == 2:
        return "Paper"
    if selection == 3:
        return "Scissors"


def whoWins(computerChoice, userSelection):
    if computerChoice == "Rock" and userSelection == "Rock":
        return "Tie"
    if computerChoice == "Rock" and userSelection == "Paper":
        return "User"
    if computerChoice == "Rock" and userSelection == "Scissors":
        return  "Computer"
    if computerChoice == "Paper" and userSelection == "Rock":
        return "Computer"
    if computerChoice == "Paper" and userSelection == "Paper":
        return "Tie"
    if computerChoice == "Paper" and userSelection == "Scissors":
        return "User"
    if computerChoice == "Scissors" and userSelection == "Rock":
        return "User"
    if computerChoice == "Scissors" and userSelection == "Paper":
        return "Computer"
    if computerChoice == "Scissors" and userSelection == "Scissors":
        return "Tie"




def mainFunc():
    scoreComp = 0
    scoreUser = 0
    while True:
        userSelection = input("Type your choice, either 'Rock' 'Paper' or 'Scissors':")
        if userSelection not in ["Rock", "Paper", "Scissors"]:
            print("Invalid Input")
            return
        botChoice = computerChoice()
        print(f"Computer Choice: {botChoice}")
        winner = whoWins(botChoice, userSelection)

        if winner == "Computer":
            scoreComp += 1
        elif winner == "User":
            scoreUser += 1
        print(f"The winner is: {winner}")
        print(f"- {'You':<8}: {scoreUser}")
        print(f"- {'Computer':8}: {scoreComp}")   



print("Game Start, CTRL+C to stop the game")
mainFunc()



