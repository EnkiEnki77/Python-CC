# Numbers in python are used to keep track of scores in games, represent data in visualizations, store info in web apps, etc.

# You can add, subtract, divide, and multpily integers in python

# Python uses two multiplication symbols to represent exponents. 
print(3 ** 2)
print(3 ** 3)

# Python also uses the order of operations, so you can chain multiple operations into one statement
print(6 + 4 * 2)
# You can also use parens to determine the order of operations
print ((6 + 4) * 2)

# Any number with a decimal point is called a float
5.14
7.24

# When you divide any two numbers, even if they would result in a whole number the result is always a float.
print(4/2)

# If you mix an integer and float in any other operatin youll also get a float
print(2 + 2.00)
print(2 * 1.0)
print(3 ** 3.0)


# To make larger numbers more readable use underscores instead of commas.
large_number = 100_000_000
print(large_number)
# Python prints only the integers

# You can assign values to more than one variable in a single line of code. This is most useful when assigning variables.
# That should be grouped together logically
x, y, z = 0, 1, 2

# Python does not have constant types, but the convention is for variables written in all caps to be treated as constant.
MAX_CONNECTIONS = 4

