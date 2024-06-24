
class Priveleges:
    """"Represents a Priveleges model which through composition is a piece of a User class"""

    def __init__(self, user_name, priveleges) -> None:
        """Initializes class attributes"""
        self.user_name = user_name
        self.priveleges = priveleges

    def show_priveleges(self):
        """Lists an admins priveleges"""
        print(f"\nThe user {self.user_name} has admin access with the following priveleges: ")
        print(*self.priveleges, sep="\n")