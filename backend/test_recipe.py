import pytest

from recipe import (get_parsed_ingredient_from_ingredient_text,
                            gotten_size_text_to_count)
from ingredients import Ingredient

PARSE_TESTS = [
    ('1 ½ cups butter, softened', (1.5, 'cups', 'butter')),
    ('2 cups white sugar', (2.0, 'cups', 'white sugar')),
    ('4 eggs', (4.0, None, 'eggs')),
    ('1 teaspoon vanilla extract', (1.0, 'teaspoon', 'vanilla extract')),
    ('5 cups all-purpose flour', (5.0, 'cups', 'all-purpose flour')),
    ('2 teaspoons baking powder', (2.0, 'teaspoons', 'baking powder')),
    ('1 teaspoon salt', (1.0, 'teaspoon', 'salt')),
    ('cooking spray', (None, None, 'cooking spray')),
    ('1 loaf day-old Italian bread', (1.0, 'loaf', 'day-old Italian bread')),
    ('2 cups fresh strawberries, sliced', (2.0, 'cups', 'fresh strawberries')),
    ('8 large eggs', (8.0, 'large', 'eggs')),
    ('2 cups milk', (2.0, 'cups', 'milk')),
    ('½ cup heavy cream', (0.5, 'cup', 'heavy cream')),
    ('2 tablespoons white sugar', (2.0, 'tablespoons', 'white sugar')),
    ('½ teaspoon fresh lemon zest (Optional)', (0.5, 'teaspoon', 'fresh lemon zest')),
    ('¼ teaspoon almond extract', (0.25, 'teaspoon', 'almond extract')),
    ('⅛ teaspoon salt', (.125, 'teaspoon', 'salt')),
    ('1 ¼ cups self-rising flour, or more as needed', (1.25, 'cups', 'self-rising flour')),
    ('1 cup whole-milk Greek yogurt', (1.0, 'cup', 'whole-milk Greek yogurt')),
    ('1 serving nonstick cooking spray', (1.0, 'serving', 'nonstick cooking spray')),
    ('1 cup diced onion', (1.0, 'cup', 'onion')),
    ('1 cup diced bell pepper', (1.0, 'cup', 'bell pepper')),
    ('2 teaspoons salt, divided', (2.0, 'teaspoons', 'salt')),
    ('2 cups chicken broth', (2.0, 'cups', 'chicken broth')),
    ('1 (10 ounce) can diced tomatoes and green chiles (such as RO*TEL®)', (10.0, 'ounce', 'tomatoes and green chiles')),
    ('1 (10 ounce) can condensed cream of mushroom soup', (10.0, 'ounce', 'condensed cream of mushroom soup')),
    ('1 (4 ounce) can chopped green chiles (such as Ortega®)', (4.0, 'ounce', 'green chiles')),
    ('2 tablespoons oil', (2.0, 'tablespoons', 'oil')),
    ('1 tablespoon taco seasoning', (1.0, 'tablespoon', 'taco seasoning')),
    ('½ teaspoon ground cumin', (0.5, 'teaspoon', 'ground cumin')),
    ('¼ teaspoon ground black pepper', (0.25, 'teaspoon', 'ground black pepper')),
    ('1 pound skinless, boneless chicken breast', (1.0, 'pound', 'skinless, boneless chicken breast')),
    ('1 (8 ounce) package Neufchatel cheese, softened', (8.0, 'ounce', 'Neufchatel cheese')),
    ('½ cup unsalted butter', (0.5, 'cup', 'unsalted butter')),
    ('2 ½ cups all-purpose flour', (2.5, 'cups', 'all-purpose flour')),
    ('4 teaspoons baking powder', (4.0, 'teaspoons', 'baking powder')),
    ('4 teaspoons white sugar', (4.0, 'teaspoons', 'white sugar')),
    ('1 teaspoon salt', (1.0, 'teaspoon', 'salt')),
    ('1 ¾ cups buttermilk', (1.75, 'cups', 'buttermilk')),
    ('6 large eggs', (6.0, 'large', 'eggs')),
    ('⅓ cup mayonnaise', (1/3, 'cup', 'mayonnaise')),
    ('2 tablespoons sweet India pickle relish', (2.0, 'tablespoons', 'sweet India pickle relish')),
    ('2 teaspoons yellow mustard', (2.0, 'teaspoons', 'yellow mustard')),
    ('1 teaspoon white sugar', (1.0, 'teaspoon', 'white sugar')),
    ('1 teaspoon lemon juice', (1.0, 'teaspoon', 'lemon juice')),
    ('¼ teaspoon salt', (0.25, 'teaspoon', 'salt')),
    ('6 very ripe bananas, mashed', (6, None, 'bananas')),
    ('¼ teaspoon ground black pepper', (0.25, 'teaspoon', 'ground black pepper')),
    ('3 dashes hot sauce (such as Tabasco®) (Optional)', (3.0, 'dashes', 'hot sauce')),
    ('1 cup bread crumbs', (1.0, 'cup', 'bread crumbs')),
    ('1 (1 ounce) package dry French onion soup mix', (1.0, 'ounce', 'dry French onion soup mix')),
    ('⅓ cup mayonnaise', (0.3333333333333333, 'cup', 'mayonnaise')),
    ('1 tablespoon garlic paste (Optional)', (1.0, 'tablespoon', 'garlic paste')),
    ('4 skinless, boneless chicken breasts', (4.0, None, 'skinless, boneless chicken breasts')),
    ('1 large onion, chopped', (1.0, 'large', 'onion')),
    ('3 skinless, boneless chicken breast halves, or more to taste', (3.0, None, 'skinless, boneless chicken breast halves')),
    ('1 (14.5 ounce) can black beans, rinsed and drained', (14.5, 'ounce', 'black beans')),
    ('1 (14.5 ounce) can petite diced tomatoes', (14.5, 'ounce', 'petite tomatoes')),
    ('2 cups chicken broth', (2.0, 'cups', 'chicken broth')),
    ('1 cup sour orange juice', (1.0, 'cup', 'sour orange juice')),
    ('¾ cup dry white wine', (0.75, 'cup', 'dry white wine')),
    ('2 cloves garlic, pressed, or more to taste', (2.0, 'cloves', 'garlic')),
    ('1 tablespoon ground cumin', (1.0, 'tablespoon', 'ground cumin')),
    ('1 tablespoon dried oregano', (1.0, 'tablespoon', 'dried oregano')),
    ('2 teaspoons kosher salt', (2.0, 'teaspoons', 'kosher salt')),
    ('1 teaspoon ground black pepper', (1.0, 'teaspoon', 'ground black pepper')),
    ('½ teaspoon ground thyme', (0.5, 'teaspoon', 'ground thyme')),
    ('⅔ cup medium-grain white rice', (2/3, 'cup', 'medium-grain white rice')),
    ('3 slices bacon', (3.0, 'slices', 'bacon')),
    ('nonstick cooking spray', (None, None, 'nonstick cooking spray')),
    ('1 medium head cauliflower, cut into florets', (1.0, 'medium head', 'cauliflower')),
    ('¼ cup chicken broth', (0.25, 'cup', 'chicken broth')),
    ('½ teaspoon salt', (0.5, 'teaspoon', 'salt')),
    ('¼ teaspoon pepper', (0.25, 'teaspoon', 'pepper')),
    ('¼ teaspoon ground turmeric (Optional)', (0.25, 'teaspoon', 'ground turmeric')),
    ('1 (10.75 ounce) can cream of chicken soup (such as Campbell\'s®)', (10.75, 'ounce', 'cream of chicken soup')),
    ('½ cup shredded mozzarella cheese', (0.5, 'cup', 'mozzarella cheese')),
    ('½ cup shredded Cheddar cheese', (0.5, 'cup', 'Cheddar cheese')),
    ('1 scallion, green part only, thinly sliced', (1.0, None, 'scallion')),
    ('cooking spray', (None, None, 'cooking spray')),
    ('1 (16 ounce) package penne pasta', (16.0, 'ounce', 'penne pasta')),
    ('4 tablespoons salted butter', (4.0, 'tablespoons', 'salted butter')),
    ('1 large onion, chopped', (1.0, 'large', 'onion')),
    ('1 green bell pepper - stemmed, seeded, and finely chopped', (1.0, 'green', 'bell pepper')),
    ('1 (8 ounce) package sliced fresh mushrooms', (8.0, 'ounce', 'fresh mushrooms')),
    ('1 (8 ounce) jar sliced fresh mushrooms', (8.0, 'ounce', 'fresh mushrooms')),
    ('3 cloves garlic, minced', (3.0, 'cloves', 'garlic')),
    ('2 (8 ounce) packages processed cheese food (such as Velveeta®), cubed', (16.0, 'ounce', 'processed cheese food')),
    ('1 (14.5 ounce) can diced tomatoes, undrained', (14.5, 'ounce', 'tomatoes')),
    ('1 (10 ounce) can diced tomatoes and green chiles (such as RO*TEL®), undrained', (10.0, 'ounce', 'tomatoes and green chiles')),
    ('1 (4 ounce) can mild chopped green chile peppers', (4.0, 'ounce', 'mild green chile peppers')),
    ('4 cups cooked chicken, cut into bite-sized pieces', (4.0, 'cups', 'chicken')),
    ('8 each bone-in, skin-on chicken thighs', (8.0, None, 'bone-in, skin-on chicken thighs')),
    ('3 tablespoons unsalted butter, divided', (3.0, 'tablespoons', 'unsalted butter')),
    ('4 cloves garlic, minced', (4.0, 'cloves', 'garlic')),
    ('¼ cup packed brown sugar', (0.25, 'cup', 'brown sugar')),
    ('1 tablespoon honey', (1.0, 'tablespoon', 'honey')),
    ('1 banana, broken into chunks', (1.0, None, 'banana')),
    ('1 orange, peeled and segmented', (1.0, None, 'orange')),
    ('1 lemon, juiced', (1.0, None, 'lemon')),
    ('½ teaspoon dried oregano', (0.5, 'teaspoon', 'dried oregano')),
    ('¼ teaspoon dried thyme', (0.25, 'teaspoon', 'dried thyme')),
    ('¼ teaspoon dried basil', (0.25, 'teaspoon', 'dried basil')),
    ('2 tablespoons butter, melted, or more to taste', (2, 'tablespoons', 'butter')),
    ('3 cups basmati rice', (3.0, 'cups', 'basmati rice')),
    ('2 teaspoons kosher salt, or to taste', (2.0, 'teaspoons', 'kosher salt')),
    ('1 teaspoon freshly ground black pepper', (1.0, 'teaspoon', 'freshly ground black pepper')),
    ('2 teaspoons ground cumin', (2.0, 'teaspoons', 'ground cumin')),
    ('1 tablespoon chili powder', (1.0, 'tablespoon', 'chili powder')),
    ('¼ teaspoon cayenne pepper (Optional)', (0.25, 'teaspoon', 'cayenne pepper')),
    ('¼ teaspoon dried oregano', (0.25, 'teaspoon', 'dried oregano')),
    ('¼ cup olive oil', (0.25, 'cup', 'olive oil')),
    ('1 (16 ounce) jar tomato salsa', (16.0, 'ounce', 'tomato salsa')),
    ('2 cups chicken broth', (2.0, 'cups', 'chicken broth')),
    ('2 (15 ounce) cans kidney beans, rinsed and drained', (30.0, 'ounce', 'kidney beans')),
    ('cooking spray', (None, None, 'cooking spray')),
    ('1 loaf day-old Italian bread', (1.0, 'loaf', 'day-old Italian bread')),
    ('2 cups fresh strawberries, sliced', (2.0, 'cups', 'fresh strawberries')),
    ('8 large eggs', (8.0, 'large', 'eggs')),
    ('2 cups milk', (2.0, 'cups', 'milk')),
    ('½ cup heavy cream', (0.5, 'cup', 'heavy cream')),
    ('2 tablespoons white sugar', (2.0, 'tablespoons', 'white sugar')),
    ('½ teaspoon fresh lemon zest (Optional)', (0.5, 'teaspoon', 'fresh lemon zest')),
    ('¼ teaspoon almond extract', (0.25, 'teaspoon', 'almond extract')),
    ('⅛ teaspoon salt', (0.125, 'teaspoon', 'salt')),
    ('1 large onion, chopped', (1, 'large', 'onion')),
    ('3 large russet potatoes, peeled and cut in half lengthwise  ', (3, 'large', 'russet potatoes')),
]

