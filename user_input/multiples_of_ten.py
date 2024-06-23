prompt = "Give me a number, ill tell you if its a multiple of 10: "
number = int(input(prompt))

if number % 10 == 0:
    print(f"{number} is a multiple of 10")
else:
    print(f"{number} is not a multiple of 10")