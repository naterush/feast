import json
import sys
import time
import Cart
from recipe import get_recipe_from_all_recipe_link
from recipe import get_raw_ingredients_from_all_recipe

ITEMS_TO_ORDER = [
    'radish',
    'carrot'
]


def main():

    cart = Cart.InstaCart('naterush1997@gmail.com', '../password-instacart.txt')
    time.sleep(5)
    cart.login()

    recipies = [
        'https://www.allrecipes.com/recipe/232268/easy-and-delicious-ham-and-potato-soup/',
        'https://www.allrecipes.com/recipe/64961/sauteed-mushrooms/',
        'https://www.allrecipes.com/recipe/240060/loaded-cauliflower/',
        'https://www.allrecipes.com/recipes/77/drinks/',
        'https://www.allrecipes.com/recipe/246866/rigatoni-alla-genovese/',
    ]

    for url in recipies:
        cart.add_recipe(url)

    
if __name__ == '__main__':
    main()


# TODO:
# - Actually order the correct number of items
# - Go through checkout properly? Get the 

# - Get the changing of the number of items fixed
# - Then, get the actual ordering working. Make it so you can go through a full checkout flow:
#   - Allow the user to pass the delivery date and time
#   - Allow the user to specify the address? No. Not for now.

# - Then, get this running in a permanent process. I think that we want just a server; you should be able to call the get_ingredients method (passing a URL)
#   and then also be able to call the checkout method. In both cases it should return some JSON object``