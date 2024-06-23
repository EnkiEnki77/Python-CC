class Restaurant:
    """Model for a restaurant"""

    def __init__(self, restaurant_name, cuisine_type) -> None:
        """"initialize restaurant_name and cuisine_type attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0 

    def describe_restaurant(self):
        """Describes restaurant"""
        print(f"The restaurant is called {self.restaurant_name} and it serves {self.cuisine_type}")

    # Even if the method doesnt use self, it must be a param, because its passed into all methods by default.
    def resaurant_open(self):
        """Indicates that the restaurant is open"""
        print("We're open, come on in!")

    def set_number_served(self, customers):
        """Updates number of customers served"""
        self.number_served = customers
        print(f"Number of customers served: {self.number_served}")

    def increment_number_served(self, customers):
        """Increments number of customers served"""
        self.number_served += customers
        print(f"Number of customers served: {self.number_served}")

Quiznos = Restaurant("Quizno's", "subs")
Dominos = Restaurant("Domino's", "pizza")
Burger_King = Restaurant("Burger King", "burgers")

print(Quiznos.restaurant_name)
print(Quiznos.cuisine_type)

Quiznos.describe_restaurant()
Quiznos.resaurant_open()

Dominos.describe_restaurant()
Burger_King.describe_restaurant()

restaurant = Restaurant("restaurant", 'sandwhiches')

print(restaurant.number_served)
restaurant.number_served = 24

print(restaurant.number_served)
restaurant.set_number_served(24)
restaurant.increment_number_served(20)