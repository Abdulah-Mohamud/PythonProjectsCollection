from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_coffee_machine = CoffeeMaker()
my_money_machine = MoneyMachine()
#my_menu_item = MenuItem()
my_menu = Menu()

is_on = True
while is_on:
    command = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if command == "report":
        my_coffee_machine.report()
        my_money_machine.report()
    elif command == "off":
        is_on = False
    else:
        drink = my_menu.find_drink(command)
        if my_coffee_machine.is_resource_sufficient(drink):

        print(a)


