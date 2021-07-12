# Number guessing game

import random

"""
1. Random number in a range
2. Capture guess
3. Evaluate user guess

command line game provide user messages

"""

game_random_number = random.randint(1, 100)
game_active = True

while game_active:
    game_start_message = "Guess a number between 1 - 100: "
    user_guess = int(input())
    if user_guess == game_random_number:
        print("You guessed correctly!")
        game_active = False
    elif user_guess < game_random_number:
        print("Too low, guess again")
    else:
        print("Too high, guess again")

