from pathlib import Path
import json

path = Path('numbers.json')

# loads the data into the program as a string
result = path.read_text()
# loads the data into memory of the new program as the data structure it originally was. This allows you to share data between
# programs.
numbers = json.loads(result)
print(type(result))