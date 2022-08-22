print('Welcome to the Pizza Place! \n Here is the menu and prices: \n Small Pizza: $15 \n Medium Pizza: $20 \n Large Pizza: $25 \n Pepperoni for Small Pizza: +$2 \n Pepperoni for Medium/Large Pizza: +$3 \n Extra cheese for any size pizza: +$1')
order = input('Would you like to place an order? Y or N: ')
if order.upper() == 'N':
    print('Thanks for stopping by!')
elif order.upper() == 'Y':
    size = input('What size pizza do you want? S, M, or L: ')
    if size.upper() == 'S':
        bill = 15
    if size.upper() == 'M':
        bill = 20
    if size.upper() == 'L':
        bill = 25
    add_pep = input('Do you want pepperoni? Y or N: ')
    extra_cheese = input('Do you want extra cheese? Y or N: ')
    if extra_cheese.upper() == 'Y':
        bill+=1
    if add_pep.upper() == 'Y':
       if size.upper() == 'S':
          bill += 2
       if size.upper() == 'M':
          bill += 3
       if size.upper() == 'L':
          bill += 3
    print(f'Your final bill is: ${bill}.')
else:
    print('You did not enter a valid value.  Please try again later.')
