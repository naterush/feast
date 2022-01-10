import json
import time
from abc import ABC, abstractmethod
from typing import List, Optional

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

from ingredients import Ingredient, IngredientLink, IngredientPair
from recipe import get_recipe_from_all_recipe_link, gotten_size_text_to_count


class Cart(ABC):

    @abstractmethod
    def __init__(self, email, password_pat, headless=False):
        raise NotImplementedError()

    @abstractmethod
    def login(self):
        raise NotImplementedError()

    @abstractmethod
    def add_recipe(self, url):
        raise NotImplementedError()

    @abstractmethod
    def clear(self):
        raise NotImplementedError()

    @abstractmethod
    def add_ingredient(self):
        raise NotImplementedError()

    @abstractmethod
    def checkout(self):
        raise NotImplementedError()
    
    


class AmazonCart(Cart):

    def __init__(self, email, password_path, headless=False):
        chrome_options = Options()
        chrome_options.headless = headless
        self.driver = webdriver.Chrome(options=chrome_options)
        self.email = email
        self.password = open(password_path, 'r').read().strip()

        self.driver.get("https://www.amazon.com")

    def login(self):
    
        signin_dropdown = self.driver.find_element_by_id('nav-link-accountList')
        signin_dropdown.click()

        email_input = self.driver.find_element_by_id('ap_email')
        email_input.send_keys(self.email)
        continue_button = self.driver.find_element_by_id('continue')
        continue_button.click()
        password_input = self.driver.find_element_by_id('ap_password')
        password_input.send_keys(self.password)
        sign_in = self.driver.find_element_by_id('signInSubmit')
        sign_in.click()

    def add_item_to_cart(self, item):
    
        search_box = self.driver.find_element_by_id('twotabsearchtextbox')
        search_box.clear()
        search_box.send_keys(item)
        search_box.send_keys(Keys.RETURN)

        first_element = self.driver.find_element_by_class_name('s-image')
        first_element.click()

        print("Added item", item)

        # TODO: actually add it to the cart

    def checkout(self):
        print("Checking out cart, return status")

        self.driver.close()
        pass


