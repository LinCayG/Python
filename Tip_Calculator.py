print('Hello, we are going to calculate the tip and let you know what each person should pay in your party')
bill = float(input('What is the total amount of the bill? $'))
tipPercent = float(input('What percentage tip would you like to give (please enter a whole number between 0 and 100)? '))
numPeople = int(input('How many people are splitting the bill? '))
tipCalc = "{:.2f}".format(bill*tipPercent/100)
splitCalc = "{:.2f}".format((bill+(bill*tipPercent/100))/numPeople)
print(f'The total tip amount for the server is ${tipCalc} and each person should pay ${splitCalc}.')
