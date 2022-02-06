from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_money_machine = MoneyMachine()
my_menu = Menu()
my_coffeemaker = CoffeeMaker()

is_on = True

while is_on:
    print(f"You can select from {my_menu.get_items()} items")
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        my_money_machine.report()
        my_coffeemaker.report()
    else:
        order = my_menu.find_drink(choice)

    can_make = my_coffeemaker.is_resource_sufficient(order)
    if can_make:
        payment = my_money_machine.make_payment(order.cost)
        if payment:
            my_coffeemaker.make_coffee(order)

