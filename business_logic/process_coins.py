from presentation.user_input import get_user_input

sales: int = 0

coins: dict[str, dict] = {
    "one": {"amount": 1, "quantity": 0},
    "five": {"amount": 5, "quantity": 0},
    "ten": {"amount": 10, "quantity": 0},
    "twenty": {"amount": 20, "quantity": 0},
}


# TODO: 5 Process coins
def process_coins() -> None:
    global coins
    while True:
        try:
            for value in coins.values():
                value["quantity"] = int(
                    get_user_input(f"How many {value.get('amount')} peso?")
                )
            break
        except ValueError:
            print("Please enter a number only.")


def get_coins_total() -> int:
    # total = 0
    # for value in coins.values():
    #     total += value["amount"] * value["quantity"]
    # return total
    return sum(value["amount"] * value["quantity"] for value in coins.values())


def coins_reset() -> None:
    for value in coins.values():
        value["quantity"] = 0


def get_change(money: int, coffee_price: int) -> int:
    global sales
    if coffee_price <= money:
        sales += coffee_price
        return money - coffee_price if money > coffee_price else 0
    coins_reset()
    return 0
