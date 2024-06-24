class Restaurant:
    """Represents a model of a restaurant"""

    def __init__(self, restaurant_name, cuisine_type) -> None:
        """Initializes attributes for the restaurant model"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Gives restaurants name and cuisine"""
        print(f"The restaurant is called {self.restaurant_name} and it serves {self.cuisine_type}")

    def restaurant_open(self):
        """Tells customers whether restaurant  is open or not"""
        print("We're open, come on in!")

    def set_number_served(self, served):
        """Sets the number of customers served"""
        self.number_served = served
        print(f"We've now served {self.number_served} customers!")

    def increment_number_served(self, served):
        """increments the number of customers served"""
        self.number_served += served
        print(f"We've now served {self.number_served} customers. Its gone up by {served}!")

# restaurant = Restaurant('Dominios', 'pizza')

# print(restaurant.cuisine_type)
# print(restaurant.restaurant_name)
# restaurant.describe_restaurant()
# restaurant.restaurant_open()

# burger_king = Restaurant('Burger King', 'burgers')
# dairy_queen = Restaurant('Dairy Queen', 'icecream')
# little_caesars = Restaurant('Little Caesars', 'pizza')

# burger_king.describe_restaurant()
# dairy_queen.describe_restaurant()
# little_caesars.describe_restaurant()