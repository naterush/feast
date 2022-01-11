"""
Here is the flow of the pipeline:

1. Give a URL of a website.
2. Get a list of the `ingredient_text`, which is the text displayed on the website
3. Get a list of the `ingredient_parsed`, which is a structure of (count, measurment, ingredient).

Then, returns the ingredients parsed. In the future, we might another step to clean them
up (so that we know better what to search for), but we don't worry about this for now!
"""

from math import ceil
import os
from typing import Dict, List
import json

import requests
from bs4 import BeautifulSoup

from ingredients import Ingredient

unit_WORDS = [
    'teaspoon',
    'tablespoon',
    'cup',

    'pound',

    'large',
    'loaf',
    'can'
]

INSTRUCTIONS = [
    'softened',
    'diced',
    'sliced',
    'chopped',
    'mashed',
    'melted',
    'packed',
    'divided',
    'minced',
    'cooked',
    'undrained',
    'juiced',
    'shredded',
    'zested',
    'quartered',
    'thinly sliced',
    'or more as needed',
    'or as desired',
    'very ripe',
    'broken into chunks',
    'peeled and segmented',
    'rinsed and drained',
    'or to taste',
    'or as needed to cover',
    'to taste',
    'or more',
    'peeled and cut in half lengthwise',
    'cut into bite-sized pieces',
    'cut into 1-inch slices',
    'cut into large florets',
    'green part only, thinly sliced',
    'cored and cut into 1-inch pieces',
    'plus more for kneading',
    ', pressed, or more to taste',
    ' - stemmed, seeded, and finely chopped',
    ', cut into florets',
]
INSTRUCTIONS.sort(key=lambda x: len(x), reverse=True)

def starts_with_count(ingredient_text):
    try:
        float(ingredient_text.split(' ')[0])
        return True
    except:
        return False


def get_parsed_ingredient_from_ingredient_text(ingredient_text) -> List[Ingredient]:
    CLEANUP = {
        '\u2009': '',
        '¾': '.75',
        '⅔': '.6666666666666666666666666666',
        '½': '.5',
        '⅓': '.3333333333333333333333333333',
        '¼': '.25',
        '⅛': '.125',
        '(Optional)': ''
    }

    # Cleanup how they handle decimals
    for old, new in CLEANUP.items():
        ingredient_text = ingredient_text.replace(old, new)    

    # Remove unnecessary instructions
    for instruction in INSTRUCTIONS:
        ingredient_text = ingredient_text.removesuffix(f', {instruction}')
        ingredient_text = ingredient_text.replace(f'{instruction} ', '')   
        ingredient_text = ingredient_text.replace(f'{instruction}', '') 

    ingredient_split = ingredient_text.split(' ')


    # If there is an count, it is the first item. It must be a number to be an count, so we try and parse it
    # this handles the sizing appropriately
    possible_count = ingredient_split[0]
    try:
        count = float(possible_count)
    except:
        count = None

    if count is None:
        # If the count is None, then the entire thing is the ingredient
        unit = None
        ingredient = ingredient_text
    else:
        if len(ingredient_split) == 2:
            unit = None
            ingredient = ingredient_split[1]
        else:
            if 'ounce)' in ingredient_text:
                # If we have some sort of ounce measurment, then we have to take special care
                # to parse the onces correctly and put them in the measurment
                unit = ' '.join(ingredient_split[1:4])
                ingredient = ' '.join(ingredient_split[4:])
            else:
                unit = ingredient_split[1]
                ingredient = ' '.join(ingredient_split[2:])


    # Remove specific brand suggestions
    if ' (such as' in ingredient:
        ingredient = ingredient[:ingredient.find(' (such as')]

    # Handle some special cases:
    if ingredient == 'head cauliflower':
        unit = unit + ' head'
        ingredient = 'cauliflower'
    if unit == 'each':
        unit = None
    if unit == 'skinless,':
        unit = None
        ingredient = 'skinless, ' + ingredient
    if unit is not None and ((unit.endswith('can') or unit.endswith('cans')) or (unit.endswith('jar') or unit.endswith('jars')) or (unit.endswith('package') or unit.endswith('packages'))):
        # Handle the cans, jars, and packages case
        new_unit = unit.removeprefix('(').split(')')[0]
        new_count, new_unit = new_unit.split(' ')
        count = count * float(new_count)
        unit = new_unit
    if 'salt' in ingredient_text and 'pepper' in ingredient_text:
        # Handle when salt and pepper are together
        return [
            Ingredient(1, 'pinch', 'salt'),
            Ingredient(1, 'pinch', 'pepper'),
        ]

    ingredient = ingredient.strip().removesuffix(',').removesuffix(', ')

    if ingredient == 'ice cubes' or ingredient == 'water':
        # If it's an ice cube, don't do it
        return []

 
    return [Ingredient(count, unit, ingredient)]


