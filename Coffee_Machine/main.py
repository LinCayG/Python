MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def check_supply(ingredient):


turn_on = True
while turn_on:
    #TODO prompt user for coffee
    print("Coffee Machine Menu \nEspresso: $1.50 \nLatte: $2.50 \nCappuccino: $3.00")
    cust_order = input("What would you like? Please type espresso, latte or cappuccino: ").lower()
    #TODO Print a report of all of the coffee machine resources
    if cust_order == 'report':
        print(resources)
    #TODO turn off the coffee machine by entering "off" to the prompt to end your program
    elif cust_order == 'off':
        turn_on = False
    else:
    # TODO Check resources sufficient to make drink order
        selection = MENU[cust_order]
        check_supply(selection)
    #TODO process coins
    #TODO Check to see if the transaction was successful (checks money entered and give change)
    #TODO Make the coffee and subtract that from the resources
