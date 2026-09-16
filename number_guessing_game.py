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
    
    
