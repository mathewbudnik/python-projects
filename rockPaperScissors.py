import random


userScore = 0
computerScore = 0

rock = "rock"
paper = "paper"
scissors = "scissors"
computerChoiceList = ["rock", "paper", "scissors"]

print("--------------------------------- Rock, Paper, Scissors! ---------------------------------\n")

while True:

    userChoice = input("What would you like to choose? Rock, Paper, or Scissors: \n")
    computerChoice = random.choice(computerChoiceList)

    if userChoice == computerChoice:
            print("Draw! Try again\n")

    if userScore != 2 and computerScore != 2:

        if userChoice == "rock" and computerChoice == "paper":
            computerScore += 1
            print("Paper beats rock, computer wins the round.\n ")

        if userChoice == "paper" and computerChoice == "scissors":
            computerScore += 1
            print("Scissors beats paper, computer wins the round.\n ")
        
        if userChoice == "scissors" and computerChoice == "rock":
            computerScore += 1
            print("Rock beats scissors, computer wins the round.\n ")
            
        if userChoice == "paper" and computerChoice == "rock":
            userScore += 1
            print("Paper beats rock, you win the round.\n ")

        if userChoice == "scissors" and computerChoice == "paper":
            userScore += 1
            print("Scissors beats paper, you win the round.\n ")

        if userChoice == "rock" and computerChoice == "scissors":
            userScore += 1
            print("Rock beats paper, you win the round.\n ")
            
    if userScore == 2:
        print("Nice Job! you won the game.")
        break

    if computerScore == 2:
        print("The computer won the game.")
        break




        