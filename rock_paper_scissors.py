<<<<<<< HEAD
import random
list=["rock", "paper", "scissors"]
input = str(input("Rock Paper Scissors: ")).lower()
computer = random.choice(list)
if input == computer:
    print("It's a tie! The computer also chose", computer)
elif (input == "rock" and computer == "scissors") or (input == "paper" and computer == "rock") or (input == "scissors" and computer == "paper"):
    print("You win! The computer chose", computer)
elif input not in list:
    print("Invalid input! Please choose rock, paper, or scissors.")
else:
    print("You lose! The computer chose", computer)
=======
import random
list=["rock", "paper", "scissors"]
input = str(input("Rock Paper Scissors: ")).lower()
computer = random.choice(list)
if input == computer:
    print("It's a tie! The computer also chose", computer)
elif (input == "rock" and computer == "scissors") or (input == "paper" and computer == "rock") or (input == "scissors" and computer == "paper"):
    print("You win! The computer chose", computer)
elif input not in list:
    print("Invalid input! Please choose rock, paper, or scissors.")
else:
    print("You lose! The computer chose", computer)
>>>>>>> 0a6f158ba4a8147a70b63fca73b4e487919d997a
