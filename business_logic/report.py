from typing import Any

from menu import MENU
from presentation.print_border import print_border
from resources import resources
from .process_coins import sales


# TODO: 3 Print report
def print_resources() -> None:
    print("\nCurrent resources values:")
    for key, value in resources.items():
        print(f"{key.title()}: {value.get('quantity')} {value.get('measurement')}.")


def print_orders_record() -> None:
    print("\nCoffee Orders:")
    for key, value in MENU.items():
        # print(f"{key.title()}: {value.get('orders')} orders.")
        print(f"{key.title()}: {value['orders']} orders.")


def report() -> None:
    print_border()
    print_resources()
    print_orders_record()
    print(f"\nTotal Sales: {sales: .2f}")


if __name__ == "__main__":
    report()
