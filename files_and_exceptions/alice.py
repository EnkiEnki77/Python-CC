from pathlib import Path

path = Path('files_and_exceptions/alice.txt')

try:
    # When trying to read from a file that wasnt created on your system you likely need to pass in an argument telling
    # the Path what encoding to use. Your systems default encoding likely doesnt match.
    contents =path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"The file {path} does not exist in the current directory.")
else:
    # Count the approximate amount of words in the file.
    # by default split splits words into a list at whitespaces.
    words = contents.split()
    number_of_words = len(words)

    print(f"The book Alice's Adventure's in Wonderland has approximately {number_of_words} words")