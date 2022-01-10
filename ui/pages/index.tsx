import type { NextPage } from 'next'
import Head from 'next/head'
import Image from 'next/image'
import { useRef, useState } from 'react'
import IconButton from '../components/IconButton'
import styles from '../styles/Home.module.css'


const OpenSource = () => (
  <svg width="266" height="80" viewBox="0 0 266 80" fill="none" xmlns="http://www.w3.org/2000/svg">
    <rect x="43.9502" y="27.9514" width="177.142" height="45.2014" rx="10" transform="rotate(-8.99559 43.9502 27.9514)" fill="#FFE2D6" fillOpacity="0.47"/>
    <path d="M75.2573 46.161C74.7254 42.8008 71.988 39.8991 67.7567 40.569C63.5254 41.2388 61.8181 44.8441 62.3529 48.222C62.8369 51.28 64.7496 53.3463 69.7098 52.5611C74.5634 51.7928 75.7442 49.2367 75.2573 46.161ZM69.3036 50.1105C66.5302 50.5495 64.8427 49.9054 64.4853 47.6476C64.1869 45.763 65.4868 43.4979 68.1535 43.0758C70.6959 42.6733 72.7272 44.3382 73.0452 46.3471C73.3942 48.5517 72.0415 49.677 69.3036 50.1105ZM80.6477 45.7815C80.0432 45.8772 79.9234 45.6957 79.853 45.2512C79.6138 43.74 79.6122 42.1183 80.238 41.5819C80.4943 41.3591 80.8386 41.2317 82.012 41.0459C85.2833 40.528 86.2577 41.1574 86.4209 42.1886C86.7221 44.0909 83.2967 45.3621 80.6477 45.7815ZM80.4148 50.7571C81.0371 50.6586 81.3513 50.2261 81.2387 49.515C81.1881 49.195 81.0775 48.9573 81.0128 48.5484C80.9593 48.2106 80.8853 47.8579 82.0708 47.6337C86.8344 46.6427 89.2358 44.6588 88.6954 41.2454C88.2901 38.6852 85.9026 37.8786 81.0669 38.6442C78.3467 39.0748 77.8274 39.2481 77.6763 40.3655C77.4431 42.1155 77.5458 44.031 77.816 45.7377C78.0693 47.3378 78.4629 48.7881 78.8488 49.7293C79.2376 50.6883 79.8103 50.8528 80.4148 50.7571ZM97.5843 47.9662C99.0038 47.7232 100.503 47.5224 101.789 47.2458C102.599 47.063 102.867 46.4556 102.738 45.6378C102.636 44.9977 102.188 44.4673 101.37 44.5968C99.7522 44.8529 97.8192 45.651 94.8858 46.1153C93.6768 46.3067 93.4644 46.231 93.2702 45.0043C93.0647 43.7065 93.3313 43.318 94.1846 43.1829C96.6559 42.7917 98.7314 42.6636 99.1936 42.5904C99.8158 42.4919 100.124 42.0239 100.026 41.4017C99.8909 40.5483 99.3584 40.5232 97.7761 40.7737C95.9271 41.0664 94.6789 41.3551 93.8255 41.4902C93.31 41.5718 93.1303 41.4727 93.0683 41.0816C92.8601 39.766 93.192 38.9845 94.2587 38.8156C97.1388 38.3597 99.0376 38.4965 100.086 38.3304C100.958 38.1925 101.197 37.5168 101.084 36.8056C100.983 36.1656 100.52 35.6558 99.4295 35.7919C98.4582 35.8728 96.8787 36.141 95.3497 36.3831C94.1586 36.5717 93.0208 36.7518 92.4397 36.8802C91.7314 37.0106 91.0278 37.286 90.9018 38.2171C90.6425 40.2628 90.768 43.013 91.0447 44.6458C91.2502 45.9437 91.3656 46.6726 91.5053 47.3248C91.7762 48.5758 92.3256 48.7075 93.3268 48.5855C94.4703 48.4409 96.002 48.2166 97.5843 47.9662ZM106.562 46.5267C107.522 46.3747 107.781 45.8234 107.655 45.0234C107.534 44.2589 106.619 42.5084 106.101 39.2372C105.952 38.2949 106.145 38.1367 106.359 38.1029C106.465 38.086 106.664 38.0729 106.808 38.1776C109.007 39.5242 110.552 41.6853 112.917 44.1903C113.908 45.2726 114.666 45.335 115.59 45.1887C116.479 45.0479 116.978 44.5134 117.017 43.6141C117.074 42.4752 116.842 40.7806 116.578 39.1095C116.299 37.3494 115.96 35.4349 115.642 34.4646C115.292 33.4083 114.639 33.3112 113.981 33.4154C113.217 33.5364 112.743 33.9942 112.897 34.972C113.007 35.6654 114.244 37.8387 114.852 41.6789C114.897 41.9633 114.854 42.1524 114.605 42.1918C114.41 42.2227 114.259 42.1919 114.104 42.016C111.502 39.1658 108.649 36.3371 107.065 35.3122C106.353 34.8417 105.969 34.7202 105.133 34.8525C104.582 34.9398 104.059 35.2048 103.808 35.9189C103.562 36.6686 103.626 38.9181 104.009 41.336C104.226 42.705 104.41 44.0973 104.829 45.3614C105.135 46.2606 105.602 46.6787 106.562 46.5267ZM132.601 33.7299C133.49 33.5892 133.706 32.8807 133.622 32.3473C133.391 30.8895 131.094 30.5423 128.427 30.9645C124.765 31.5442 123.226 33.3369 123.539 35.3103C123.865 37.3726 126.094 38.0951 129.345 37.799C132.129 37.5405 132.598 38.0859 132.711 38.7971C132.854 39.7038 132.051 40.2684 130.7 40.4823C127.659 40.9635 126.429 39.4088 124.971 39.6396C124.1 39.7775 123.813 40.4972 123.903 41.0661C124.157 42.6662 126.369 43.5187 129.907 42.9586C134.156 42.286 135.673 40.5879 135.35 38.5433C135.054 36.6766 133.583 35.6703 129.351 35.9939C126.612 36.1906 126.006 35.8128 125.902 35.1549C125.783 34.4082 126.566 33.8287 128.273 33.5585C130.229 33.2489 131.641 33.8819 132.601 33.7299ZM149.775 34.3645C149.243 31.0043 146.505 28.1026 142.274 28.7725C138.043 29.4423 136.335 33.0476 136.87 36.4255C137.354 39.4835 139.267 41.5498 144.227 40.7646C149.081 39.9962 150.262 37.4402 149.775 34.3645ZM143.821 38.314C141.048 38.753 139.36 38.1089 139.003 35.8511C138.704 33.9665 140.004 31.7014 142.671 31.2793C145.213 30.8768 147.245 32.5417 147.563 34.5506C147.912 36.7552 146.559 37.8805 143.821 38.314ZM161.632 32.0135C161.984 34.2358 161.044 35.2047 158.413 35.6213C155.995 36.004 154.514 35.4001 154.165 33.1956C153.819 31.0088 154.704 29.2286 154.555 28.2863C154.446 27.4835 153.865 27.1562 153.154 27.2688C152.23 27.4151 151.646 27.872 151.59 28.9014C151.545 30.1114 151.635 31.719 151.951 33.7102C152.55 37.497 154.831 39.013 158.76 38.391C163.418 37.6536 164.394 35.1847 163.859 31.8067C163.53 29.7266 163.291 28.2155 162.933 27.1058C162.613 26.1177 162.008 25.8672 161.083 26.0135C160.212 26.1514 159.737 26.7187 159.889 27.6788C160.038 28.621 161.272 29.7378 161.632 32.0135ZM166.697 26.5463C166.508 28.6903 166.725 30.7517 167.006 32.5296C167.201 33.7563 167.396 34.8735 167.684 35.7755C168.005 36.7636 168.618 36.7212 169.24 36.6227C170.058 36.4932 170.523 36.0916 170.424 35.4693C170.348 34.9893 169.88 33.9882 169.798 33.4726C169.686 32.7615 170.254 32.4347 171.783 32.1926C173.294 31.9534 174.527 33.0702 175.573 34.0346C176.531 34.9036 177.074 35.4554 178.816 35.1796C179.652 35.0474 180.142 34.4595 180.026 33.7306C179.914 33.0194 179.217 32.7652 178.086 32.5251C177.073 32.3393 175.772 31.725 175.275 31.3481C174.949 31.1265 175.052 30.855 175.337 30.7005C177.396 29.6638 178.549 28.4244 178.25 26.5398C177.856 24.0508 175.104 23.7029 171.477 24.277C170.784 24.3868 168.763 24.7432 168.152 24.9128C167.188 25.1565 166.744 25.5731 166.697 26.5463ZM168.822 30.1829C168.577 28.6361 168.66 27.2015 171.504 26.7512C173.833 26.3825 175.512 26.627 175.706 27.8538C175.892 29.0271 173.582 30.3222 170.222 30.8542C169.28 31.0033 168.951 31.0007 168.822 30.1829ZM188.748 33.7167C193.264 33.0018 194.558 31.0474 194.336 29.6429C194.226 28.9495 193.622 28.699 192.999 28.7975C192.661 28.8509 192.346 29.0466 192.045 29.3312C191.368 30.0034 190.642 30.829 188.651 31.1443C185.415 31.6565 183.931 30.798 183.587 28.6291C183.23 26.3712 184.677 24.5748 187.486 24.1302C189.601 23.7952 190.289 24.7981 190.779 25.249C191.278 25.7531 191.577 26.1432 192.483 25.9997C193.23 25.8815 193.415 25.3237 193.325 24.7548C193.072 23.1547 191.326 20.9891 187.219 21.6392C182.685 22.3569 180.635 25.5244 181.28 29.5957C181.792 32.8314 184.41 34.4034 188.748 33.7167ZM203.093 31.2636C204.512 31.0207 206.011 30.8198 207.298 30.5432C208.107 30.3604 208.376 29.753 208.246 28.9352C208.145 28.2952 207.696 27.7648 206.878 27.8942C205.261 28.1503 203.328 28.9484 200.394 29.4128C199.185 29.6042 198.973 29.5285 198.779 28.3017C198.573 27.0039 198.84 26.6154 199.693 26.4803C202.164 26.0891 204.24 25.961 204.702 25.8879C205.324 25.7894 205.633 25.3213 205.534 24.6991C205.399 23.8457 204.867 23.8207 203.284 24.0712C201.436 24.3639 200.187 24.6526 199.334 24.7877C198.818 24.8693 198.639 24.7702 198.577 24.379C198.368 23.0634 198.7 22.2819 199.767 22.113C202.647 21.6571 204.546 21.7939 205.595 21.6279C206.466 21.4899 206.705 20.8142 206.593 20.1031C206.491 19.463 206.028 18.9532 204.938 19.0894C203.967 19.1702 202.387 19.4385 200.858 19.6805C199.667 19.8691 198.529 20.0492 197.948 20.1777C197.24 20.308 196.536 20.5834 196.41 21.5146C196.151 23.5603 196.276 26.3105 196.553 27.9433C196.759 29.2411 196.874 29.97 197.014 30.6222C197.285 31.8732 197.834 32.005 198.835 31.8829C199.979 31.7384 201.51 31.5141 203.093 31.2636Z" fill="#FCB598"/>
    <path fillRule="evenodd" clipRule="evenodd" d="M26.408 70.1557C23.569 71.7561 20.9327 73.7676 18.3921 75.7358C17.8466 76.1614 17.7306 76.947 18.1676 77.4534C18.5703 77.9948 19.3491 78.0795 19.86 77.6886C22.3205 75.7792 24.8695 73.8198 27.5813 72.3004C28.1615 71.9788 28.381 71.2269 28.0618 70.6302C27.743 70.0339 26.9886 69.8345 26.408 70.1557Z" fill="#FCB598"/>
    <path fillRule="evenodd" clipRule="evenodd" d="M24.3561 54.6474C17.1594 54.5952 9.97826 55.4605 2.7536 55.2417C2.09387 55.2062 1.52033 55.7425 1.49799 56.4138C1.47599 57.0855 1.98765 57.6662 2.68206 57.667C9.91741 57.8965 17.1089 57.0416 24.3163 57.1044C25.0025 57.0969 25.5621 56.547 25.5751 55.8663C25.5538 55.2207 25.0423 54.6399 24.3561 54.6474Z" fill="#FCB598"/>
    <path fillRule="evenodd" clipRule="evenodd" d="M17.1093 34.0122C19.2878 35.9826 21.4662 37.9532 23.645 39.924C24.1202 40.3992 24.9035 40.3497 25.366 39.841C25.8281 39.332 25.7702 38.5809 25.2947 38.1054C23.1127 36.1315 20.9313 34.1578 18.7496 32.1842C18.2398 31.7437 17.4591 31.7955 16.9994 32.3069C16.5744 32.7837 16.5998 33.572 17.1093 34.0122Z" fill="#FCB598"/>
    <path fillRule="evenodd" clipRule="evenodd" d="M242.003 8.85836C244.659 7.36127 247.125 5.47957 249.502 3.63842C250.012 3.24033 250.12 2.5054 249.712 2.03168C249.335 1.52519 248.606 1.44596 248.129 1.81161C245.827 3.59786 243.442 5.43075 240.906 6.85212C240.363 7.15293 240.157 7.85636 240.456 8.41452C240.754 8.97235 241.46 9.15885 242.003 8.85836Z" fill="#FCB598"/>
    <path fillRule="evenodd" clipRule="evenodd" d="M243.922 23.366C250.655 23.4148 257.372 22.6054 264.131 22.8101C264.748 22.8432 265.285 22.3415 265.305 21.7135C265.326 21.0852 264.847 20.542 264.198 20.5413C257.429 20.3266 250.702 21.1263 243.96 21.0675C243.318 21.0745 242.794 21.589 242.782 22.2257C242.802 22.8296 243.281 23.373 243.922 23.366Z" fill="#FCB598"/>
    <path fillRule="evenodd" clipRule="evenodd" d="M250.701 42.6696C248.664 40.8264 246.626 38.9829 244.588 37.1393C244.143 36.6948 243.41 36.7411 242.978 37.217C242.545 37.6931 242.599 38.3958 243.044 38.8406C245.085 40.6871 247.126 42.5334 249.167 44.3796C249.644 44.7917 250.374 44.7432 250.804 44.2648C251.202 43.8188 251.178 43.0814 250.701 42.6696Z" fill="#FCB598"/>
  </svg>
)

