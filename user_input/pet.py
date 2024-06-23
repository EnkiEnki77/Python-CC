# We can use a while loop to remove all instances of something from a list

pets = ['cat', 'bird', 'dog', 'cat', 'duck', 'cat']

while 'cat' in pets:
    pets.remove('cat')

print(pets)