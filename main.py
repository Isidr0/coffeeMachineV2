import ingredients as ingredients

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

choice = input("What would you like? (espresso/latte/cappuccino): ")
drink = MENU[choice]

def check_resources(drink):
    """Takes input coffee choice. Compares ingredients for choice against available resources.
    Returns False if resources insufficient"""

    for item in drink:
        print("item", item)
        print("drink", drink)
        print("drink/item", drink[item])
        print("resource item", resources[item])
        if drink[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

check_resources(drink["ingredients"])