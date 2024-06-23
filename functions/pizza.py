# We can accept an arbitrary amount of arguments using the unpack operator.
# It packs all arguments into a tuple under a single parameter name

def make_pizza(*toppings):
    # functions should always have a comment at the top describing what they do. programmers should be able to use a
    # function just off this docstring
    """adds topping to pizza"""
    # When used in the print function the tuple is unpacked into a string. 
    print(*toppings)

# make_pizza('pepperoni', 'mushrooms')