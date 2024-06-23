# You can make arguments optional with default params

def format_name(first, last, middle=""):

    if middle: 
        print(f"{first} {middle} {last}")
    else:
        print(f"{first} {last}")

format_name('jimi', 'hendrix')