# lists are great for storing collections of items that change throughout the life of your program, but if you have a list
# of items that cannot change this is now called a tuple. An immutable list. 

# A tuple looks just like a list except you use parens instead of square brackets.
dimensions = (200, 10)
print(*dimensions, sep="\n")

# If you want to define a tuple with one element you need to give it a trailing comma
(3,)

