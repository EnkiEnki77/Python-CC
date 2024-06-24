# You should have a module level docstring that defines the uses of the classes in the module. Classes should be in a 
# module separate from any instances of that class. 
"""A set of classes that represent gas and electric cars"""
# You can contain multiple classes in a single module, but they should be related. Although if you get too many classes
# in one module or some classes are related to only one or a few of the other classes but not all you should abstract
# these classes into additional modules and import them into other modules as needed. For instance here we should actually
# have an electric_car module that contains the ElectricCar and Battery classes and then just import the Car module in. 
# Since ElectricCar inherits from it. Rule of thumb, parent and child classes should be in separate modules. classes that
# have a compositional relationship can be in the same module.

class Car:
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year) -> None:
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        # Attributes can be defined without being passed in as parameters
        self.odometer = 0

    def get_descriptive_name(self):
        """Get a neatly formatted descriptive name of the car"""
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name.title()
    
    def odometer_reading(self):
        print(f"The odometer is currently at: {self.odometer}")

    def update_odometer(self, mileage):
        """Updates odometer attribute"""
        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            print("You can't roll back the odometer.")

    def add_mileage(self, miles):
        self.odometer += miles

    def fill_gas_tank(self):
        """FIlls gas tank"""
        print("Gas tank is filled")
    
# my_new_car = Car('nissan', '370z', 2012)
# my_old_car = Car('ford', 'taurus', 1994)
# print(my_new_car.get_descriptive_name())
# print(my_old_car.get_descriptive_name())
# my_new_car.odometer_reading()

# There are three ways to modify the value of an attribute. The simplest way is to reassign the attribute directly
# my_new_car.odometer = 12
# my_new_car.odometer_reading()

# The second way is to update the attribute through a method
# my_new_car.update_odometer(28)
# my_new_car.odometer_reading()

# my_new_car.update_odometer(14)

# my_new_car.add_mileage(100)

# my_new_car.odometer_reading()

# You dont always have to create a whole new class from scratch if your new class essentially a special version of a class
# you already made. For example we have the general car class, so if we wanted to make an electric car class we could simply
# just inherit from the car class and then add on the additional attributes/methods. 


# First the child class takes the parent in as an argument

# You may find your classes getting really big describing certain attributes of something. You might recognize that part 
# the class can be written as a seperate class. When a few of the attributes pertain to one specific piece of the main clas
# such as a battery for an electric car.
class Battery:
    """Models aspects of a battery for an electric car"""

    def __init__(self, battery_size=40) -> None:
        """Initialize attributes to describe the battery for the electric car"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Describe the size of the battery in the electric car."""
        print(f"This car has a {self.battery_size}-kwh battery.")

    def get_range(self):
        """Gives info about the range of the car based on the size of the battery"""
        range = 0
        if self.battery_size == 40:
             range = 150
        elif self.battery_size == 65:
            range = 225
        # print(self.battery_size)
        print(f"This car has a range of {range}")

    def upgrade_battery(self):
        if self.battery_size < 65:
            self.battery_size = 65
            print(f"Battery size was upgraded to 65-kwh!")
        else:
            print("Battery is already at the highest tier.")



class ElectricCar(Car):
    """Models aspects of a car, specific to electric cars"""

    # Next you make a call to the super function, the __init__ function of the parent class is a method of super because 
    # you passed the parent in as an argument. the child takes in the arguments the parent requires and passes them on to 
    # the parent.
    def __init__(self, make, model, year) -> None:
        super().__init__(make, model, year)
        # We can define the instance of another class  as attribute of the main class. This is called composition. 
        
        self.battery = Battery()

    def fill_gas_tank(self):
        """Overrides method from parent class, because electric cars dont have a gas tank"""
        print("This car has no gas tank, its electric")
