from menu import MENU
from resources import resources


# TODO: 4 Check resources sufficient?
def get_available_resources() -> dict[str, int]:
    # _resources = {}
    # for key, value in resources.items():
    #     _resources[key] = value.get("quantity")

    # return {key: value.get("quantity") for key, value in resources.items()}
    return {key: value["quantity"] for key, value in resources.items()}


def get_coffee_ingredients(coffee: str) -> dict[str, int]:
    # return MENU.get(coffee).get("ingredients")
    return MENU[coffee]["ingredients"]


def is_resources_enough(resources: dict, ingredients: dict) -> bool:
    # for key, value in ingredients.items():
    #     if int(resources.get(key)) < int(value):
    #         return False
    # return True
    return all(
        int(resources.get(key)) >= int(value) for key, value in ingredients.items()
    )


def check_resources(coffee: str) -> bool:
    # available_resources: dict[str, int] = get_available_resources()
    # coffee_ingredients: dict[str, int] = get_coffee_ingredients(coffee)
    # return is_resources_enough(available_resources, coffee_ingredients)
    return is_resources_enough(
        get_available_resources(), get_coffee_ingredients(coffee)
    )
