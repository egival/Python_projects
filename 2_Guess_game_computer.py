"""
Guess number game, where the computer chooses a number and the user has to guess it.
"""

import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0

    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess > random_number:
            print(f"Sorry, your guess is too high. Try again")
        elif guess < random_number:
            print(f"Sorry, your guess is too low. Try again")

    print(f"Your guess is correct! The number is {random_number}. Congratulations!")

guess(10)
