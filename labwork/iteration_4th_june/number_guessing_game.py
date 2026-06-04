# program for guess the number game
 
import random
number_to_guess = random.randint(1,50) 
attempts = 0
print("Welcome to the Number Guessing Game!")

# loop until the user guesses the correct number

while True:
    user_guess = int(input("guess a number between 1 to 50:"))
    attempts += 1
    if user_guess == number_to_guess:
        print("Congratulations! You guessed the correct number.")
        print(f"It took you {attempts} attempts.")
        break
    elif user_guess < number_to_guess:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")