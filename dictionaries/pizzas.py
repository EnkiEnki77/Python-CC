# It can sometimes be useful to store a list in a dictionary. If a key for something youre describing could have multiple
# values such as how a pizza could have multiple toppings it makes sense to store these values as a list under one key.

pizza = {
    "crust": "thick",
    "toppings": ["mushrooms", "pepperoni"]
}

print(f"You ordered a {pizza['crust']}-crust pizza, with the following toppings:  ")
for topping in pizza['toppings']:
    print(f"\t{topping}")

# Nest a list inside a dictionary anytime you want more than one value associated with a single key. 

# Dont nest too deeply. If youre nesting any more than one to two levels theres likely a simpler way to solve the problem.

# You can also nest dictionaries in dictionaries, say we have a dictionary where the keys are a users username, and the 
# values are a dictionary of the rest of their info

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton'
    }, 

    'mcurrie': {
        'first': 'marie',
        'last': 'currie',
        'location': 'jeruselum'
    }
}

for username, user_info in users.items():
    print(f"username: {username}")
    print(f"\tfull name: {user_info['first'] + ' ' + user_info['last']}")

# again each nested dictionary should be identical so that they can be more easily looped through.
 