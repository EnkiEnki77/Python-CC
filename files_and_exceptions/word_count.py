from pathlib import Path

def word_count(path):
    """Count the approximate number of words in a file"""

    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError: 
        print(f"The file {path} does not exist in the current directory.")
    else:
        words = contents.split()
        number_of_words = len(words)

        print(f"The file {path} has approximately {number_of_words} words")

filenames = ['alice.txt', 'sidhartha.txt', 'moby_dick.txt']

for filename in filenames:
    path = Path(filename)
    word_count(path)

# In some instances you may not want to do anything with an error when it happens in this case just use pass in the 
# except block. This allows things to fail silently. You only wanna give users error information about things they were
# looking for. Otherwise fail silently. 
# Well tested code should not be prone to eternal errors, but anytime you rely on something external such as user input,
# the existence of a file, or a network connection they can happen and you should use exception blocks to handle these
# possibilities.   