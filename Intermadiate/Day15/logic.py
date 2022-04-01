
def print_report(resources):
    """
    Prints the resources available in the coffee machine
    :param resources: Dictionary of resources available in the machine
    :return: Print the amount of each resource
    """
    print(f"Water: {resources['water']}ml\n"
          f"Milk: {resources['milk']}ml\n"
          f"Coffee: {resources['coffee']}g\n"
          f"Money: ${resources['money']}")


def get_flavours(menu):
    """
    Gets the list of coffees flavours' name
    :param menu: Dictionary of coffees' flavours
    :return: List of coffees flavours' name
    """
    flavours = []
    for _ in menu:
        flavours.append(_)
    return flavours


def sum_coins(coins, coins_value):
    """
    Get the total value of the coins inserted by the user
    :param coins: Dictionary of coins inserted by the user
    :param coins_value: Dictionary of the value of each coin
    :return: Sum of the coins inserted by the user
    """
    total = 0
    for _ in coins_value:
        total += coins[_] * coins_value[_]
    return total


def check_resources(ingredients, resources):
    """
    Check if the resources are enough to make the coffee
    :param ingredients: Ingredients needed to make the coffee
    :param resources: Resources available in the coffee machine
    :return: Returns ok if the resources are enough, otherwise returns the resource that isn't enough
    """
    water_remain = resources["water"] - ingredients["water"]
    milk_remain = resources["milk"] - ingredients["milk"]
    coffee_remain = resources["coffee"] - ingredients["coffee"]
    if water_remain < 0:
        return "water"
    elif milk_remain < 0:
        return "milk"
    elif coffee_remain < 0:
        return "coffee"
    else:
        return "ok"


def make_coffee(flavour, resources):
    """
    Makes the coffee
    :param flavour: The flavour chosen by the user
    :param resources: Resources available in the machine
    :return: Null
    """
    resources["water"] -= flavour["ingredients"]["water"]
    resources["milk"] -= flavour["ingredients"]["milk"]
    resources["coffee"] -= flavour["ingredients"]["coffee"]
    resources["money"] += flavour["cost"]
