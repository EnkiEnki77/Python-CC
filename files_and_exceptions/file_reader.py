from pathlib import Path

path = Path('Python Crash Course/files_and_exceptions/pi_digits.txt')
# Make sure youre in the right directory in the terminal
content = path.read_text()
content = content.rstrip()

# splitlines allows you to split a files lines into individual pieces, so you can more easily parse them and format them
# however you need to. 
lines = content.splitlines()
for line in lines:
    print(line)