from business_logic.report import report
from business_logic.check_resources import (
    get_available_resources,
    get_coffee_ingredients,
    is_resources_enough,
)
from business_logic.make_coffee import make_coffee
from business_logic.process_coins import process_coins, get_coins_total, get_change
from menu import MENU, get_menu
from presentation.print_border import print_border
from presentation.print_transaction import print_transaction
from presentation.user_input import get_order_coffee


coffee_choices: dict[int, str] = get_menu(choices=True)
is_machine_off: bool = False


def machine_off() -> None:
    global is_machine_off
    print("Machine Shutting Down... \nThank you very much")
    is_machine_off = True


def main_prompt() -> str:
    while True:
        print_border()
        if value := input(
            "What would you like to do? \n1: Make Coffee \n2: Report \n3: Exit \nEnter your choice: "
        ):
            return value


def prepare_coffee_order():
    coffee = coffee_choices.get(get_order_coffee())
    available_resources = get_available_resources()
    coffee_ingredients = get_coffee_ingredients(coffee)

    if is_resources_enough(available_resources, coffee_ingredients):
        process_coffee_order(coffee)
    else:
        print(f"{coffee.title()} is not available")


def process_coffee_order(coffee):
    print(f"{coffee.title()} is available.")
    process_coins()
    total_money = get_coins_total()
    coffee_price = MENU[f"{coffee}"]["cost"]
    change = get_change(total_money, coffee_price)
    print_transaction(total_money, coffee_price, change)
    make_coffee(coffee)
    print(f"Here's your {coffee.title()}")


def invalid_input_action():
    return print("\nInvalid input. Please select from choices only.")


def main():
    actions: dict[str, callable] = {
        "1": prepare_coffee_order,
        "2": report,
        "3": machine_off,
    }

    while not is_machine_off:
        choice = main_prompt()
        action = actions.get(choice, invalid_input_action)
        if action():
            break


if __name__ == "__main__":
    main()
