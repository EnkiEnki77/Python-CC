from pathlib import Path
import json 

path = Path('username.json')
contents = path.read_text()
# Converts data back to the actual type it was.
username = json.loads(contents)

print(f"Welcome back {contents}")