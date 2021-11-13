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

#Test2

def check_resources(c_choice):
    print(MENU[c_choice])

turn_machine_off = False

while not turn_machine_off:
    # TODO: 1. Ask user what coffee they'd like

    coffee_choice = input("What would you like? (espresso/latte/cappuccino): ")

    # TODO: 2. Turn off the coffee machine. Use "off" to end execution.

    if coffee_choice == "off":
        turn_machine_off = True

    # TODO: 3. Print report of current resource values
    elif coffee_choice == "report":
        for r in resources:
            print(f"{r}: {resources[r]}")

    # TODO: 4. Check if resources are sufficient when user chooses a drink.

    elif coffee_choice == "espresso":
        check_resources("espresso")
