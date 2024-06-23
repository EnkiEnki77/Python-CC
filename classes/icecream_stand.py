from restaurant import Restaurant

class IcecreamStand(Restaurant):
    """Respect aspects of a restaurant, specific to an icecream stand"""

    def __init__(self, restaurant_name, cuisine_type, *flavors) -> None:
        """Initialize inheritance from Restaurant class and Icecream stands own attributes"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def flavors_available(self):
        """Lists out the flavors available"""
        print("\nThe flavors available are:")
        print(*self.flavors, sep="\n")

baskin_robins = IcecreamStand('baskin robins', 'icecream', 'vanilla', 'choclate', 'strawberry')

baskin_robins.flavors_available()