@pytest.mark.parametrize("ingredient_text, parsed", PARSE_TESTS)
def test_ingredient_parser(ingredient_text, parsed):
    print(get_parsed_ingredient_from_ingredient_text(ingredient_text), Ingredient(*parsed), get_parsed_ingredient_from_ingredient_text(ingredient_text) == Ingredient(parsed[0], parsed[1], parsed[2]))
    assert get_parsed_ingredient_from_ingredient_text(ingredient_text) == [Ingredient(*parsed)]

def test_no_ingredients():
    assert get_parsed_ingredient_from_ingredient_text('1 cup water') == []

def test_two_ingredients():
    assert get_parsed_ingredient_from_ingredient_text('salt and ground black pepper to taste') == [Ingredient(1, 'pinch', 'salt'), Ingredient(1, 'pinch', 'pepper')]

SIZE_TESTS = [
    ('12 ct', 6.0, 'large', None, 1),
    ('12 ct', 13.0, 'large', None, 2),
    ('30 oz', 0.3333333333333333, 'cup', None, 1),
    ('30 oz', 10, 'cups', None, 3),
    ('16 fl oz', 2.0, 'tablespoons', None, 1),
    ('16 fl oz', 33, 'tablespoons', None, 2),
    ('14 oz', 2.0, 'teaspoons', None, 1),
    ('24 oz', 1.0, 'teaspoon', None, 1),
    ('24 oz', 1000.0, 'teaspoon', None, 7),
    ('52 fl oz', 1.0, 'teaspoon', None, 1),
    ('17.6 oz', 0.25, 'teaspoon', None, 1),
    ('3 oz', 0.25, 'teaspoon', None, 1),
    ('5 oz', 3.0, 'dashes', None, 1),
    ('1 lb', 3.0, 'large', 'russet potatoes', 2),
    ('3 lb bag', 1.0, 'large', 'onion', 1),
    ('6.5 oz', 2.0, 'stalks', 'celery', 1),
    ('6.5 oz', 2.0, 'celery', 'stalks', 1),
    # NEW: FIX THESE UP WITH PROPER INGREDIENTS
    ('4 each', 0.25, 'cup', 'butter', 1),
    ('5 lb', 2.5, 'tablespoons', 'all-purpose flour', 1),
    ('4 each', 2.0, 'tablespoons', 'butter', 1),
    ('4 each', 0.3333333333333333, 'cup', 'butter', 1),
    ('1 each', 1.0, 'teaspoon', 'salt', 1),
    ('24 oz', 3.0, 'pounds', 'Yukon Gold potatoes', 2),
    ('5 lb', 3.0, 'pounds', 'Yukon Gold potatoes', 1),
    ('24 oz bag', 3.0, 'pounds', 'Yukon Gold potatoes', 2),
    ('1.5 lb', 3.0, 'pounds', 'Yukon Gold potatoes', 2),
    ('1 lb bag', 3.0, 'pounds', 'Yukon Gold potatoes', 3),
    ('1 lb', 8.0, 'ounces', 'unelbow macaroni', 1),
    ('16.8 lb', 1.0, 'pound', 'ground beef', 1),
    ('per lb', 1.0, 'pound', 'ground beef', 1),
    ('16 oz', 1.0, 'pound', 'ground beef', 1),
    ('16 oz', 1.0, 'pound', 'lean ground beef', 1),
    ('16.8 lb', 1.0, 'pound', 'lean ground beef', 1),
    ('5 oz', None, None, 'cooking spray', 1),
    ('1 each', 1.5, 'teaspoons', 'salt', 1),
    ('88 ct', 5.0, 'pounds', 'Granny Smith apples', 1),
    ('1 lb', 5.0, 'pounds', 'Granny Smith apples', 5),
    ('1 ct', 5.0, 'pounds', 'Granny Smith apples', 15),
    ('per lb', 5.0, 'pounds', 'Granny Smith apples', 5),
    ('2 lb bag', 5.0, 'pounds', 'Granny Smith apples', 3),
    ('12 oz container', 5.0, 'pounds', 'Granny Smith apples', 7),
    ('0.5 gal', 2.0, 'cups', 'milk', 1),
    ('8 oz', 1.0, 'pound', 'mushrooms', 2),
    ('8 oz container', 1.0, 'pound', 'mushrooms', 2),
    ('3 ct', 0.75, 'cup', 'ham', 1),
    ('1 ct', 0.3333333333333333, 'cup', 'celery', 1),
    ('2 count bag', 0.3333333333333333, 'cup', 'celery', 1),
    ('4 each', 1.0, 'ounce', 'dry ranch salad dressing mix', 1),
    ('4 each', 1.0, 'teaspoon', 'dry ranch salad dressing mix', 1),
    ('per lb', 8.0, 'chicken', 'thighs', 3),
    ('48 oz', 6.0, 'small', 'red potatoes', 1),
    ('5 lb bag', 6.0, 'small', 'red potatoes', 1),
    ('1 ct', 6.0, 'small', 'red potatoes', 6),
    ('1 ct', 1, 'pinch', 'pepper', 1),
    ('1 lb', 8.0, 'chicken', 'thighs', 3),
    ('1 bunch', 1.5, 'teaspoons', 'fresh oregano', 1),
    ('$3.99', 1.0, 'cup', 'cauliflower', 1),
    ('1 ct', 1.0, 'cup', 'cauliflower', 1),
    ('$0.94\neach (est.)\n$0.80 with Express\n$0.99 / lb\nFinal cost by weight', 3.5, 'cups', 'potatoes', 5),
    ('per lb', 0.75, 'cup', 'ham', 1),
    ('1 ct', 3.0, 'cloves', 'garlic', 1),
    ('$0.50', 3.0, 'cloves', 'garlic', 1),
]

@pytest.mark.parametrize("size_text, count, unit, ingredient, final_count", SIZE_TESTS)
def test_size_computations(size_text, count, unit, ingredient, final_count):
    assert gotten_size_text_to_count(size_text, count, unit, ingredient) == final_count


def main():
    import json
    with open('tests.json', 'r+') as f:
        data = json.loads(f.read())

    for d in data:
        print(str((d['gotten_size_text'], d['count'], d['unit'], d['ingredient'])) + ",")

main()
