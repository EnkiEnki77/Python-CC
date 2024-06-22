# If youd like to use a for loop to create a new list based on operations on the items of a range or different list use
# a list comprehension
cubes = [value ** 3 for value in range(1, 11)]

# If youd like to print all the items of a list print the list with the * prefixed to it. add the argument sep="\n" to print
# each on its own line
print(*cubes, sep="\n")

