import argparse, os, random, requests
from os import exists
import bs4 as BeautifulSoup

# soup = BeautifulSoup(html_doc, 'html.parser')

def create_list_of_foods() -> list:
    '''
    Creates a list of food words from wiktionary.org category en:Foods using "beautiful soup"

    note to future Sam: this is the tricky part
    '''


    return list()

def find_ingredients_in_recipe(filename: str) -> list:
    '''
    Takes the name of the file containing the recipe as an argument, converts the contents of the file to string format, 
    and returns the contents of the file as a string, returns a list of all ingredients found in the recipe
    '''
    return list()

def pick_ingredient_to_be_replaced(ingredients: list) -> str:
    return random.choice(ingredients)


def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-fn', '--filename', type=str, help='the filename of the txt file containing the recipe')
    args = parser.parse_args()
    src_filename = args.filename

    if (exists(src_filename) == False):
        raise Exception('File {fn} not found'.format(fn=src_filename))

    foods = create_list_of_foods()

    recipe_ingredients = find_ingredients_in_recipe(src_filename)





if __name__ == "__main__":
    main()