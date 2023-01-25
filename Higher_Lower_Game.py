#Random Number x2 for the beginning comparison list of entities, making sure the same number isnt picked at random

import random
from HL_Logo import logo, vs
from HL_game_data import data

print(logo)
PersonA = random.choice(data)
PersonB = random.choice(data)
if PersonA == PersonB: #ensures there will be 2 different entities to compare
    while PersonA==PersonB: #continues to loop until there are 2 different entities
        PersonB = random.choice(data)

#Bring up information about the celebrities from the dictionary
def format_person(Person):
    Person_name = Person["name"]
    Person_descr = Person["description"]
    Person_country = Person["country"]
    return f"{Person_name}, a(n) {Person_descr}, from {Person_country}"

#take input on who is higher
print(f"Compare A: {format_person(PersonA)}.")
print(vs)
print(f"Against B: {format_person(PersonB)}.")

guess = input("Who has more followers? Type 'A' or 'B': ").upper()
#if statement to determine who has more followers and continue if user guessed correctly using the dictionary keys:value
def follower_count(Count):
    Person_count = Count["follower_count"]
    return Person_count

FollowerA = follower_count(PersonA)
FollowerB = follower_count(PersonB)
winner = max(FollowerA, FollowerB)

if guess == 'A':
    choice = FollowerA
else:
    choice = FollowerB

if winner == choice:
    print('you won')
else:
    print('you lose')

#if user guessed correctly, have an ongoing count, with count = 0 to begin and assign the correct guess to PersonA
#when user guesses wrong, print the number of correct guesses
#ask the user if they want to play again - use a while loop with a boolean
