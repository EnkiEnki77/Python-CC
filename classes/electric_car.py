# You dont always have to create a whole new class from scratch if your new class essentially a special version of a class
# you already made. For example we have the general car class, so if we wanted to make an electric car class we could simply
# just inherit from the car class and then add on the additional attributes/methods. 

from car import Car

# First the child class takes the parent in as an argument

# You may find your classes getting really big describing certain attributes of something. You might recognize that part 
# the class can be written as a seperate class. When a few of the attributes pertain to one specific piece of the main clas
# such as a battery for an electric car.
class Battery:
    """Represent aspects of a battery for an electric car"""

    def __init__(self, battery_size=40) -> None:
        """Initialize attributes to describe the battery for the electric car"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Describe the size of the battery in the electric car."""
        print(f"This car has a {self.battery_size}-kwh battery.")

    def get_range(self):
        """Gives info about the range of the car based on the size of the battery"""
        range = 0
        if self.battery_size >= 40:
             range = 150
        elif self.battery_size >= 65:
            range = 225

        print(f"This car has a range of {range}")


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric cars"""

    # Next you make a call to the super function, the __init__ function of the parent class is a method of super because 
    # you passed the parent in as an argument. the child takes in the arguments the parent requires and passes them on to 
    # the parent.
    def __init__(self, make, model, year) -> None:
        super().__init__(make, model, year)
        # We can define the subclass instance as attribute of the main class 
        self.battery = Battery()

    def fill_gas_tank(self):
        """Overrides method from parent class, because electric cars dont have a gas tank"""
        print("This car has no gas tank, its electric")


my_leaf = ElectricCar('nissan', 'leaf', 2024)

my_leaf.odometer_reading()
print(my_leaf.get_descriptive_name())

# my_leaf.describe_battery()

my_leaf.fill_gas_tank()

my_leaf.battery.describe_battery()

my_leaf.battery.get_range()