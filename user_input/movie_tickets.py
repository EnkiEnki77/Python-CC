prompt = "How old are you?: "

active = True
while active:
    age = int(input(prompt))
 
    if age <= 3:
        print("Your ticket is free!")
        active = False
    elif age <= 12:
        print("Your ticket is $10")
        active = False
    else:
        print("Your ticket is $15")
        active = False