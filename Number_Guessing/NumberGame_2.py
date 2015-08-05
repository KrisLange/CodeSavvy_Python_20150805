################################################################################
##                                                                            ##
##   Title:     NumberGame_2.py                                               ##
##   Author:    Kris Lange                                                    ##
##                                                                            ##
##   Description: A simple, text-based number guessing game                   ##
##                    Asks player to guess a number until the                 ##
##                    player guesses correctly or types "quit"                ##
##                    into the console                                        ##
##                                                                            ##
################################################################################

# Tells python that we would like to use the random library code
import random

# Sets random_number to a random integer between 0 and 10
random_number = random.randint(0, 10)

# Prompts user for input, stores input in response
#  then converts response to an integer
response = input("Guess a number between 0 and 10:\t")
guess = int(response)

# Checks if guess equals random_number
if guess == random_number:
    print("Correct!")
    exit(0)         #if correct, exit the program
else:
    print("Wrong!") #else, print wrong and continue

# Ask the user for another guess
response = input("Guess a number between 0 and 10:\t")
guess = int(response)

if guess == random_number:
    print("Correct!")
    exit(0)
else:
    print("Wrong!")

response = input("Guess a number between 0 and 10:\t")
guess = int(response)

if guess == random_number:
    print("Correct!")
    exit(0)
else:
    print("Wrong!")

response = input("Guess a number between 0 and 10:\t")
guess = int(response)

if guess == random_number:
    print("Correct!")
    exit(0)
else:
    print("Wrong!")

response = input("Guess a number between 0 and 10:\t")
guess = int(response)

if guess == random_number:
    print("Correct!")
    exit(0)
else:
    print("Wrong!")
