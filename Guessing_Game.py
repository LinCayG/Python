#Number Guessing Game
import random
from guessart import logo

def hard():
    hard_num = random.randint(1,100)
    attempt = 5
    while attempt > 0:
        print(f"You have {attempt} attempts remaining.")
        guess = int(input("Make a guess: "))
        if guess == hard_num:
            print(f"You have guessed the correct number, {hard_num}!")
            attempt = 0
        elif guess > hard_num:
            attempt -=1
            print("Too high!")
        else:
            print("Too low!")
            attempt -=1
    print(f"The game is over.  The number was {hard_num}.")

def easy():
    easy_num = random.randint(1,100)
    attempt = 10
    while attempt > 0:
        print(f"You have {attempt} attempts remaining.")
        guess = int(input("Make a guess: "))
        if guess == easy_num:
            print(f"You have guessed the correct number, {easy_num}!")
            attempt = 0
        elif guess > easy_num:
            attempt -=1
            print("Too high!")
        else:
            print("Too low!")
            attempt -=1
    print(f"The game is over.  The number was {easy_num}.")


replay = True
while replay is True:
    print(logo)
    difficulty = input("I'm thinking of a integer between 1 and 100. \nChoose a difficulty.  Type 'easy' or 'hard': ")

    if difficulty == 'hard':
        hard()
    else:
        easy()
    play_again = input("Would you like to play again? 'Y' or 'N': ").upper()
    if play_again == 'N':
        replay = False


