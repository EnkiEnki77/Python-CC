from random import randint, choice

import string

def generate_possible_chars():
    """Generates the list of possible characters that will be picked from for the winning lot"""
    # Get a string of all the lowercase letters in the alphabet
    alphabet = string.ascii_uppercase
    # Generate a list of the nums from 1 - 100
    possible_chars = list(range(1, 101))
    # Append the letters of the alphabet to the list of numbers
    for letter in alphabet:
        possible_chars.append(letter)
    
    return possible_chars

def create_lot():
    """Function that generates a 6-digit winning lot of numbers/letters"""

    # Generates list of possible chars for winning lot
    possible_chars = generate_possible_chars()

    # String that will be returned as the winning lot
    lot = ''
    # Randomly picks the six characters for the winning lot from the possible characters.
    for char in range(1, 3):
        lot += f"{str(choice(possible_chars))}, "

    print(lot[:-2])
    # Formats the winning lot string correctly and then returns it
    return lot[:-2]

# create_lot()
        

