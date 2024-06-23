from pathlib import Path

path = Path('files_and_exceptions/pi_digits.txt')

content = path.read_text()
content = content.rstrip()

lines = content.splitlines()

pi_string = ''
for line in lines:
    pi_string += line.lstrip()

print(len(pi_string))
# When python reads from a file it interprets it as a string. If you want to work with the data as a number youll have to 
# wrap it in a float or int functions.
print(float(pi_string))