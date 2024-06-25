from pathlib import Path
import json

def give_fav_number(path):
    """recalls your favorite number"""
    fav_num = path.read_text()
    fav_num = json.loads(fav_num)
    return fav_num

def ask_for_fav_number(path):
    """Asks what your fav num is and remembers"""
    prompt = "Tell me sir, what is your favorite number?"
    answer = input(prompt)
    answer = json.dumps(answer)
    path.write_text(answer)   
    return(answer) 

def my_fav_number():
    """Tells you your favorite number. Or asks for it."""
    path = Path('fav_number.json')
    fav_num = give_fav_number(path)

    if fav_num:
        print(f"Ah, a man of culture, your fav number is {fav_num}")
    else:
        fav_num = ask_for_fav_number(path)
        print(f"Ah, so your fav number is {fav_num}. Ill remember that!")

my_fav_number()
