MENU = {
    "espresso": {
        "ingredients": {
            "water": 250,
            "coffee": 100,
        },
        "cost": 75,
        "orders": 0,
    },
    "latte": {
        "ingredients": {
            "water": 355,
            "milk": 250,
            "coffee": 150,
        },
        "cost": 125,
        "orders": 0,
    },
    "cappuccino": {
        "ingredients": {
            "water": 500,
            "milk": 350,
            "coffee": 200,
        },
        "cost": 300,
        "orders": 0,
    },
}


def get_menu(choices: bool) -> dict | str:
    # new_dict = {idx: key for idx, key in enumerate(MENU.keys())}
    coffee_choices = dict(enumerate(MENU.keys(), start=1))

    return (
        coffee_choices
        if choices
        else "\n".join(
            f"{key}: {value.title()} @{MENU[value]["cost"]}"
            for key, value in coffee_choices.items()
        )
    )


if __name__ == "__main__":
    print(get_menu(True))
    print(get_menu(False))
