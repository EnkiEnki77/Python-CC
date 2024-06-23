prompt = "How old are you?: "

while True:
    age = int(input(prompt))

    if age <= 3:
        print("Your ticket is free!")
        break
    elif age <= 12:
        print("Your ticket is $10")
        break
    else:
        print("Your ticket is $15")
        break