################################################################################
##                                                                            ##
##   Title:     NumberGame_3.py                                               ##
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
# and WHILE that guess does not equal random_number
# keep prompting the user for a new guess
while guess != random_number:
    response = input("Wrong, Guess a number between 0 and 10:\t")
    guess = int(response)

# Print what the number was
print("The number was ", random_number)