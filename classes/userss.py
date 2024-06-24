class User:
    """Represents model of a user"""

    def __init__(self, first_name, last_name, user_name, age) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        """Formats users info into a message"""
        print(f"\nFull name: {self.first_name.title()} {self.last_name.title()}\nUsername: {self.user_name}\nAge: {self.age}")

    def greet_user(self):
        """Greets user"""
        print(f"Hey {self.first_name.title()}, hows it going?")
    
    def increment_login_attempts(self):
        """Increases login attempt counter by 1"""
        self.login_attempts += 1
        print(f"{self.first_name} youve attempted to login {self.login_attempts} times")

    def reset_login_attempts(self):
        """Resets login attempts to 0"""
        self.login_attempts = 0
        print(f"Login attempts reset to 0")


# enki = User('enki', 'layman', 'alayman', 25)
# bat = User('bat', 'graves', 'bgraves', 22)

# enki.describe_user()
# enki.greet_user()
# bat.describe_user()
# bat.greet_user()