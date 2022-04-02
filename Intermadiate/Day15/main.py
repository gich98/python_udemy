import data
from logic import print_report, get_flavours, make_coffee, check_resources, process_coins

machine_on = True
resources = data.RESOURCES
menu = data.MENU
flavours = get_flavours(menu)

while machine_on:
    flavour = input("What would you like? (espresso/latte/cappuccino): ")
    if flavour in flavours:
        enough_resources = check_resources(menu[flavour]["ingredients"], resources)
        if enough_resources == "ok":
            change = round(process_coins(data.COINS, menu[flavour]["cost"]), 2)
            if change >= 0:
                if change != 0:
                    print(f"Here is ${change} in change.")
                make_coffee(menu[flavour], resources)
                print(f"Here is your {flavour} ☕️. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print(f"Sorry there is not enough {enough_resources}.")
    elif flavour == "report":
        print_report(resources)
    elif flavour == "off":
        machine_on = False
    else:
        print(f"The flavour {flavour} is not in the menu! Choice between: espresso, latte and cappuccino.")
