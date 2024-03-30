from business_logic.check_resources import get_coffee_ingredients
from resources import resources
from menu import MENU


# TODO:7 Make Coffee
def deduct_resources(ingredients: dict) -> None:
    for key, value in ingredients.items():
        resources[key]["quantity"] -= value


def increase_orders(coffee: str) -> None:
    MENU[f"{coffee}"]["orders"] += 1


def make_coffee(coffee: str) -> None:
    deduct_resources(get_coffee_ingredients(coffee))
    increase_orders(coffee)
