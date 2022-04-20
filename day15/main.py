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
    "money": 0
}


def insert_coins(coffee_choice, menu_items):
    print(f"A {coffee_choice} will cost you ${menu_items[coffee_choice]['cost']:.2f}")
    total_cost = menu_items[coffee_choice]['cost']
    quarters = int(input("How many quarters? ")) * .25
    dimes = int(input("How many dimes? ")) * .10
    nickles = int(input("How many nickles? ")) * .05
    pennies = int(input("How many pennies? ")) * .01
    change_given = quarters + dimes + nickles + pennies

    if total_cost > change_given:
        print(f"Sorry, {change_given:.2f} is not enough money. Money refunded. Please try again!")
        return False
    else:
        print(f"Looks like you have some change, here's ${change_given - total_cost:.2f} back!")
        return True


def show_resources(resources_left):
    """Prints the total resources left"""

    for type in resources_left:
        if type == "coffee":
            print(f"{type.title()}: {resources_left[type]}g")
        elif type == "money":
            print(f"{type.title()}: ${resources_left[type]}")
        else:
            print(f"{type.title()}: {resources_left[type]}ml")


def choose_coffee(resources_left):
    """Lets user choose what coffee they want"""

    coffee = ''
    wrong_input = True
    while wrong_input:
        coffee = input("What would you like? (Espresso / Latte / Cappuccino): ").lower()
        if coffee == "espresso" or coffee == "latte" or coffee == "cappuccino":
            return coffee
        elif coffee == 'report':
            show_resources(resources_left)
        else:
            coffee = input("What would you like? (Espresso / Latte / Cappuccino): ").lower()


def change_resources(coffee_choice, menu_items, resources_left):
    """Takes user's coffee choice and check if there are enough resources, if there are
    then subtracts resources from the resources that are available"""

    for key in menu_items[coffee_choice]:
        if key == "ingredients":
            for ingredient in menu_items[coffee_choice]["ingredients"]:
                resources_left[ingredient] -= menu_items[coffee_choice]["ingredients"][ingredient]
        else:
            resources_left["money"] += menu_items[coffee_choice][key]


def is_transaction_possible(coffee_choice, menu_items, resources_left):
    """Checks if the desired order is even possible"""
    resources_copy = resources_left.copy()
    change_resources(coffee_choice, menu_items, resources_copy)

    for key in resources_copy:
        if key == "money":
            continue
        elif resources_copy[key] < 0:
            print(f"Sorry, you can't order because we don't have enough {key}.")
            return False
    return True


def coffee_machine():
    ordering = True
    enoughChange = True
    while ordering:
        possible = True
        coffeeChoice = choose_coffee(resources)
        enoughChange = insert_coins(coffeeChoice, MENU)
        if coffeeChoice == "off":
            return

        elif enoughChange:
            possible = is_transaction_possible(coffeeChoice, MENU, resources)
            if possible:
                change_resources(coffeeChoice, MENU, resources)


coffee_machine()