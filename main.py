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


def check_resources(c_choice):
    """Takes input coffee choice. Compares ingredients for choice against available resources.
    Returns False if resources insufficient"""
    for item in c_choice:
        if c_choice[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

    # print(resources)


def process_coins():
    """Returns total calculated from coins inserted"""
    print("Please inset coins.")
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickles = float(input("How many nickles?: "))
    pennies = float(input("How many pennies?: "))
    amount = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    # print(amount)
    return amount

def is_transaction_successful(money_received, drink_cost):
    """Return True when the paayment is accepted, or False if moeny is insufficient"""
    # 6. Check transaction successful. Compare money user inserted to cost of coffee.
    if money_received >= drink_cost:
        change = round(money_received - drink_cost,2)
        print(f"Here is ${change} in change.")
        global money
        money += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredientsf rom the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ")

turn_machine_off = False
current_water = resources["water"]
current_milk = resources["milk"]
current_coffee = resources["coffee"]
money = 0
enough_resources = True

while not turn_machine_off:
    # 1. Ask user what coffee they'd like
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    coffee_cost = 0
    # print(coffee_cost)

    # 2. Turn off the coffee machine. Use "off" to end execution.
    if choice == "off":
        turn_machine_off = True

    # 3. Print report of current resource values
    elif choice == "report":
        print(f"Water: {current_water}")
        print(f"Milk: {current_milk}")
        print(f"Coffee: {current_coffee}")
        print(f"Money: {money}")

    # 4. Check if resources are sufficient when user chooses a drink.
    else:
        coffee_cost = MENU[choice]["cost"]
        drink = MENU[choice]
        if check_resources(drink["ingredients"]):
            # 5. If there are enough resources then the user should insert coins. Calculate the total value of coins inserted.
            payment = process_coins()
            if is_transaction_successful(payment, coffee_cost):
                make_coffee(choice, drink["ingredients"])
