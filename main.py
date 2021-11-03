import argparse, os, random, requests
from bs4 import BeautifulSoup

def create_list_of_foods() -> list:
    '''
    Creates a list of food words from wiktionary.org category en:Foods using "beautiful soup"

    note to future Sam: this is the tricky part
    '''
    food_files = os.listdir("wiktionary") # list of filenames
    if (food_files[0] == '.DS_Store'): # remove .DS_Store file from the list if it exists
        food_files.pop(0)

    list_of_foods = list() # list of food words

    for food_file in food_files:
        fn = 'wiktionary/' + food_file
        
        with open(fn) as fp:
            content = fp.read()
            fp.close()
            soup = BeautifulSoup(content, 'html.parser')

            for li in soup.find(id="mw-pages").find_all('li'):
                list_of_foods.append(li.find('a')['title'])
        
    return(list_of_foods)

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
    src_filename = str(args.filename)

    if (os.path.exists(src_filename) == False):
        raise Exception('File {fn} not found'.format(fn=src_filename))

    foods = create_list_of_foods()

    # recipe_ingredients = find_ingredients_in_recipe(src_filename)





if __name__ == "__main__":
    main()