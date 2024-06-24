from pathlib import Path

path = Path('files_and_exceptions/guest.txt')

def gimme_yo_name():
    """Demands a users name, and then saves it on the cloud for nepharious purposes later on."""

    name = input("Hey chump, gimme yo name. Or else. ")

    path.write_text(name)

gimme_yo_name()