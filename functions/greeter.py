# You can use functions in while loops. Pass in user input as arguments

def format_name(first, last, middle=""):

    if middle: 
        print(f"{first} {middle} {last}")
    else:
        print(f"{first} {last}")


while True:
    f_name = input("\nWhats your first name?: ")
    l_name = input(f"\nWhats your last name?: ")

    formatted_name = format_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")

    break