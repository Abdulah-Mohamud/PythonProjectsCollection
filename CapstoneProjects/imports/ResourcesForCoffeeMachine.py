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

money_box = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
machine_status = True


while machine_status:
    command = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if command == "off":
        machine_status = False

    elif command == "report":
        print(f"Water is {resources['water']}ml")
        print(f"Milk is {resources['milk']}ml")
        print(f"Coffee is {resources['coffee']}ml")
        print(f"Profit is £{money_box}")

    else:
        drink = MENU[command]


