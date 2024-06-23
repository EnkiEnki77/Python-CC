# The for loop takes a collection of items and executes a block of code for each item. The while loop however continues
# executing the block of coding while a condition remains true.

# current_num = 1

# while current_num <= 5:
#     print(current_num)
#     current_num += 1

# While loops allow a user to choose when a program ends based on state. The program can be set up to run perpetually until
# a condition is met such as hitting the quit button. 
# prompt = "Tell me something, and ill repeat it: "
# prompt += "\nEnter 'quit' to end the program."

# message = ''
# while message != 'quit':
#     message = input(prompt)
#     print(f"{message}\n")

# The above ends the program on a single condition. But what if there are multiple situations youd want the program to end
# from? In this case use a flag such as active = True, and then put active=False behind whatever conditionals you want to
# end the program

# active = True
# while active:
#     message = input(prompt)

#     if message == 'quit':
#         active = False
#     else:
#         print(message)

# You can use continue to restart a loop from the beginning. For example we can have a conditional that checks if the 
# current value of a variable is even or not and skip over the rest of the code if it is so the code only runs if the 
# variable is an odd number. 
current_num = 0
while current_num < 10:
    current_num += 1

    if current_num % 2 == 0:
        continue

    print(current_num)

# Make sure to always test that your loops have a way to break so theyre not infinite.
