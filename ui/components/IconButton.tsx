import Image from "next/image";
import React from "react";
import styles from '../styles/IconButton.module.css'


const IconButton = (props: {text: string, color: 'black' | 'blue', onClick: () => void}): JSX.Element => {
    return (
        <button 
            className={styles.button + ' flex flex-row align-items-center'} 
            style={{backgroundColor: props.color == 'black' ? '#303030' : '#576FC8'}}
            onClick={props.onClick}
        >
            <div className='mr-5px' style={{color: 'white'}}>
                {props.text}
            </div>
            <svg className='ml-5px' width="21" height="11" viewBox="0 0 21 11" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path fillRule="evenodd" clipRule="evenodd" d="M19.8825 1.41949C15.9411 8.74847 8.06768 11.7281 0.755008 7.60207C0.511567 7.46468 0.202858 7.55057 0.0654659 7.79101C-0.0719257 8.03574 0.0139533 8.34486 0.257394 8.48225C8.09559 12.9088 16.549 9.75315 20.7738 1.90036C20.9061 1.65563 20.8138 1.34645 20.5677 1.21336C20.3217 1.08455 20.0147 1.17476 19.8825 1.41949Z" fill="white"/>
                <path d="M6.90777 4.45884C7.72193 4.45884 8.38196 3.79884 8.38196 2.98467C8.38196 2.1705 7.72193 1.5105 6.90777 1.5105C6.0936 1.5105 5.43359 2.1705 5.43359 2.98467C5.43359 3.79884 6.0936 4.45884 6.90777 4.45884Z" fill="white"/>
                <path d="M13.0118 2.89072C13.81 2.89072 14.4572 2.24361 14.4572 1.44536C14.4572 0.647103 13.81 0 13.0118 0C12.2135 0 11.5664 0.647103 11.5664 1.44536C11.5664 2.24361 12.2135 2.89072 13.0118 2.89072Z" fill="white"/>
            </svg>
        </button>
    )
}

export default IconButton;