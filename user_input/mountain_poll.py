# You can collect as much user input as youd like with a single pass through of a while loop. Meaning you can fill up 
# a whole dictionary.

responses = {}

poll_active = True
while poll_active:
    name = input("\nWhat is your name?")
    response = input("\nWhat mountain would you like to climb someday? ")

    responses[name] =  response

    repeat = input("Would you like to let another person respond? (yes/no)")
    if repeat == 'no':
        poll_active = False

print("\n---Poll results---")
for name, mountain in responses.items():
    print(f"{name} would like to climb {mountain}")
