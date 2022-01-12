# Contains helpers for dealing with data extracted from a raw recepie

from dataclasses import dataclass
import json
from typing import List

@dataclass
class Ingredient:
    count: float
    unit: str
    ingredient: str

    def __eq__(self, other):
        return self.count == other.count and self.unit == other.unit and self.ingredient == other.ingredient

    def to_serializable(self):
        return self.__dict__


@dataclass
class IngredientLink:
    """
    Stores a link to an ingredient, as well as some information
    about that ingredient that is useful for presenting other
    options to the user
    """
    ingredient: str
    link: str
    is_sponsored: bool
    is_store_choice: bool

    def to_serializable(self):
        return self.__dict__


@dataclass()
class IngredientPair:
    """
    Storing the mapping from one ingredient to other ingredients, and includes if
    is is currently included in the recipe
    """
    recipe_ingredient: Ingredient
    cart_ingredient: Ingredient
    other_ingredient_links: List[IngredientLink]
    toggle: bool # False if the ingredient is not in the cart

    def __repr__(self) -> str:
        return f'To order {self.recipe_ingredient.count}, {self.recipe_ingredient.unit}, {self.recipe_ingredient.ingredient}, ordered {self.cart_ingredient.count}, {self.cart_ingredient.unit}, {self.cart_ingredient.ingredient} with {len(self.other_ingredient_links)} other options.'

    def to_serializable(self):
        return {
            'recipe_ingredient': self.recipe_ingredient.to_serializable(),
            'cart_ingredient': self.cart_ingredient.to_serializable(),
            'other_ingredient_links': [
                link.to_serializable() for link in self.other_ingredient_links
            ],
            'toggle': self.toggle
        }

DEFAULT_NO_ADD_INGREDIENTS = [
    'water',
    'salt',
    'kosher salt',
    'pepper',
    'salt and pepper'
]