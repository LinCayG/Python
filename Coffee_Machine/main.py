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
profit = 0

def check_supply(ingredient):
    for item in ingredient:
        if ingredient[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def process_coins():
    """Returns total of coins inserted"""
    print("Please insert coins.")
    total = int(input("How many quarters?: "))*0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickels?: "))*0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def sub_resources(ingred):
    for thing in ingred:
        resources[thing] -= ingred[thing]


turn_on = True
while turn_on:
    #TODO prompt user for coffee
    print("Coffee Machine Menu \nEspresso: $1.50 \nLatte: $2.50 \nCappuccino: $3.00")
    cust_order = input("What would you like? Please type espresso, latte or cappuccino: ").lower()
    #TODO Print a report of all of the coffee machine resources
    if cust_order == 'report':
        print(f"Water: {resources['water']} mL")
        print(f"Milk: {resources['milk']} mL")
        print(f"Coffee: {resources['coffee']} g")
        print(f"Money: ${profit}")
    #TODO turn off the coffee machine by entering "off" to the prompt to end your program
    elif cust_order == 'off':
        turn_on = False
    else:
    # TODO Check resources sufficient to make drink order
        selection = MENU[cust_order]
        if check_supply(selection["ingredients"]):
    #TODO process coins
            payment = process_coins()
    #TODO Check to see if the transaction was successful (checks money entered and give change)
            if payment >= selection["cost"]:
                profit += selection["cost"]
                change = payment - selection["cost"]
                print(f"You paid {round(payment,2)}.  Your change is {round(change,2)}.  Here's your {cust_order}, enjoy!")
            # TODO Make the coffee and subtract that from the resources
                sub_resources(selection["ingredients"])
            else:
                print("Sorry, that is not enough money.  Money has been refunded.  Please place a new order.")

