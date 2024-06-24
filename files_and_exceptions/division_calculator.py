# Python uses special objects called exceptions to handle errors while a program is running. 
# Whenever python runs into an error and doesnt know what to do next by default it just ends the program and shows traceback.
# But before that it returns an exception object and if you write code to handle that exception the program will 
# continue running. 
# Exceptions are handled with try-except blocks. try-except blocks ask python to do something but also handle errors.
# If python runs into an error. Instead of shutting down the program and giving a traceback. it keeps running and an 
# error message you write is output to the user. 

# Lets say we try to divide by zero
# print(5/0)

# we get a ZeroDivisionError exception object. Python creates exception objects in situations it cant do what we asked it to.
# It stops and tells what kind of exception was raised. We can then use this info to modify our program. We can tell python
# what to do when this exception occurs. 

# If you think an error might occur use a try-except block. Put the code you want to try in the try block and code for
# any exceptions in the except block
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

# If more code happens after a try except block the program continues running because we told python how to handle the
# error.

# Handling error correctly is especially important when more work is to occur after the error such as when taking in user
# input
# If a program responds to invalid input appropriately it can request more valid input instead of crashing. 

print("Enter two numbers and ill divide them.")
print("Press 'q' to quit.")

while True:
    first_number = input("\nFirst Number: ")
    if first_number == 'q':
        break
    second_number = input("Second Number: ")
    if second_number == 'q':
        break
    
    answer = None
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You cant divide by zero, please try again")
    # Any code that relies on the try block executing successfully with no exception goes in the else block.
    else:
        print(answer)


    # Any code that you think may cause an exception to occur should be placed in a try block
    # An exception block should then be used to tell Python what to do whenever it runs into a certain exception
    # Any code that relies on the code in the try block executing successfully should go in an else block

    # This makes your code protected against crashes due to errors and malicious attacks. 

    