def get_raw_ingredients_from_all_recipe(url: str) -> Dict[str, str]:
    """
    Like: https://www.allrecipes.com/recipe/280034/southern-style-egg-salad/
    """
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib

    ingredient_spans = soup.find_all('span', attrs={'class': 'ingredients-item-name'})
    ingredient_texts = [span.text.strip() for span in ingredient_spans]

    ingredients = []
    for text in ingredient_texts:
        ingredients.extend(get_parsed_ingredient_from_ingredient_text(text))

    return ingredients

def get_recipe_from_all_recipe_link(url: str) -> Dict[str, str]:
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib

    title_spans = soup.find_all('h1', attrs={'class': 'headline'})

    title = title_spans[0].text.strip()

    serving_divs = soup.find_all('div', attrs={'class': 'recipe-adjust-servings__size-quantity'})
    servings = int(serving_divs[0].text.strip())
    print("Servings", servings)

    ingredients = get_raw_ingredients_from_all_recipe(url)

    return {
        'title': title,
        'url': url,
        'servings': servings,
        'ingredients': ingredients
    }





def get_raw_ingredients_from_recipe(url: str) -> Dict[str, str]:
    if 'allrecipes' in url:
        return get_raw_ingredients_from_all_recipe(url)
    else:
        raise ValueError('All recipes is the only supported website currently')

    
def size_text_to_unit(size_text: str) -> str:
    _, gotten_unit = size_text.split(' ', 1)
    return gotten_unit

def gotten_size_text_to_count(gotten_size_text, count, unit, ingredient=None) -> int:
    try:
        return _gotten_size_text_to_count(gotten_size_text, count, unit, ingredient=ingredient)
    except Exception as e:
        if not os.path.exists('tests.json'):
            with open('tests.json', 'w+') as f:
                f.write('[]')

        # Write to a file
        with open('tests.json', 'r+') as f:
            data = json.loads(f.read())

        data.append({
            'gotten_size_text': gotten_size_text,
            'count': count,
            'unit': unit,
            'ingredient': ingredient
        })

        with open('tests.json', 'w+') as f:
            f.write(
                json.dumps(data)
            )

        raise e

