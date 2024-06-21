# We can use f strings to dynamically add data to strings with variables

f_name = "enki"
l_name = "layman"

full_name = f"{f_name} {l_name}"
print(full_name)

# You can use f strings to display full messages using the data in variables
message = f"Hello there, {full_name.title()}"
print(message)

# We can add whitespace to text with the following characters: \t for indents, \n to put it on a new line
print("\tPython")
print("Langusges:\nPython\nC\nJavascript")

# Whitespace added to the ends of strings from users can mess up comparison checking in the code. To format a string to
# have whitespace on the right stripped off use rstrip()
print("Python ".rstrip())

# You also have lstrip to strip it from the left, or just strip to strip it from both sides.

# These stripping functions are used most often to clean up user input before storing it in the program. 

# Another common thing to do with strings is to remove prefixes, such as https:// from a url, so we can focus just on the 
# domain users need to type in. 

nostarch_url = "https://nostarch.com"
print(nostarch_url.removeprefix("https://"))