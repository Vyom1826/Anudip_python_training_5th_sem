# program for guess the number game
 
import random
number_to_guess = random.randint(1,100) 

# loop until the user guesses the correct number

while True:
    user_guess = int(input("guess a number between 1 to 100:"))
    if user_guess == number_to_guess:
        print("Congratulations! You guessed the correct number.")
        break
    elif user_guess < number_to_guess:
        print("low! Try again.")
    else:
        print("high! Try again.")