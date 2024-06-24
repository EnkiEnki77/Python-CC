from restaurants import Restaurant

class IcecreamStand(Restaurant):
    """Represents aspects of a Restaurant model, specific to an Icecream stand"""

    def __init__(self, restaurant_name, cuisine_type, *flavors) -> None:
        """Initializes class inheritance as well as local attributes"""
        super().__init__(restaurant_name, cuisine_type)

        self.flavors = flavors

    def available_flavors(self):
        """Displays flavors available"""
        print(f"\nThe available flavors are: ")
        print(*self.flavors, sep="\n")


baskin_robins = IcecreamStand('baskin robins', 'icecream', 'vanilla', 'choclate', 'strawberry')

baskin_robins.available_flavors()
