import data
from logic import print_report, get_flavours, make_coffee, check_resources, process_coins

machine_on = True
resources = data.RESOURCES
menu = data.MENU
flavours = get_flavours(menu)

while machine_on:
    flavour = input("What would you like? (espresso/latte/cappuccino): ")
    if flavour in flavours:
        # If the user inserted a flavour that is in the menu then proceed
        enough_resources = check_resources(menu[flavour]["ingredients"], resources)
        # Check if there is enough resources to make the coffee
        # Otherwise print the first resource unavailable
        if enough_resources == "ok":
            change = round(process_coins(data.COINS, menu[flavour]["cost"]), 2)
            # If there is enough coins inserted then make the coffee
            # Otherwise don't make the coffee
            if change >= 0:
                # If the user inserted too much money then offer the change
                if change != 0:
                    print(f"Here is ${change} in change.")
                make_coffee(menu[flavour], resources)
                print(f"Here is your {flavour} ☕️. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print(f"Sorry there is not enough {enough_resources}.")
    elif flavour == "report":
        # If the user inserted the secret key "report" then print the resources available
        print_report(resources)
    elif flavour == "off":
        # If the user inserted the secret key "off" then turn off the machine (end the program)
        machine_on = False
    else:
        # Otherwise, if the user inserted something not in the menu or is not a secret key then warn him
        print(f"The flavour {flavour} is not in the menu! Choice between: espresso, latte and cappuccino.")
