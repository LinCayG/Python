import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

ascii = [rock, paper, scissors]
print('Let\'s play paper, rock, scissors against the computer!')
choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: \n'))
if choice >= 3 or choice < 0:
    print('You typed an invalid choice.  You lose!')
else:
    print('You chose: ')
    print(ascii[choice])
    compChoice = random.randint(0,2)
    print('The computer chose: ')
    print(ascii[compChoice])
    if choice ==0 and compChoice == 2:
        print('You win!')
    elif choice == 2 and compChoice == 0:
        print('You lose!')
    elif compChoice < choice:
        print('You win!')
    elif compChoice > choice:
        print('You lose!')
    elif compChoice == choice:
        print('It\'s a draw!')

