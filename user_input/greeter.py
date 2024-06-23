# You should always give a user a prompt that tells them exactly what kind of info youre looking for from them.
# name = input("Please enter your name: ")
# print(f"Hello {name}")

# Write your prompt as a variable, and if it will be multiple lines, concatenate. this makes things clean and readable

prompt = "If you share your name, we can personalize the messages you see"
prompt += "\nPlease enter your name: "

name = input(prompt)
print(f"Hello, {name}!")