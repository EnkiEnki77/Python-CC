prompt = "Enter a number, and ill tell you if its ever or odd: "
number = int(input(prompt))

if number % 2 == 0:
    print(f"{number} is evern")
else:
    print(f"{number} is odd")