class InstaCart(Cart):

    def __init__(self, email, password_path, headless=False):
        chrome_options = Options()
        chrome_options.headless = headless
        chrome_options.add_argument("--user-data-dir=/Users/nathanrush/feast-monorepo/UserData")

        self.driver = webdriver.Chrome(options=chrome_options)
        self.email = email
        self.password = open(password_path, 'r').read().strip()

        self.driver.get("https://www.instacart.com")

        self.url = ''
        self.title = ''
        self.servings = 0
        self.ingredient_pairs = []


    def login(self):
        if False:
            # We only login first time
            signin_button = self.driver.find_elements_by_xpath("//*[contains(text(), 'Log in')]")[0]
            signin_button.click()

            time.sleep(2)

            email = self.driver.find_element_by_name('email')
            email.send_keys(self.email)

            password = self.driver.find_element_by_name('password')
            password.send_keys(self.password)

            login_button = self.driver.find_elements_by_xpath("//*[contains(text(), 'Log in')]")[1]
            login_button.click()

        store = self.driver.find_element_by_xpath('//a[contains(@href,"/storefront")]')
        store.click()

        time.sleep(5)

    def add_recipe(self, url: str) -> Optional[List[IngredientPair]]:

        recipe = get_recipe_from_all_recipe_link(url)        

        try:
            for ingredient in recipe['ingredients']:
                if not self.add_ingredient(ingredient):
                    print("Unable to add ingredient", ingredient)
                    # TODO: clear cart
                    self.ingredient_pairs = []

                    return None
        except Exception as e:
            print(e)
            pass

        self.url = url
        self.title = recipe['title']
        self.servings = recipe['servings']

        print("RETURNING!")

        return self.ingredient_pairs


    def _add_ingredient_on_page(self, link: str, ingredient: Ingredient) -> Ingredient: 
        """
        Given a link to a specific item (one of the search results for an item), this
        checks if it is the appropriate size, and adds it if so. 
        """

        self.driver.get(link)
        time.sleep(3)

        # First, check if we can add to cart. If we cannot, then this doesn't work, and return
        add_to_cart_buttons = self.driver.find_elements_by_xpath("//span[contains(text(), 'Add to cart')]")
        if len(add_to_cart_buttons) == 0:
            return False

        # Then, check that the ingredient is actually something we want. The search is not exact
        ingredient_title = self.driver.find_element_by_xpath('//*[@id="react-views-container"]/div/div[1]/div/div/div[1]/div[2]/div[1]/h2/span').text
        
        # Then, check if the sizing works
        size_texts = self.driver.find_elements_by_xpath('//*[@id="react-views-container"]/div/div[1]/div/div/div[1]/div[2]/div[1]/div[1]')
        if len(size_texts) == 0:
            return False

        count_needed = gotten_size_text_to_count(size_texts[0].text, ingredient.count, ingredient.unit, ingredient=ingredient.ingredient)
        print("Ordering", count_needed, "of", ingredient_title, "for", ingredient.ingredient)


        # Click on the selected text
        if count_needed != 1:
            self.driver.find_element_by_id('selected-text').click()

            # Click on the correct option
            options = self.driver.find_elements_by_xpath('//li[@role="option"]')
            clicked = False
            values = []
            for option in options:
                value = option.get_attribute('value')
                values.append(value)
                if value.startswith(str(count_needed)):
                    option.click()
                    clicked = True
                    break
            if not clicked:
                raise Exception('Not found', count_needed, "in", values, link)
            
        # Finially, add to cart
        add_to_cart_buttons[0].click()

        # TODO: handle if there are replicated ingredients in the recipe. This needs to be handled above

        # And then click on the quantity we want

        # TODO: actually add the specific number of items
        time.sleep(1)

        return Ingredient(
            count_needed, 
            size_texts[0].text, # TODO: this is a bit weird, it's a unit and count in one
            ingredient_title
        )

    def _get_current_ingredient_links(self) -> List[IngredientLink]:
        # We get the container for each of the search results, and pull out their title, 
        # if they are sponsored or not (as these are usually irrelevant), and the links
        # NOTE: we just search for all li elements, and then in parsing just bail if
        # they don't follow the correct format
        search_results = self.driver.find_elements_by_xpath('//ul/li')

        ingredient_links: List[IngredientLink] = []
        for search_result in search_results:
            try:
                # Easy to find if it's sponsored
                is_sponsored = len(search_result.find_elements_by_xpath(".//span[contains(text(), 'Sponsored')]")) > 0
                store_choice = len(search_result.find_elements_by_xpath(".//span[contains(text(), 'Store choice')]")) > 0

                # Also, easy to find the link    
                link = search_result.find_element_by_xpath('.//div/div/div/div/div/a').get_attribute('href')

                # We have to handle the differing paths if there is a top element
                text_xpath = './/div/div/div/div/div/a/div[2]/div[2]' if is_sponsored or store_choice else './/div/div/div/div/div/a/div[1]/div[2]'
                # The title changes places depending on promotions, but we always want to get the second to last div
                ingredient_xpath = text_xpath + '/div[position() = (last() - 1)]'
                search_ingredient = search_result.find_element_by_xpath(ingredient_xpath).text

                ingredient_links.append(
                    IngredientLink(search_ingredient, link, is_sponsored, store_choice)
                )
            except:
                pass
        
        return ingredient_links


    def add_ingredient(self, ingredient: Ingredient) -> bool:
        
        search = self.driver.find_element_by_xpath("//input[@aria-label='search']")
        # TODO: we have to handle count and measurment 
        search.send_keys(ingredient.ingredient)
        search.send_keys(Keys.RETURN)

        # Need a long enough delay the page can load
        time.sleep(8)

        ingredient_links = self._get_current_ingredient_links()

        if len(ingredient_links) == 0:
            print("Found no ingredient links, waiting another 10 seconds")
            time.sleep(10)
            ingredient_links = self._get_current_ingredient_links()
            if len(ingredient_links) == 0:
                print("Still 0, waiting for Nate to come back")
                time.sleep(1000)
        
        for ingredient_link in ingredient_links:
            try:
                # We don't try adding sponsored ingredients
                if ingredient_link.is_sponsored:
                    continue

                added_ingredient = self._add_ingredient_on_page(ingredient_link.link, ingredient)

                if not added_ingredient:
                    continue

                self.ingredient_pairs.append(
                    IngredientPair(
                        ingredient,
                        added_ingredient,
                        ingredient_links
                        # TODO: add the other links, and link index here!
                    )
                )

                return True
            except Exception as e:
                import traceback
                print(traceback.format_exc())
                pass

        # TODO: here, I should just add an ingredient (if there is more than one)
        # and 

        return False

        
    def clear(self):

        # TODO: we might have to close some notifications here

        time.sleep(2)

        # Open the cart
        self.driver.find_element_by_xpath('//*[@id="commonHeader"]/div[2]/div[4]/button').click()

        # Loading the cart takes a while sometimes
        time.sleep(6)

        remove_buttons = self.driver.find_elements_by_xpath("//button[@aria-label='Remove']")
        for button in remove_buttons:
            button.click()
            time.sleep(1)

        print(f"Cleared {len(remove_buttons)} items from the cart")

    def to_JSON(self):
        return json.dumps({
            'title': self.title,
            'url': self.url,
            'servings': self.servings,
            'ingredients': [
                ingredient_pair.to_serializable()
                for ingredient_pair in self.ingredient_pairs
            ]
        })

    def checkout(self):
        print(self.ingredient_pairs)
        exit(0)

        # Open checkout
        self.driver.get('https://www.instacart.com/store/checkout_v3')

        time.sleep(8)

        # If a popup appears, close it
        try:
            continue_button = self.driver.find_element_by_xpath('//*[@id="modal-content-container"]/div/div[2]/div[3]/div/div/div/button')
            continue_button.click()
        except Exception as e:
            print(e)
            pass

        # Click continue on the delivery time
        self.driver.find_element_by_xpath('//*[@id="react-views-container"]/div/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/button[1]/span').click()
        self.driver.find_element_by_xpath('//*[@id="react-views-container"]/div/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[2]/form/div[2]/button').click()
        self.driver.find_element_by_xpath('//*[@id="Mobile number chooser"]/form/div[3]/button').click()
        self.driver.find_element_by_xpath('//*[@id="react-views-container"]/div/div[1]/div/div/div/div/div[1]/div[6]/div/div/div/div[2]/div/button[1]').click()
        self.driver.find_element_by_xpath('//*[@id="react-views-container"]/div/div[1]/div/div/div/div/div[1]/div[9]/div/div/div[2]/button').click()

        # TODO: we just have to click checkout, and then we're done, I think

        
        print("Checking out cart, return status")

        self.driver.close()
        pass
