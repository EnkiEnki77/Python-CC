# Saving data with json is useful when working with user generated data, because if you dont save your users data 
# somehow itll be lost when they close the program. 

from pathlib import Path 
import json

# After your code is working you should always see if you can refactor it into more concise code such as functions
# with specific jobs that work together.

def greet_user():
    # Functions should preferably only be doing one task, if your functions are doing multiple you should probably 
    # refactor even further.
    """Greet the user by name"""
    path = Path('username.json')
    username = get_stored_username(path)

    if username:
        print(f"Welcome back {username}")
    else:
        username = get_new_username(path)
        print(f"We'll remember you {username}")


def get_stored_username(path):
    """Get stored username if available"""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else: 
        return None
    

def get_new_username(path):
    """Prompts for user to enter a new username, and stores it in JSON"""
    username = input("What is your username?: ")
    content = json.dumps(username)
    path.write_text(content)
    return username
    
        
        
def __main__():
    # If you define all your functions first and then execute the logic of your program in the main function at the bottom
    # You dont have to worry about which order you defined all the functions
    """Main function that runs the program"""
    greet_user()

__main__()


    

