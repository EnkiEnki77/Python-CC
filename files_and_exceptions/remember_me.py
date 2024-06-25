# Saving data with json is useful when working with user generated data, because if you dont save your users data 
# somehow itll be lost when they close the program. 

from pathlib import Path 
import json

path = Path('username.json')
name = None

if path.exists():
    contents = path.read_text()
    # Converts data back to the actual type it was.
    username = json.loads(contents)

    print(f"Welcome back {contents}")
else:
    # Saves input from user as a string
    username = input("What is your username?: ")

    # Grabs path to username.json file
    path = Path('username.json')
    # Converts user input string to json
    content = json.dumps(username)
    # Writes user input json to json file
    path.write_text(content)

    print(f"We'll remember you {username}")
    

