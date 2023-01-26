#Random Number x2 for the beginning comparison list of entities, making sure the same number isnt picked at random

import random
from HL_Logo import logo, vs
from HL_game_data import data
import os

score = 0
print(logo)
#Bring up information about the celebrities from the dictionary
def format_person(Person):
    Person_name = Person["name"]
    Person_descr = Person["description"]
    Person_country = Person["country"]
    return f"{Person_name}, a(n) {Person_descr}, from {Person_country}"

#if statement to determine who has more followers and continue if user guessed correctly using the dictionary keys:value
def follower_count(Count):
    Person_count = Count["follower_count"]
    return Person_count

game_should_continue = True
PersonB = random.choice(data)

while game_should_continue:

    PersonA = PersonB
    PersonB = random.choice(data)
    if PersonA == PersonB: #ensures there will be 2 different entities to compare
        while PersonA==PersonB: #continues to loop until there are 2 different entities
            PersonB = random.choice(data)

    #take input on who is higher
    print(f"Compare A: {format_person(PersonA)}.")
    print(vs)
    print(f"Against B: {format_person(PersonB)}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    os.system('cls')
    print(logo)

    FollowerA = follower_count(PersonA)
    FollowerB = follower_count(PersonB)
    winner = max(FollowerA, FollowerB)

    if guess == 'A':
        choice = FollowerA
    else:
        choice = FollowerB

    if winner == choice:
        is_correct = True
    else:
        is_correct = False

    if is_correct:
        score +=1
        print(f"You're right!  Current score: {score}.")
    else:
        print(f"Sorry, that's wrong.  Final score: {score}.")
        game_should_continue = False

