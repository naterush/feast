# feast - munch a bunch.

Feast is open source meal delivery tooling. 

1. Find the URL of a recipe you want to cook.
2. Paste it into feast, which will parse the recipe and add the proper amount of each ingredient to your Instacart.
3. Checkout on Instacart.

Please see instructions and disclaimer below for proper usage instructions.

# Running Feast

Feast is not a web-app, and instead is software you run on your machine. Follow the instructions below to get setup.

## Python3 and Node

1. Make sure you have Python 3.6 or above installed.
2. Second, make sure you have node installed, so you can run the next project that is the Feast frontend.

## Setting up Selenium

1. First, make sure you have Chrome installed

## Running Feast for the first time

TODO. Talk about login.

## TODOs before Alpha Release

1. Specify and implement the editing functionality. You should just be able to change the ingredient at a specific index to a different ingredient (a dropdown, or something).
2. Test on 25 most popular all-recipies recipes, and fix up the ingredient parser to handle all the found common cases.

# Benchmarks

1. 1min10seconds for 3 ingredients was starting point.
2. 41 seconds for 3 ingredients, after optimizing timeouts to backoff with a delay.
3. 34 seconds for 3 ingredients, after adding 5 tabs that can be searched at once.
4. 25 seconds for 3 ingredients, after optimizing the link searching. This is probably as quick as I can get it. 

## Disclaimer

This software should not be used to break any terms and conditions of any other software projects. Please run this code at your own risk, after reading the terms and conditions for any services it may interact with.
