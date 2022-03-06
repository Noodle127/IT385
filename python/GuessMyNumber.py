#!/usr/bin/python3
import random

guesses_taken = 0
while guesses_taken < 5:

    random_number = random.randint(1, 10)
    print(random_number)
    user_guess = int(input("Choose a number between 1 and 10: "))
    guesses_taken += 1

    if user_guess == random_number:
        print("Congratulations! The number was " + str(random_number)
        + " and you guessed " + str(user_guess) + "!")
        break

    if user_guess < random_number:
        print("Too low, try again.")

    if user_guess > random_number:
        print ("Too high, try again.")

if user_guess != random_number:
    print("Too many guesses. The number was " + str(random_number))