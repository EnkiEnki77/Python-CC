# you can import as many classes as you need into a file
from car import ElectricCar, Car

my_nissan = Car('nissan', '350z', 2008)
my_tesla = ElectricCar('tesla', 'model y', 2020)

my_nissan.odometer_reading()
my_tesla.battery.describe_battery()