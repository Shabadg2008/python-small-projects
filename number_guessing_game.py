<<<<<<< HEAD
import random 
ans= random.randint(1,100)
guess = int(input("Guess a number between 1 and 100: "))
while guess != ans:
    if guess < ans:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    guess = int(input("Guess a number between 1 and 100: "))

if guess == ans:
    print("Congratulations! You guessed the correct number.")
    
    
=======
import random 
ans= random.randint(1,100)
guess = int(input("Guess a number between 1 and 100: "))
while guess != ans:
    if guess < ans:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    guess = int(input("Guess a number between 1 and 100: "))

if guess == ans:
    print("Congratulations! You guessed the correct number.")
    
    
>>>>>>> 0a6f158ba4a8147a70b63fca73b4e487919d997a
