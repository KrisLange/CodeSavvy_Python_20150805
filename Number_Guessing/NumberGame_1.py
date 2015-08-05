################################################################################
##                                                                            ##
##   Title:     NumberGame_1.py                                               ##
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
response = input("Guess a number between 0 and 10:\t")

# Converts response to an integer
guess = int(response)

# Checks if guess equals random_number
if guess == random_number:
    # if the guess equals random_number
    print("Correct!")
else:
    # if the guess does not equal random_number
    print("Wrong! The number was ", random_number)