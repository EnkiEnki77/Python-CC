# You can simplify class names by setting an alias for them.
from electric_car import ElectricCar as EC

my_leaf = EC('Toyota', 'Leaf', 2024)

print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()
my_leaf.battery.upgrade_battery()

# You should always instiate classes in a separate file from the modules the class lives in otherwise youll be creating
# those instance in any other files you import the class into. The classs module should have no instances of the class. 