cars = ['subaru', 'bmw', 'audi', 'toyota']

# You can also temporarily sort things using the sorted function
print(f"Original list: {cars}")
print(f"Sorted list: {sorted(cars)}")
print(f"Original list again: {cars}")
print(f"Sorted list again, but in reverse: {sorted(cars, reverse=True)}")

# We can sort a list alphabetically using the sort method. This operation is permanent
cars.sort()
print(cars)

# You can also do it in reverse order
cars.sort(reverse=True)
print(cars)

# Sorting lists complicates if strings have capitals, so one solution is to lowercase everything before sorting.
