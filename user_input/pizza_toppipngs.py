prompt = "\nWhat toppings would you like on your pizza?: "
prompt += "\n (Enter 'quit' to exit)"

while True:
    message = input(prompt)

    if message == 'quit':
        break
    else: 
        print(f"Ill add {message} to your pizza!")