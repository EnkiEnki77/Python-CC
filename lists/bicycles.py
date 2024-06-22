# Lists are indicated by [] and contain whatever kind of data youd like them to but generally that data will be related.
# You should generally use a name in plural that describes what the list contains.

bicycles = ['trek', 'cannondale', 'redline', 'specialized']

# If you dont know the length of a list and want to access items starting from the end of it use negative numbers. -1 will
# give you the last item, -2 the second to last, and so on.

print(bicycles[-1].title())

# In python append() is the same thing as push() in js
bicycles.append('ducati')
print(bicycles)

# This allows you to add data to your list dynamically after the program starts such as from user input

# You can also insert data at any index of a list using the inser() method. this shifts the data currently at that index
# as well as the ones after one space to the right
bicycles.insert(2, 'bananna')
print(bicycles)



# If you know the index of an item you want to remove from a list you can use the del statement.
del bicycles[2]
print(bicycles)

# Sometimes you want to access a value after you remove it from a list, such as to take user from an active list of users
# and place it in an inactive list of users. Or to draw an explosion at the x,y position of an alien just shot down. Do 
# this with th pop mehtod. 
popped_bicycle = bicycles.pop()
print(bicycles)
print(popped_bicycle)

# An example of when we might want to pop a value from a list is say we have a list of bikes in order of when we owned them
# we could then pop the last bike in the list and create a message about it
last_bike_owned = bicycles.pop()
print(f"The last bike I owned was a {last_bike_owned.title()}")


# If you want to remove an item from a list and not use it in any way use del, if you will use the removed item as you remove
# it use pop()

# Sometimes you dont know the index of the item you want to remove, just the value. In this case use the remove method.
bicycles.remove('trek')
print(bicycles)

# You might want to make a message about the removed item, so save the input you use as input to remove as a variable
too_expensive = 'redline'
bicycles.remove(too_expensive)
print(f"A {too_expensive} is too expensive")
print(bicycles)
# print(f"A {too_expensive.title()} is too expensive for me.")

# Remove only removes the first occurence of an item, if you want to remove every occurence use a loop. 