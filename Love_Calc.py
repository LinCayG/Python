print("Welcome to the Love Calculator!  We are going to determine how compatible you are with your crush by a super non-scientific method.")
name1 = input("What is your first and last name? \n")
name1Low = name1.lower()
name2 = input("What is your crush's first and last name? \n")
name2Low = name2.lower()
nameCat = name1Low+name2Low
T = nameCat.count("t") #counts number of T
R = nameCat.count("r") #counts number of R
U = nameCat.count("u") #counts number of U
L = nameCat.count("l") #counts number of L
O = nameCat.count("o") #counts number of O
V = nameCat.count("v") #counts number of V
E = nameCat.count("e") #counts number of E
score1 = T+R+U+E
score2 = L+O+V+E
conCatScore = str(score1)+str(score2)
scoreInt = int(conCatScore)
if scoreInt < 10 or scoreInt > 90:
    print(f'Your score is {scoreInt}, you go together like coke and mentos.')
elif 40 < scoreInt < 50:
    print(f'Your score is {scoreInt}, you are alright together.')
else:
    print(f'Your score is {scoreInt}.')

