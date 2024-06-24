from pathlib import Path

path = Path('files_and_exceptions/dark_web.txt')

def gimme_yo_names_chumps():
    """Demands a users name, and then saves it on the dark web for nepharious purposes later on."""
    prompt = "\nHey chump, gimme yo name. Or else."
    prompt += "\nOr you gonna run? (type quit)"

    while True:
        name = input(prompt)
        
        if name == 'quit':
            break
        else:
            if path.exists():
                # To make each string you write to the file go on its own line this is how you have to do things
                file_text = path.read_text()
                file_text += f"\n{name}"
                path.write_text(file_text)
            else:
                path.write_text(name)

gimme_yo_names_chumps()