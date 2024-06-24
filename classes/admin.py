from userss import User

class Admin(User):
    """Represents aspects of a User model specific to an Admin"""

    def __init__(self, first_name, last_name, user_name, age, *priveleges) -> None:
        """Initializes class inheritance as well as local attributes"""
        super().__init__(first_name, last_name, user_name, age)

        self.priveleges = priveleges

    def show_priveleges(self):
        """Lists an admins priveleges"""
        print(f"\nThe user {self.user_name} has admin access with the following priveleges.")
        print(*self.priveleges, sep="\n")


admin_1 = Admin('enki', 'layman', 'elayman', 25, 'can add post', 'can edit post')

admin_1.show_priveleges()