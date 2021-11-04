import argparse, os, random, requests, wordfilter
from bs4 import BeautifulSoup
from wordfilter import Wordfilter

def create_list_of_foods() -> list:
    '''
    Creates a list of food words from wiktionary.org category pages using "beautiful soup"
    '''

    list_of_foods = list()

    with open('wiktionary_categories.txt') as fp:
        categories = fp.read()
        fp.close()
        
    for category in categories.splitlines():
        r = requests.get(category, timeout=5)
        r.encoding = 'utf-8'
        soup = BeautifulSoup(r.text, 'html.parser')

        for li in soup.find(id="mw-pages").find_all('li'):
            food = li.find('a')['title']
            if list_of_foods.count(food) <= 0: # make sure there are no duplicates
                list_of_foods.append(food)

    return filter_list_of_foods(list_of_foods)

def filter_list_of_foods(list_of_foods: list) -> list:
    wordfilter = Wordfilter()
    wordfilter.addWords(['arse', 'baby beef', "breast milk", 'cow', 'cup', 'cuppa', 'fuck', 'good egg', 'heal-all', 'human burger', 'lacta', 'latte art', "mother's milk", 'sarcophagic', 'sessionable', 'shit', 'take the gilt off the gingerbread', 'tea cosy', 'tea house', 'tea room', 'turd']) # add additional words to filter
    
    for food in list_of_foods:
        if (wordfilter.blacklisted(food) == True): # if the food contains a blacklisted word
            list_of_foods.remove(food) # remove that food from the list of foods
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
    
    # for filtering
    print(str(len(list_of_foods)) + " food words found") # the total number of foods in list_of_foods
    for x in range(10):
        print(random.choice(list_of_foods))
    exit()
    

    list_of_ingredients = find_ingredients_in_recipe(list_of_foods, src_filename)

    for x in range(5):
        print(generate_comment(random.choice(list_of_ingredients), random.choice(list_of_foods)))

if __name__ == "__main__":
    main()