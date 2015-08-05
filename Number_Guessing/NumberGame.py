################################################################################
##                                                                            ##
##   Title:     NumberGame.py                                                 ##
##   Author:    Kris Lange                                                    ##
##                                                                            ##
##   Description: A simple, text-based number guessing game                   ##
##                    Asks player to guess a number until the                 ##
##                    player guesses correctly or types "quit"                ##
##                    into the console                                        ##
##                                                                            ##
################################################################################


# Asks python to provide the random-number-generating code
import random

# Sets answer to a random number between 0 and 10 (including 0 and 10)
answer = random.randint(0, 10)
print("A number between 0 and 10 has been picked")

# Asks the user to guess a number, saves that number as raw_guess
raw_guess = input("Guess a number:\t")

# Converts raw_guess into a whole number (integer -> int)
#     That number is saved as guess
guess = int(raw_guess)

# While the guess does not equal the answer, keep asking the user to guess
while guess != answer:
    raw_guess = input("Nope--Guess again:\t")
    guess = int(raw_guess)

# The user has guessed correctly, so congratulate them!
print("Correct! The number was " + str(answer))