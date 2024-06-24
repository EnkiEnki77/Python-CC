from pathlib import Path

cats_file = Path('cats.txt')
dogs_file = Path('dogs.txt')

try:
    cat_content = cats_file.read_text()
    
except FileNotFoundError:
    pass
else:
    print(cat_content)
    

try:
    
    dog_content = dogs_file.read_text()
except FileNotFoundError:
    pass
else:
   
    print(dog_content)