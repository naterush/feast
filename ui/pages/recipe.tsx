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
}
export interface IngredientPair {
  recipe_ingredient: Ingredient;
  cart_ingredient: Ingredient;
  other_ingredient_links?: IngredientLink[];
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

  console.log(recipe);

  const loadData = async () => {
    const response = await fetch('/getcurrentrecipe', {
        method: 'GET',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
    });

    setRecipe(JSON.parse(await response.text()))
  }

  useEffect(() => {
    loadData()
  }, [])

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
                <Ingredient key={i} ingredient={ingredientPair.cart_ingredient} recipeIngredient={ingredientPair.recipe_ingredient}/>
              )
            })}
          </div>
          <div className='w-100 flex flex-row justify-content-space-between mt-30px'>
            <button className='blue-button'>
              <h3 className='mr-10px ml-10px'>
                <Link href='/'>
                  Back
                </Link>
              </h3>
            </button>
            <IconButton text='Checkout' color='blue' onClick={() => {
              window.open('https://www.instacart.com/store/checkout_v3')
            }}/>
          </div>
        </main>
      </div>
    </>
  )
}

export default Home
