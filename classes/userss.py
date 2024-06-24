class User:
    """Represents model of a user"""

    def __init__(self, first_name, last_name, user_name, age) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.age = age

    def describe_user(self):
        """Formats users info into a message"""
        print(f"\nFull name: {self.first_name.title()} {self.last_name.title()}\nUsername: {self.user_name}\nAge: {self.age}")

    def greet_user(self):
        """Greets user"""
        print(f"Hey {self.first_name.title()}, hows it going?")


enki = User('enki', 'layman', 'alayman', 25)
bat = User('bat', 'graves', 'bgraves', 22)

enki.describe_user()
enki.greet_user()
bat.describe_user()
bat.greet_user()