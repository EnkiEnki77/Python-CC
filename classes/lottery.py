from random import randint

lottery = [1, 3, 42, 12, 51, 63, 24, 23, 64, 41, 'a', 'e', 'd', 'y', 'j']

winning_lot = ''

for num in range(1, 5):
    # print(randint(0, len(lottery) - 1))
    
    winning_lot += f"{str(lottery[randint(0, len(lottery) - 1)]).title()}, "

print(f"Anyone who gets a lottery ticket with these numbers/letters wins!: {winning_lot[:-2]}")