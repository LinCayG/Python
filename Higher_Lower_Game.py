#Random Number x2 for the beginning comparison list of entities, making sure the same number isnt picked at random

import random
from HL_game_data import data

length_data = len(data) #uses the length of the game data list - allows for expansion of game data later
Person1 = random.randint(0,length_data-1) #subtract by 1 since lists start their count at 0
Person2 = random.randint(0,length_data-1)
if Person1 == Person2: #ensures there will be 2 different entities to compare
    while Person1==Person2: #continues to loop until there are 2 different entities
        Person2 = random.randint(0,length_data)


#Bring up information about the celebrities from the dictionary
#take input on who is higher
#if statement to determine who has more followers and continue if user guessed correctly using the dictionary keys:value
#if user guessed correctly, have an ongoing count, with count = 0 to begin
#when user guesses wrong, print the number of correct guesses
#ask the user if they want to play again - use a while loop with a boolean
