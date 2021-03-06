import type { NextPage } from 'next'
import Head from 'next/head'
import Link from 'next/link'
import { useEffect, useState } from 'react'
import IconButton from '../components/IconButton'
import Ingredient from '../components/Ingredient'
import styles from '../styles/Recipe.module.css'

export interface Recipe {
  title: string;
  url: string;
  servings: number;
  ingredients: IngredientPair[];
  total_num_ingredients: number;
  outstanding_operations: boolean;
}
export interface IngredientPair {
  recipe_ingredient: Ingredient;
  cart_ingredient: Ingredient;
  other_ingredient_links?: IngredientLink[];
  toggle: boolean;
}
export interface Ingredient {
  count: number;
  unit: string;
  ingredient: string;
}

export interface IngredientLink {
  ingredient: string;
  link: string;
  is_sponsored: boolean;
  is_store_choice: boolean;
}

const Home: NextPage = () => {
  
  const [recipe, setRecipe] = useState<Recipe | undefined>(undefined);
  const [toggles, setToggles] = useState<boolean[]>([]);

  const loadData = async () => {

    //const text1 = `{"title": "Butterhorn Dinner Rolls", "url": "https://www.allrecipes.com/recipe/8296140/butterhorn-dinner-rolls/", "servings": 12, "ingredients": [{"recipe_ingredient": {"count": 1.5, "unit": "teaspoons", "ingredient": "kosher salt"}, "cart_ingredient": {"count": 1.5, "unit": "teaspoons", "ingredient": "kosher salt"}, "other_ingredient_links": [], "toggle": false}], "total_num_ingredients": 8, "outstanding_operations": true}`

    const response = await fetch('/getcurrentrecipe', {
        method: 'GET',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
    });
    if (response.status != 200) {
      return;
    }

    const text = await response.text();
    setRecipe(JSON.parse(text))
  }

  useEffect(() => {
    loadData()
    // We load the data every 200ms, so we can watch the recipe grow
    const interval = setInterval(() => {
      loadData()
    }, 200);

    return () => clearInterval(interval);
  }, [])

  // Make sure the toggles are the right length
  useEffect(() => {
    setToggles((prevToggles) => {
      const newToggles = [...prevToggles];
      if (newToggles.length < (recipe?.ingredients.length || 0)) {
        const originalLength = newToggles.length;
        for (let i = 0; i < ((recipe?.ingredients.length || 0) - newToggles.length); i++) {
          const newToggleValue = recipe?.ingredients[i + originalLength].toggle;
          newToggles.push(newToggleValue !== undefined ? newToggleValue : true);
        }
      }
      return newToggles;
    })
  }, [recipe])

  const numIngredientsNotYetInCart = (recipe?.total_num_ingredients || 0) - (recipe?.ingredients.length || 0);

  return (
    <>
      <Head>
        <title>Feast</title>
        <meta name="Feast" content="Feast on food" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <div className={'centered-container'}>
        
        <main className={styles.main}>
          <div className='w-100 flex flex-row justify-content-space-between align-items-center'>
            <h1>
              {recipe?.title}
            </h1>
            <a className='blue-button' href={recipe?.url} target='_blank' rel="noreferrer">
              {recipe?.url}
            </a>
          </div>
          <div className='w-100 text-left'>
            <p>
              Select how many servings you want, and delete the ingredients you already have in your fridge.
            </p>
          </div>
          <div className='w-100 flex flex-row justify-content-space-between align-items-center'>
            <h2>
              Selected Ingredients
            </h2>
            <div className={'flex flex-row blue-button'}>
              <div className='mr-5px ml-5px'>-</div>
              <div>{recipe?.servings} Servings</div>
              <div className='mr-5px ml-5px'>+</div>
            </div>
          </div>
          <div className='w-100 flex flex-column justify-content-space-between'>
            {recipe?.ingredients.map((ingredientPair, i) => {
              return (
                <Ingredient key={i} ingredientPair={ingredientPair} toggles={toggles} setToggles={setToggles} index={i}/>
              )
            })}
            {numIngredientsNotYetInCart > 0 && 
              <div>
                Loading {numIngredientsNotYetInCart} more ingredients. About {Math.round(numIngredientsNotYetInCart * .15)} minutes left.
              </div>
            }
          </div>
          <div className='w-100 flex flex-row justify-content-space-between mt-30px'>
            <div>
              <button className='blue-button'>
                <h3 className='mr-10px ml-10px'>
                  <Link href='/'>
                    Back
                  </Link>
                </h3>
              </button>
              <button 
                className='blue-button' 
                onClick={async () => {
                  const response = await fetch('/clear', {
                    method: 'POST',
                    headers: {
                      'Accept': 'application/json',
                      'Content-Type': 'application/json'
                    },
                  });
                  if (response.status != 200) {
                    return;
                  }
                }}
              >
                <h3 className='mr-10px ml-10px'>
                  Clear
                </h3>
              </button>
            </div>
            <IconButton text={!recipe?.outstanding_operations ? 'Checkout' : 'Loading...'} color='blue' onClick={() => {
              if (recipe?.outstanding_operations ) {
                return;
              }
              window.open('https://www.instacart.com/store/checkout_v3')
            }}/>
          </div>
        </main>
      </div>
    </>
  )
}

export default Home
