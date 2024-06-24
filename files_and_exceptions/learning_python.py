from pathlib import Path

path = Path('files_and_exceptions/learning_python.txt')
result = path.read_text()

for num in range(2):
    print(result)