from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def coffee_machine():
    menu = Menu()
    coffeeMaker = CoffeeMaker()
    moneyMachine = MoneyMachine()
    running = True

    while running:
        coffeeChoice = input(f"What type of drink would you like? ({menu.get_items()}): ").lower()
        if coffeeChoice == "off":
            running = False
        elif coffeeChoice == "report":
            coffeeMaker.report()
            moneyMachine.report()

        else:
            coffee = menu.find_drink(coffeeChoice)

            if coffeeMaker.is_resource_sufficient(coffee):
                if moneyMachine.make_payment(coffee.cost):
                    coffeeMaker.make_coffee(coffee)

coffee_machine()