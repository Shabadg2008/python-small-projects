
import random
list=["rock", "paper", "scissors"]
while True:
    outcome = str(input("Rock Paper Scissors: ")).lower()
    computer = random.choice(list)
    if outcome == computer:
        print("It's a tie! The computer also chose", computer)
    elif (outcome == "rock" and computer == "scissors") or (outcome == "paper" and outcome == "rock") or (outcome == "scissors" and computer == "paper"):
        print("You win! The computer chose", computer)
    elif outcome not in list:
        print("Invalid input! Please choose rock, paper, or scissors.")
    else:
        print("You lose! The computer chose", computer)
    play_again = str(input("Do you want to play again? \n")).lower()
    if play_again == "no":
        print("Thanks for playing")
        break





