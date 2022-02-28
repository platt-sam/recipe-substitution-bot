# recipe-substitutor

Based on a [Tumblr post](https://img.ifunny.co/images/55d6c06960fbca7d63c814af95689502bf4060d6b0d525cff72523f8f4f78263_1.jpg), this program generates comments for recipe sites suggesting that a random ingredient from the recipe is substituted with one randomly chosen from a massive list of ingredients.

## How to Run this Program

> python3 main.py -fn 'foo.txt'

or

> python3 main.py --filename 'foo.txt'

where foo.txt refers to the filename (including the path) of the file containing a list of ingredients for a recipe.

## Known Issues
### Offensive or Strange Food Words
There are some foods that may contain offensive words or words that do not make sense as ingredients. I am working to add more words to the filter. If you find something I missed, please let me know.

### Program is Slow
I've switched to grabbing live versions of the Wiktionary category pages using the requests library, unfortunately this is much slower. I may optimize it more in the future, but please be aware that the program takes about five seconds to run (depending on factors like your internet connection).

## Program Environment
This program was developed on a computer running Python 3.10.0. Mileage may vary if you are using a different version of Python. Some packages may need to be installed in order to run this program on your computer.

## Test Input
The links to the sources of the test input are listed in test_input_sources.txt. If you own one of the recipes used as test input and would like me to remove it, let me know and I will.

