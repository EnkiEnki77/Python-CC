prompt = "How many people will be at your table this evening?: "
people = int(input(prompt))

if people > 8:
    print("Youll have to wait for a table")
else:
    print("Your table is ready!")
