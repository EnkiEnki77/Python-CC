from pathlib import Path

path = Path('files_and_exceptions/learning_python.txt')
result = path.read_text()
# You can replace words/chars in a file with other words/chars
result = result.replace('Python', 'Go')

# Split lines puts each line of the file into a list you can loop through 
lines = result.splitlines()
print(lines)

# print(result)