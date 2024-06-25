# many of your programs will ask users to input certain kinds of info, maybe to store preferences in a game, or provide
# data for a visualization. youll store this info in data structures such as lists and dictionaries. 
# When users close the program youll almost always want to save the info they entered. A simple way to do this is 
# storing your data using the json module. It allows you to turn python data structures into JSON formatted strings
# and then load the data from that file the next time the program runs. 
# You can also use json to store data between different programs. Even if theyre not Python programs. 

from pathlib import Path 
import json

numbers = [2,5,3,65,42]

path = Path('numbers.json')
# Converts data structure to json
contents = json.dumps(numbers)
path.write_text(contents)