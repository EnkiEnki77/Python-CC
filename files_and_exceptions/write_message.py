# One of the simplest ways to save data is to write it to a file. The output will still be available after you close the 
# terminal containing your programs output. 
# You can examine output after a program finishes running, and you can share it with others as well.You can also create 
# programs that read the data back into memory and work with it later as well. 

# once you have a path defined you can write to the file using write_text()

from pathlib import Path
path = Path('files_and_exceptions/learning_python.txt')
result = path.read_text()
result += '\nI lovvve programming!'
# Python can only write string data, if you want to write numerical data yoou must first convert it to a string.
# write_text does a few things, if a file its writing to does not exist it creates the file. it also properly closes it
# to avoid corruption of the data.  
# Be careful writing to files that already exist. write_text will delete any data already in the file.  
path.write_text(result)

result = path.read_text()

print(result)