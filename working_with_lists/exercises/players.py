# slicing a list allows you to work with certain groups of items within it.
numbers = list(range(1, 11))

# A slice takes two number, the index to start the slice, and the index to end it.
print(numbers[1:4])

# You can omit the starting index and the slice will begin from the first index
print(numbers[:4])

# You can omit the ending index and the slice will go to the end of the list
print(numbers[3:])

# Say we want just the last three items of a list use a negative number as the start index, and nothing for ending
print(numbers[-3:])

# If you want to copy the whole list dont give a start or end index
print(numbers[:])

# You can set a step size for a slice as well
print(numbers[1::2])


# You can use slices in a for loop or any other iterator
# The asterisk used on a list like this is called the unpack operator. 
print(*numbers[3:], sep="\n")

for num in numbers[3:]:
    print(f"These are my numbers: {num}")


# If youd like to make a new list that contains the same items as a preexisting list but that you may want to add different
# items to later you should make a copy using a slice. 
my_foods = ["pizza", "ice cream", "burritos"]
print(f"MY foods {my_foods}")
friends_foods = my_foods[:]
print(f"MY friends foods {friends_foods}")

# now we can change the two lists independently from eachother
my_foods.append("pad thai")
friends_foods.append("bologna")
print(f"MY foods edited {my_foods}")
print(f"MY friends foods edited {friends_foods}")

# Whereas if we dont create a copy with a slice and just try to assign the original list to a new variable the list is 
# now just associated with both variables, and editing either variable will alter the list for both.
friends_foods = my_foods
print(my_foods)
print(friends_foods)
friends_foods.pop()
print(my_foods)
print(friends_foods)