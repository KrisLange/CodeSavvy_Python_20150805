################################################################################
##                                                                            ##
##   Title:     NumberGame_4.py                                               ##
##   Author:    Kris Lange                                                    ##
##                                                                            ##
##   Description: A simple, text-based number guessing game                   ##
##                    Asks player to guess a number until the                 ##
##                    player guesses correctly or types "quit"                ##
##                    into the console                                        ##
##                                                                            ##
################################################################################

# asks python to use the random library of code
import random

# sets random_number to be a random integer between 0 and 10
random_number = random.randint(0, 10)

# defines the maximum number of tries
max_tries = 5

# num_tries will keep track of how many guesses have been done
num_tries = 0


# prompts the user for a guess, saves guess in response
response = input("Guess a number between 0 and 10:\t")

# converts the response to an integer, saves in guess
guess = int(response)

# increments num_tries by 1 because we made a guess
num_tries = num_tries + 1


# repeats the indented code while the guess is no equal to the answer
#   AND we have not exceeded the maxiumum number of guesses.
while guess != random_number and num_tries < max_tries:
    response = input("Wrong, Guess a number between 0 and 10:\t")
    guess = int(response)
    num_tries = num_tries + 1

# Prints the answer after either the max number of guesses or a correct guess
print("The number was ", random_number)