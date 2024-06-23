# When you need to treat input as a number use the int() function, it converts input into a number
prompt = "How tall are you in inches?: "
height = int(input(prompt))


if height >= 48:
    print("Youre tall enough to ride!")
else:
    print("Grow a bit first.")