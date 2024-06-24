class Restaurant:
    """Represents a model of a restaurant"""

    def __init__(self, restaurant_name, cuisine_type) -> None:
        """Initializes attributes for the restaurant model"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Gives restaurants name and cuisine"""
        print(f"The restaurant is called {self.restaurant_name} and it serves {self.cuisine_type}")

    def restaurant_open(self):
        """Tells customers whether restaurant  is open or not"""
        print("We're open, come on in!")

restaurant = Restaurant('Dominios', 'pizza')

print(restaurant.cuisine_type)
print(restaurant.restaurant_name)
restaurant.describe_restaurant()
restaurant.restaurant_open()