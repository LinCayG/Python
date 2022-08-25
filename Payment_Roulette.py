import random
print('Who is going to pay the bill?  This program is going to randomly select someone to pay the bill.')
people = input('Please type everyone\'s names, separated by a comma: ')
names=people.split(",")
print(names)
bill = random.randint(0,len(names)-1)
print(names[bill]+ ' is going to be paying the bill today!')
