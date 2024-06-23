person = {
    'first': 'bat',
    'last': 'graves',
    'age': 22,
    'location': 'Salem, VA'
}

person2 = {
    'first': 'tim',
    'last': 'henson',
    'age': 30,
    'location': 'Plano, Texas'
}

person3 = {
    'first': 'enki',
    'last': 'layman',
    'age': 25,
    'location': 'Salem, VA'
}

people = [person, person2, person3]

for person in people:
    print(f"Full name: {person['first'].title()} {person['last'].title()}\nage: {person['age']}\nlocation: {person['location']}\n")