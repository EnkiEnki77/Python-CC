# Dictionaries allow you to connect pieces of related info
alien_0 = {'color': 'green', 'points': 5}

# you can then access the keys of the dictionarie using bracket noatation
print(alien_0['color'])

# Dictionaries in python are a collection of key/value pairs. You use the key to access its value. ITs essentially a list
# of variables. 

# You can add a new key value pair by accessing a key that doesnt exist yet and assigning a value. YOu can also access a key
# that does exist and assign it a new value this way

alien_0['x-position'] = 0
print(alien_0)

# Generally when you have a dictionary that is full of user supplied data or data generated automatically you would start
# the dictionary off as empty 
alien_0 = {}

# Say we wanted to increment a counter stored in a dictionary based off the previous value of the counter.
counter = {'count': 1}
print(counter)
counter['count'] = counter['count'] + 1
print(counter)

# To remove a key/value pair del the key
del counter['count']
print(counter)

# If youre trying to grab a key from a dictionary and there's a chance it doesnt exist use get instead to avoid a 
# traceback error
# It takes the key desired as an argument, and a message to be displayed if that key doesnt exist.
points = alien_0.get('points', 'points not assigned')
print(points)

# You can loop through a dictionary using the following syntax
user_0 = {
    'username': 'efermi',
    'f_name': 'elonzo',
    'l_name': 'fermi'
}

# The items() method returns a sequence of key value pairs, the two variables key and value hold these.
for key, value in user_0.items():
    print(f"The {key} is {value}")

# looping through all key value pairs like this works best for dictionaries that store the same kind of data for all key/
# values.

# If you need access to just the keys of the object, instead of using the items method use keys
for key in user_0.keys():
    print(key)

# Looping through keys is actually the default when looping through a dictionary, so the above is the same as 
for key in user_0:
    print(key)

# You can access the value of other dictionaries using the keys youre loopiong through
friends = ['phil', 'sarah']
for key in user_0:
    if key in friends:
        print(user_0[key])

# Keys is not only for looping, you can use it in conditional statements to find out of a certain value exists as a key
# within a dictionary
if 'erin' not in user_0.keys():
    print('Please take our poll\n')

favorite_languages = {
    "Enki": "Python",
    "Bat": "Javascript",
    "Keith": "C",
    "Robert": "C++",
    "Nathaniel": "Javascript"
}

print(*favorite_languages, sep="\n")

# Looping through a dictionary returns the items in the order they were inserted, but you can instead decide to sort the 
# keys as they are returned from the for loop using the sorted function
for name in sorted(favorite_languages):
    print(name)

# If youre strictly interested in the values of a dictionary use the values method.
for language in favorite_languages.values():
    print(language)

print("\n")
# Using the values method can be useful for small amounts of data, but given a large amount youll likely have many 
# duplicates, to remove any duplicates wrap the call in a set function. 
for language in set(favorite_languages.values()):
    print(language)

# A set looks like a dictionary, but it doesnt have key value pairs, and it does not retain items in anny particular order
languages = {"Python", "C", "Javascript", "Python"}
print(languages)
    