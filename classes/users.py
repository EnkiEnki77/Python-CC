class User:
    """Model of a person"""

    def __init__(self, first, last, username, age) -> None:
        self.first = first
        self.last = last
        self.username = username
        self.age = age

    def describe_user(self):
        print(f"\nName: {self.first} {self.last}\nUsername: {self.username}\nAge: {self.age}")

    def greet_user(self):
        print(f"\nHi {self.first}, how's it going?")

user_1 = User("Enki", "Layman", "elayman", 25)
user_1.describe_user()
user_1.greet_user()
user_1 = User("Bat", "Graves", "bgraves", 22)
user_1.describe_user()
user_1.greet_user()
