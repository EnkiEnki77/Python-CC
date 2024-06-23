import pizza
# You can import files as modules in order to acces their functions. Modules are files ending in .py that contain code
# youd like to execute. 
from pizza import make_pizza
# You can also import individual functions from a module.
# You can also give modules and functions an alias in case you already have something in the program named their original 
# name
import pizza as p
from pizza import make_pizza as mp

# If you want to just import all functions from a module
from pizza import *


# Any functions within the module can now be used as methods of that module.

pizza.make_pizza('olives')

make_pizza('pepperoni')