# In OOP you create classes that represent real world things and situations. and you create objects based on these classes
# When you design a class you define the general behaviours a whole category of objects can have.

# When you create objects from a class each object automatically has the behaviour of that class, and then you are
# free to give the object unique characteristics. 

# Making an object from a class is called instantiation and you work with instances of a class. 

# By convention classes are capitalized and we use a docstring to explain what the class is modeling
class Dog:
    """A simple dog model"""

    # A function thats a part of a class is a method. Every class has a __init__ method that is called when a new 
    # instance of the class is instantiated. 
    # The self parameter is required first in the __init__ method because when a new instance is created the self argument
    # is automatically passed in. We can also add additional parameters to hold arguments passed in unique for each instance
    # to make these unique arguments accessible throughout the other methods and properties of the class we assign them as
    # properties of self. 
    def __init__(self, name, age) -> None: 
        """Initialize name and age attributes"""
        self.name = name
        self.age = age

    # To give methods access to the attributes declared in __init__ you have to pass them self as an argument
    def sit(self):
        """Simulate dog sitting in response to a command"""
        print(f"{self.name} is now sitting")

    def roll_over(self):
        """Simulate dog rolling over in response to a command"""
        print(f"{self.name} rolled over")

my_dog = Dog("Tank", 4)

print(f"My dog's name is {my_dog.name}")
print(f"My dog's age is {my_dog.age}")
my_dog.sit()