# The range function is great for creating a list of numbers in Python

# It takes two arguments, the number to start at, and the number to stop at. 
for num in range(1, 6):
    print(num)

# You can also pass range only one number, and it will start at 0
for num in range(6):
    print(num)

# If you want to create a list of numbers you can do so without a loop, instead you can wrap a call to range with a call
# to list. Range outputs the numbers, and list converts them to a list.
numbers = list(range(1, 11))
print(f"\n{numbers}")