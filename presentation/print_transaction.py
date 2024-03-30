from .print_border import print_border


def print_transaction(money: int, coffee_price: int, change: int):
    print_border()
    print(f"The coffee price is P{coffee_price}")
    print(f"You give P{money}")
    if coffee_price > money:
        print("Sorry that's not enough money. Money refunded")
    elif change > 0:
        print(f"Here is P{change} as change.")
