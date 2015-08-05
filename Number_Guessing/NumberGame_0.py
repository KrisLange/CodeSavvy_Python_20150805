################################################################################
##                                                                            ##
##   Title:     NumberGame_0.py                                               ##
##   Author:    Kris Lange                                                    ##
##                                                                            ##
##   Description: Step 0 in making a number-guessing game                     ##
##                    Generates a random integer between 0 and 10             ##
##                    and prints the value to the screen                      ##
##                                                                            ##
################################################################################

# Asks python to provide the random-number-generating code
import random

# Sets random_number to a random integer between 0 and 10
random_number = random.randint(0, 10)

# Displays the random number
print(random_number)