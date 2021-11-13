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


current_water = resources["water"] = 500
current_milk = resources["milk"] = 500
current_coffee = resources["coffee"] = 500
money = 0


def check_resources(c_choice):
    """Takes input coffee choice. Compares ingredients for choice against available resources."""
    if c_choice == "espresso":
        choice_water = MENU[c_choice]["ingredients"]["water"]
        choice_coffee = MENU[c_choice]["ingredients"]["coffee"]
        print(choice_water, choice_coffee)
        if choice_water > current_water:
            print("Sorry there is not enough water.")
            return True
        if choice_coffee > current_coffee:
            print("Sorry there is not enough coffee.")
            return True
    else:
        choice_milk = MENU[c_choice]["ingredients"]["milk"]
        choice_water = MENU[c_choice]["ingredients"]["water"]
        choice_coffee = MENU[c_choice]["ingredients"]["coffee"]
        print(choice_water, choice_milk, choice_coffee)
        if choice_water > current_water:
            print("Sorry there is not enough water.")
            return True
        if choice_coffee > current_coffee:
            print("Sorry there is not enough coffee.")
            return True
        if choice_milk > current_milk:
            print("Sorry there is not enough milk")
            return True
    print(resources)


def process_coins(c_choice):
    print("Please inset coins.")
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickles = float(input("How many nickles?: "))
    pennies = float(input("How many pennies?: "))
    amount = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    print(amount)
    return amount

turn_machine_off = False

while not turn_machine_off:
    # 1. Ask user what coffee they'd like

    coffee_choice = input("What would you like? (espresso/latte/cappuccino): ")

    # 2. Turn off the coffee machine. Use "off" to end execution.
    if coffee_choice == "off":
        turn_machine_off = True

    # 3. Print report of current resource values
    elif coffee_choice == "report":
        print(f"Water: {current_water}")
        print(f"Milk: {current_milk}")
        print(f"Coffee: {current_coffee}")
        print(f"Money: {money}")

    # 4. Check if resources are sufficient when user chooses a drink.
    elif coffee_choice == "espresso":
        check_resources("espresso")
        turn_machine_off = check_resources("espresso")
    elif coffee_choice == "latte":
        check_resources("latte")
        turn_machine_off = check_resources("latte")
    elif coffee_choice == "cappuccino":
        check_resources("cappuccino")
        turn_machine_off = check_resources("cappuccino")



    # If the user has enetered enough money the amount gets added to money for the machine.
    process_coins(coffee_choice)
