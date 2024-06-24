from userss import User
from priveleges import Priveleges

class Admin(User):
    """Represents aspects of a User model specific to an Admin"""

    def __init__(self, first_name, last_name, user_name, age, *priveleges) -> None:
        """Initializes class inheritance as well as local attributes"""
        super().__init__(first_name, last_name, user_name, age)

        # Utilize composition to give the Admin class priveleges
        self.priveleges = Priveleges(user_name, priveleges)

   


admin_1 = Admin('enki', 'layman', 'elayman', 25, 'can add post', 'can edit post')

admin_1.priveleges.show_priveleges()