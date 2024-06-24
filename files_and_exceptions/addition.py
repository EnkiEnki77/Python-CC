print("Give me two numbers and ill add them together")
print("Press 'q' to quit")

while True:

    first_number = input("\nFirst Number: ")
    if first_number == 'q':
        break
    second_number = input("Second Number: ")
    if second_number == 'q':
        break
    
    try:
        add = int(first_number) + int(second_number)
    except ValueError:
        print('Only numbers are acceptable input. Unless youre trying to quit, in which case press "q"')
    else:
        print(f"{first_number} + {second_number} = {add}")