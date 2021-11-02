import argparse, os
from os import exists

def get_string_from_file(filename: str) -> str:
    '''
    Takes the name of the file containing the recipe as an argument, returns the contents of the file as a string
    '''

    return "lorem ipsum dolor sit amet recipe"

def create_food_dict() -> list:
    '''
    Creates a list of food words from wiktionary.org category en:Foods using "beautiful soup"
    '''

    return list()

def find_ingredients_in_recipe(recipe: str) -> list:
    '''
    Takes the string representation of the recipe as an argument, returns a list of all ingredients found in the recipe
    '''
    return list()


def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-fn', '--filename', type=str, help='the filename of the txt file containing the recipe')
    args = parser.parse_args()
    src_filename = args.filename

    if (exists(src_filename) == False):
        raise Exception('File {fn} not found'.format(fn=src_filename))

    create_food_dict()

    get_string_from_file(src_filename)





if __name__ == "__main__":
    main()