const Arrow = () => (
  <svg width="97" height="290" viewBox="0 0 97 290" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M1 3C20 9 34.6379 13.6299 45 18.5C74.0532 32.1548 76.0799 40.3378 73.5 52.5C70.3283 67.4522 35.9687 56.9327 15.5677 49.914C14.5659 49.5693 13.748 50.8145 14.4765 51.5836C37.06 75.4262 77 127.332 77 167.5C77 209.5 51 262.667 38 284M38 284C40.1667 277.333 40.5 261.5 40 251C39.505 240.604 37.8333 224.667 36.5 218M38 284C41.0614 282.019 46.8795 276.629 53.3515 272C56.1478 270 64.8408 264.948 70 262C77 258 86.5 253.5 95.5 250" stroke="#FCB598" strokeWidth="5"/>
  </svg>
)




const Home: NextPage = () => {

  const [url, setURL] = useState('');
  const [loading, setLoading] = useState(false);
  const inputRef = useRef<HTMLInputElement>(null);

  const submitURL = async () => {
    setLoading(true);

    console.log("123")
    const response = await fetch('/setcurrentrecipe', {
        method: 'POST',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
      body: JSON.stringify({url: url})
    });

    console.log(response)
    
    if (!response.ok) { /* Handle */ }
    
    // If you care about a response:
    if (response.body !== null) {
    }

    setLoading(false);

    // Load the recipe
    window.location.href = '/recipe.html';
  }


  return (
    <>
      <Head>
        <title>Create Next App</title>
        <meta name="description" content="Generated by create next app" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <div className={styles.container}>
        
        <main className={styles.main}>
          <div className='flex flex-column w-60'>
            <div className='flex flex-column w-60 m-auto'>
              <div style={{position:'relative', top: '-1000%', left: '-20%'}}>
                <OpenSource/>
              </div>
              <h1>
                YOUR COOL INTERNET RECIPES GO HERE.
              </h1>
              <h3 className='mt-50px'>
                The struggle to motivate yourself to get your butt to the store for a new recipe is over: Feast delivers ingredients straight to your door.
              </h3>
              <div 
                className={styles.inputContainer + ' mt-70px'}
                onClick={() => {
                  inputRef.current?.focus();
                }}
              >
                <input 
                  className={styles.input} 
                  ref={inputRef} 
                  placeholder='Paste recipe URL here' 
                  value={url} 
                  onChange={(e) => {setURL(e.target.value)}}
                  onKeyDown={(e) => {
                    if (e.key == 'Enter') {
                      submitURL()
                    }
                  }}
                />
                <IconButton text={!loading ? "Get cookin'" : 'Loading'} color='black' onClick={submitURL}/>
              </div>
              {/* We put this here so the spacing still works*/}
              <div style={{visibility: 'hidden'}}>
                <OpenSource/>
              </div>
            </div>
          </div>
          <div style={{position: 'absolute'}}>
            <Arrow/>
          </div>
          <div className='w-40' style={{height: '100vh', backgroundImage: 'url("/landing.png")'}}>
          </div>
        </main>
      </div>
    </>
  )
}

export default Home