# Guess the number by ARMAGEDDON

import random

def guess_the_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    print("Welcome to the Guess the Number game!")
    print("I have selected a number between 1 and 100. Try to guess it.")

    attempts = 0
    max_attempts = 10

    while attempts < max_attempts:
        try:
            # Get player's guess
            guess = int(input("Enter your guess: "))
            attempts += 1

            # Check if the guess is correct
            if guess == secret_number:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                break
            elif guess < secret_number:
                print("Too low. Try again.")
            else:
                print("Too high. Try again.")
        except ValueError:
            print("Please enter a valid integer.")

    else:
        print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.")

if __name__ == "__main__":
    guess_the_number()
