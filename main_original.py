# Import modules
import menu
import resources as resource

# declare and initialize global variables
ONE = 1
FIVE = 5
TEN = 10
TWENTY = 20
sales = 0
machine_off = False


# TODO: 1 Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
def prompt():
    return input(
        "What would you like? (espresso P75/latte P125/cappuccino P300): "
    ).lower()


# TODO: 2 Turn off the Coffee Machine by entering “off” to the prompt
def turnOff():
    global machine_off
    print("Machine Shutting Down... \nThank you very much")
    machine_off = True


# TODO: 3 Print report
def report():
    global sales
    resource_water, resource_milk, resource_coffee = resource.resources.values()
    # espresso_order, latte_order, cappuccino_order = menu.MENU[*][2].values()
    print("The current resources values are:")
    print(f"Water: {resource_water} ml.")
    print(f"Milk: {resource_milk} grams")
    print(f"Coffee: {resource_coffee} grams")
    print(f"Money: P{round(sales,2)}")
    print("Coffee Order Transaction Record")

    # view coffee order records
    for id, info in menu.MENU.items():
        for key in info:
            if key == "orders":
                print(f"{id} : {info[key]}")


# TODO: 4 Check resources sufficient?
def checkResources(coffee_order):
    resource_water, resource_milk, resource_coffee = resource.resources.values()

    if coffee_order == "espresso":
        order_water, order_coffee = menu.MENU[f"{coffee_order}"]["ingredients"].values()

        if int(resource_water) < int(order_water):
            print("Sorry there is not enough water.")
            return False
        elif int(resource_coffee) < int(order_coffee):
            print("Sorry there is not enough coffee.")
            return False
        else:
            return True

    else:
        order_water, order_milk, order_coffee = menu.MENU[f"{coffee_order}"][
            "ingredients"
        ].values()
        if int(resource_water) < int(order_water):
            print("Sorry there is not enough water.")
            return False
        elif int(resource_milk) < int(order_milk):
            print("Sorry there is not enough coffee.")
            return False
        elif int(resource_coffee) < int(order_coffee):
            print("Sorry there is not enough coffee.")
            return False

        return True


# TODO: 5 Process coins
def processCoins():
    one = int(input("How many 1 peso?: "))
    five = int(input("How many 5 peso?: "))
    ten = int(input("How many 10 peso?: "))
    twenty = int(input("How many 20 peso?: "))

    one_total = one * ONE
    five_total = five * FIVE
    ten_total = ten * TEN
    twenty_total = twenty * TWENTY

    return one_total + five_total + ten_total + twenty_total


# TODO: 6 Check transaction successful?
def checkTrans(coins, order_coffee):
    global sales
    coffee_price = menu.MENU[f"{order_coffee}"]["cost"]

    print(f"The coffee price is P{coffee_price}")
    print(f"You give P{round(coins,2)}")

    if coffee_price > coins:
        print("Sorry that's not enough money. Money refunded")
        return False
    else:
        sales += coffee_price
        if coins > coffee_price:
            change = coins - coffee_price
            print(f"Here is P{round(change, 2)} as change")
        return True


# TODO:7 Make Coffee
def makeCoffee(coffee):
    resource_water, resource_milk, resource_coffee = resource.resources.values()
    if coffee == "espresso":
        order_water, order_coffee = menu.MENU[f"{coffee}"]["ingredients"].values()
        order_milk = 0
    else:
        order_water, order_milk, order_coffee = menu.MENU[f"{coffee}"][
            "ingredients"
        ].values()

    resource.resources["water"] = resource_water - order_water
    resource.resources["milk"] = resource_milk - order_milk
    resource.resources["coffee"] = resource_coffee - order_coffee

    menu.MENU[f"{coffee}"]["orders"] += 1


def main():
    while not machine_off:
        user_order = prompt()

        if (
            user_order == "espresso"
            or user_order == "latte"
            or user_order == "cappuccino"
        ):
            check_resource = checkResources(f"{user_order}")

            if check_resource:
                input_coins = processCoins()
                trans = checkTrans(input_coins, user_order)
                if trans:
                    makeCoffee(user_order)
                    print("“Here is your latte ☕. Enjoy!")

        elif user_order == "off":
            turnOff()
        elif user_order == "report":
            report()
        else:
            print("Please choose from espresso/latte/cappuccino only.")


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    main()
