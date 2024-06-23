class Car:
    """A model for a car"""

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