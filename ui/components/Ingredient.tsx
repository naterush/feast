import React from "react";
import { Ingredient } from "../pages/recipe";
import styles from '../styles/Ingredient.module.css'

const Edit = () => (
    <svg width="12" height="13" viewBox="0 0 12 13" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M8.5649 1.9178C8.69735 1.78534 8.8546 1.68027 9.02767 1.60858C9.20073 1.5369 9.38623 1.5 9.57355 1.5C9.76087 1.5 9.94636 1.5369 10.1194 1.60858C10.2925 1.68027 10.4497 1.78534 10.5822 1.9178C10.7147 2.05026 10.8197 2.20751 10.8914 2.38057C10.9631 2.55364 11 2.73913 11 2.92645C11 3.11377 10.9631 3.29926 10.8914 3.47233C10.8197 3.64539 10.7147 3.80265 10.5822 3.9351L3.7738 10.7435L1 11.5L1.75649 8.7262L8.5649 1.9178Z" stroke="#576FC8" strokeWidth="1.3" strokeLinecap="round" strokeLinejoin="round"/>
    </svg>
)

const Check = () => (
    <svg width="11" height="7" viewBox="0 0 11 7" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M9.13601 1L4.13601 6L1.86328 3.72727" stroke="white" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
    </svg>
)

const Ingredient = (props: {ingredient: Ingredient, recipeIngredient: Ingredient}): JSX.Element => {
    return (
        <div className={styles.container + ' w-100 text-left flex flex-row justify-content-space-between align-items-center mt-10px'}>
            <div>
                <p>
                    {props.ingredient.count}x {props.ingredient.ingredient} ({props.ingredient.unit})
                </p>
                <p>
                    {props.recipeIngredient.count}x {props.recipeIngredient.ingredient} ({props.recipeIngredient.unit})
                </p>
            </div>
            <div className='flex flex-row align-items-center mr-20px'>
                <button className={styles.edit + ' blue-button flex flex-row align-items-center mr-20px'}>
                    <Edit/> 
                    <div className='ml-5px'>
                        Edit
                    </div>
                </button>
                <div className={styles.checkbox + ' flex flex-row justify-content-center align-items-center'}>
                    <Check/>
                </div>
            </div>
            
        </div>
    )
}

export default Ingredient;