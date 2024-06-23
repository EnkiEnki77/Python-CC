class Restaurant:
    """Model for a restaurant"""

    def __init__(self, restaurant_name, cuisine_type) -> None:
        """"initialize restaurant_name and cuisine_type attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Describes restaurant"""
        print(f"The restaurant is called {self.restaurant_name} and it serves {self.cuisine_type}")

    # Even if the method doesnt use self, it must be a param, because its passed into all methods by default.
    def resaurant_open(self):
        """Indicates that the restaurant is open"""
        print("We're open, come on in!")

Quiznos = Restaurant("Quizno's", "subs")

print(Quiznos.restaurant_name)
print(Quiznos.cuisine_type)

Quiznos.describe_restaurant()
Quiznos.resaurant_open()