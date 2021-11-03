import argparse, os, random
from bs4 import BeautifulSoup

def create_list_of_foods() -> list:
    '''
    Creates a list of food words from wiktionary.org category pages using "beautiful soup"
    '''
    food_files = os.listdir("wiktionary") # list of filenames
    if food_files.count('.DS_Store') >= 1:
        food_files.remove('.DS_Store') 

    list_of_foods = list()

    for food_file in food_files:
        with open('wiktionary/' + food_file) as fp:
            content = fp.read()
            fp.close()
            soup = BeautifulSoup(content, 'html.parser')

            for li in soup.find(id="mw-pages").find_all('li'):
                food = li.find('a')['title']
                if list_of_foods.count(food) <= 0: # make sure there are no duplicates
                    list_of_foods.append(food)
    return list_of_foods

def find_ingredients_in_recipe(list_of_foods: list, filename: str) -> list:
    '''
    Takes the name of the file containing the recipe as an argument, converts the contents of the file to string format, 
    and returns the contents of the file as a string, returns a list of all ingredients found in the recipe
    '''
    with open(filename) as fp:
        content = fp.read()
        fp.close()

    list_of_ingredients = list()

    for food in list_of_foods:
        if content.find(food) != -1:
            list_of_ingredients.append(food)
    return list_of_ingredients

def pick_random_ingredient(l: list) -> str:
    return random.choice(l)

def generate_comment(original_ingredient: str, new_ingredient: str) -> str:
    comment = "This turns out so much better if you swap out the {oi} for {ni}. Sounds really weird but trust me".format(oi=original_ingredient, ni=new_ingredient)
    return comment

def main():

    # parsing the arguments
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-fn', '--filename', type=str, help='the filename of the txt file containing the recipe')
    args = parser.parse_args()
    src_filename = str(args.filename)

    # check if input file exists
    if (os.path.exists(src_filename) == False):
        raise Exception('File {fn} not found'.format(fn=src_filename))

    list_of_foods = create_list_of_foods()
    # print(len(list_of_foods)) # the total number of foods in list_of_foods

    list_of_ingredients = find_ingredients_in_recipe(list_of_foods, src_filename)

    for x in range(5):
        print(generate_comment(pick_random_ingredient(list_of_ingredients), pick_random_ingredient(list_of_foods)))

if __name__ == "__main__":
    main()