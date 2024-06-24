from pathlib import Path

filenames = ['alice.txt', 'romeo.txt', 'moby.txt']

# Grab the file
path = Path('alice.txt')

# Grab the text from the file and save it in this variable. This file was not written on this machine so we need to change
# the encoding to utf-8
text = path.read_text(encoding='utf-8')

# The count string method returns the number of times the given argument occurs in the string. Format it to all lower first
# so that formatting doesnt effect the result.
the_count = text.lower().count('the')

print(the_count)