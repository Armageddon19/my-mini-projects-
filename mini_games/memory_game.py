#Memory game by ARMAGGEDON

import random
import time
import os

minimun = 1
maximun = 9
score = 0  # Initialize the score

while True:
    number = str(random.randint(minimun, maximun))
    print(f"Remember the number {number}...")
    time.sleep(1.5)
    os.system('cls' if os.name == 'nt' else 'clear')  
    attempt = input('Introduce the number: ')

    if attempt == number:
        print("YES, you guessed it")
        score += 1  # Increase score for a correct guess
        minimun *= 10
        maximun *= 10
    else:
        print("WRONG, The number is:", number)
        break

# Display the final score after the game ends
print(f"Game Over! Your final score is: {score}")
