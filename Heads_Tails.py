import random
input('We are going to toss a coin and see if it lands on Heads or Tails.  Press Enter to toss the coin.')
coin = random.randint(0,1)
if coin == 0:
    print('The coin landed on Heads.')
if coin == 1:
    print('The coin landed on Tails.')
