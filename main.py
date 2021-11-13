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
    """Takes input coffee choice. Compares ingredients for choice against available resources."""
    if c_choice == "espresso":
        choice_water = MENU[c_choice]["ingredients"]["water"]
        choice_coffee = MENU[c_choice]["ingredients"]["coffee"]
        # print(choice_water, choice_coffee)
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
        # print(choice_water, choice_milk, choice_coffee)
        if choice_water > current_water:
            print("Sorry there is not enough water.")
            return True
        if choice_coffee > current_coffee:
            print("Sorry there is not enough coffee.")
            return True
        if choice_milk > current_milk:
            print("Sorry there is not enough milk")
            return True
    # print(resources)


def process_coins(c_choice):
    print("Please inset coins.")
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickles = float(input("How many nickles?: "))
    pennies = float(input("How many pennies?: "))
    amount = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    # print(amount)
    return amount


turn_machine_off = False
current_water = resources["water"] = 500
current_milk = resources["milk"] = 500
current_coffee = resources["coffee"] = 500
money = 0
report_check = True

while not turn_machine_off:
    # 1. Ask user what coffee they'd like
    coffee_choice = input("What would you like? (espresso/latte/cappuccino): ")
    coffee_cost = 0
    # print(coffee_cost)

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
        coffee_cost = MENU[coffee_choice]["cost"]
        check_resources("espresso")
        turn_machine_off = check_resources("espresso")
    elif coffee_choice == "latte":
        coffee_cost = MENU[coffee_choice]["cost"]
        check_resources("latte")
        turn_machine_off = check_resources("latte")
    elif coffee_choice == "cappuccino":
        coffee_cost = MENU[coffee_choice]["cost"]
        check_resources("cappuccino")
        turn_machine_off = check_resources("cappuccino")
    # print(coffee_choice)

    # 5. If there are enough resources then the user should insert coins. Calculate the total value of coins inserted.
    if coffee_choice != "report":
        coins_amount = process_coins(coffee_choice)

    # 6. Check transaction successful. Compare money user inserted to cost of coffee.
    if coffee_choice != "report":
        if coins_amount < coffee_cost:
            print("Sorry that's not enough money. Money refunded.")
        elif coins_amount == coffee_cost:
            print("You've purchases coffee. No change.")
        else:
            coffee_change = round(coins_amount - coffee_cost, 2)
            print(f"Here is ${coffee_change} in change.")

    # 7. Make the coffee. Deduct resources based on coffee selected. Then print your is your "drink" enjoy.
    # Add cost of coffee to money.
    if coffee_choice == "espresso":
        choice_water = MENU[coffee_choice]["ingredients"]["water"]
        choice_coffee = MENU[coffee_choice]["ingredients"]["coffee"]
        current_water -= choice_water
        current_coffee -= choice_coffee
        # print(current_water)
    elif coffee_choice != "report":
        choice_milk = MENU[coffee_choice]["ingredients"]["milk"]
        choice_water = MENU[coffee_choice]["ingredients"]["water"]
        choice_coffee = MENU[coffee_choice]["ingredients"]["coffee"]
        current_water -= choice_water
        current_coffee -= choice_coffee
        current_milk -= choice_milk
        # print(choice_water, choice_milk, choice_coffee)
    # print(resources)
    if coffee_choice != "report":
        money += coffee_cost
        print(f"Here is your {coffee_choice}, enjoy!")