def _gotten_size_text_to_count(gotten_size_text, count, unit, ingredient=None) -> int:
    """
    Returns the total amoutn we need to get count of measurment. Currently
    only handles size measurments from allrecipies.
    """
    ingredient = ingredient.lower() if ingredient else None
    gotten_count, gotten_unit = gotten_size_text.split(' ', 1)

    # First, we check if this is a per lb approach, in which case we handle this specially
    if gotten_size_text == 'per lb':
        if unit == None:
            return ceil(count)
        elif unit == 'pound' or unit == 'pounds':
            return ceil(count)
        elif unit == 'chicken' and ingredient == 'thighs':
            # 2 2/3 chicken thighs in a pound
            return ceil(count / (2 + 2/3))
        else:
            raise Exception("No handler for unit", gotten_size_text, count, unit, ingredient)
    

    gotten_count = float(gotten_count)

    # Then, we check specific ingredients that have tricky measurments
    if ingredient == 'butter':
        if unit == 'tablespoon' or unit == 'tablespoons':
            return 1 # Not sold smaller than a table spoon

        if gotten_unit == 'each':
            # 4 each, means 4 sticks that are .5 cups each
            if unit == 'cup' or unit == 'cups':
                return ceil(count * 2 / gotten_count)
            
    if ingredient == 'all-purpose flour':
        if unit == 'tablespoons':
            return 1 # Not sold smaller than a table spoon

    if ingredient == 'salt':
        if unit == 'teaspoon' or unit == 'teaspoons':
            return 1 # Not sold smaller than a table spoon
        
    if ingredient == 'unelbow macaroni':
        if gotten_unit == 'lb':
            if unit == 'ounce' or unit == 'ounces':
                return ceil(count / 16 / gotten_count)
        
    if ingredient == 'cooking spray':
        return 1

    if ingredient == 'granny smith apples':
        if gotten_unit == 'ct':
            if unit == 'pound' or unit == 'pounds':
                return ceil(count * 3 / gotten_count)
    
    if ingredient == 'ham':
        if gotten_unit == 'ct':
            if unit == 'cup' or unit == 'cups':
                # TODO: this is wrong, but ok...
                return 1

    if ingredient == 'celery':
        if gotten_unit == 'ct' or gotten_unit == 'count bag':
            if unit == 'cup':
                # 2 celery stalks in a cup
                return ceil(count * 2 / gotten_count)
    
    if ingredient == 'dry ranch salad dressing mix':
        # Assume we only need one packet of this
        return 1

    if ingredient == 'red potatoes' and unit == 'small':
        if gotten_unit == 'lb bag' or gotten_unit == 'lb':
            # 1 pound is 7 small red potatoes
            return ceil(count / 7 / gotten_count)
        if gotten_unit == 'oz':
            return ceil(count * 6 / gotten_count)

    if unit == 'chicken' and ingredient == 'thighs':
        if gotten_unit == 'lb' or gotten_unit == 'lbs':
            # 2 2/3 chicken thighs in a pound
            return ceil(count / (2 + 2/3) / gotten_count)

    if ingredient == 'fresh oregano':
        if gotten_unit == 'bunch':
            # We don't need more than a single bunch of herbs, methinks
            return 1


    if gotten_unit == 'oz' or gotten_unit == 'fl oz' or gotten_unit == 'oz container':
        if unit == 'clove' or unit == 'cloves':
            # A garlic glove is .18 ounces, according to: https://thewholeportion.com/how-many-ounces-of-garlic-in-a-clove/
            return ceil((count * .18) / gotten_count)
        elif (unit == 'head' or unit == 'heads') and ingredient == 'cauliflower':
            # A cauliflower is between 10 and 30 ounces
            return ceil((count * 15) / gotten_count)
        elif unit == 'celery' or ingredient == 'celery':
            # 2 ounces in celery stalk
            return ceil((count * 2) / gotten_count) 
    elif gotten_unit == 'lb' or gotten_unit == 'lb bunch' or gotten_unit == 'lb bag' or gotten_unit == 'per lb':
        if unit is None:
            if ingredient == 'bananas':
                # 4 bananas are 1 pound
                return ceil(gotten_count / 4 / gotten_count)
            elif ingredient == 'lemon' or ingredient == 'lemons':
                # 4 lemons in a pound
                return ceil(gotten_count / 4 / gotten_count)
        elif unit == 'large':
            if ingredient == 'onion':
                #  There are three large onions in a pound
                return ceil(count / 3 / gotten_count)
            if ingredient == 'russet potatoes':
                #  There are 2 large onions in a pound
                return ceil(count / 2 / gotten_count)
        elif unit == 'pound' or unit == 'pounds':
            return ceil(count / gotten_count)


    # Or, we're just dealing with a number, in which case we handle that here
    if gotten_unit == 'oz' or gotten_unit == 'fl oz' or gotten_unit == 'oz container' or gotten_unit == 'oz bag':
        if unit == 'ounce' or unit == 'ounces':
            return ceil(count / gotten_count)
        elif unit == 'pound' or unit == 'pounds':
            return ceil(count * 16 / gotten_count)
        elif unit == 'cups' or unit == 'cup':
            return ceil((count * 8) / gotten_count)
        elif unit == 'tablespoons' or unit == 'tablespoon':
            return ceil((count * .5) / gotten_count)
        elif unit == 'teaspoons' or unit == 'teaspoon':
            return ceil((count * 0.166667) / gotten_count)
        elif unit == 'dash' or unit == 'dashes' or unit == 'pinch' or unit == 'pinches':
            # If you need dashes of something, assume you just need one bottle of it
            return 1
        elif unit == 'pound' or unit == 'pounds':
            return ceil(count * 16 / gotten_count)
    elif gotten_unit == 'ct':
        if unit == 'large':
            return ceil(count / gotten_count)
        elif unit == 'small':
            return ceil(count / gotten_count)
        elif unit == 'head' or unit == 'heads':
            return ceil(count / gotten_count)
        elif unit is None:
            return ceil(count / gotten_count)
        elif unit == 'pinch':
            return 1
        
    elif gotten_unit == 'lb' or gotten_unit == 'lb bunch' or gotten_unit == 'lb bag':
        if unit == 'cup' or unit == 'cups':
            return ceil((count * .44) / gotten_count)

    elif gotten_unit == 'g':
        if unit == 'cup' or unit == 'cups':
            return ceil((count * 136) / gotten_count)
    elif gotten_unit == 'gal':
        if unit == 'cup' or unit == 'cups':
            return ceil(count / 16 / gotten_count)
    
    raise Exception("No handler for unit", gotten_size_text, count, unit, ingredient)


def is_same_ingredient(ingredient_one: str, ingredient_two: str) -> bool:
    """
    Returns true if the two ingredients are the same.

    For now, we hard code most common ingredients; in the future,
    we'd like to some language embedding to generalize this.
    """
    
    

    return True