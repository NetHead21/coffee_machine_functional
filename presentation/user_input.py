from menu import get_menu

from .print_border import print_border


# TODO: 1 Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
def get_user_input(label: str) -> str:
    # while True:
    #     if value := input(f"{label}: "):
    #         return value
    return input(f"{label}: ")


def get_order_coffee() -> int:
    while True:
        print_border()
        try:
            coffee = int(
                get_user_input(
                    f"What would you like? \n{get_menu(choices=False)}\nEnter your choice"
                )
            )
            if coffee in get_menu(choices=True):
                return coffee
            print("\nPlease select from choices only.")
        except ValueError:
            print("\nInvalid input. Please select from choices only.")


if __name__ == "__main__":
    get_order_coffee()
