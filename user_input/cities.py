# If youd like to exit a while loop immediately without running any more code in the block than use the break keyword

prompt = "\nPlease enter the names of any cities youve visited."
prompt += "\n(Enter 'quit' to end the program) "

# A loop that has a condition of True will run forever unless it hits a break statement. You can also use break in for loops
# to keep it from completely going through a collection.
while True:
    cities = input(prompt)

    if cities == 'quit':
        break
    else:
        print(cities)