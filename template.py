# Importing necessary modules from typing
from typing import Optional, Union

# Example of a simple function with type hints for parameters and return type
def add(x: int, y: int) -> int:
    """Add two integers and return the result."""
    return x + y

# Example of a function with different types of parameters
def process_data(data: list, flag: bool) -> str:
    """
    Process data based on the flag.
    
    Args:
        data (list): The data to be processed.
        flag (bool): A flag to control the processing.
        
    Returns:
        str: The result of processing.
    """
    if flag:
        return f"Processed: {data}"
    else:
        return "Processing skipped"

# Example of a function with an optional parameter
def get_user_name(user_id: int, default_name: Optional[str] = None) -> str:
    """
    Get the user name by user_id. Return default_name if user_id is not found.
    
    Args:
        user_id (int): The user ID.
        default_name (Optional[str]): The default name to return if user_id is not found.
        
    Returns:
        str: The user name or default name.
    """
    if user_id == 123:
        return "Alice"
    else:
        return default_name if default_name is not None else "Guest"

# Example of a function with a parameter that can be multiple types
def parse_input(data: Union[str, bytes]) -> str:
    """
    Parse input data which can be either str or bytes.
    
    Args:
        data (Union[str, bytes]): The input data.
        
    Returns:
        str: The parsed string.
    """
    if isinstance(data, bytes):
        return data.decode('utf-8')
    return data

# Example of a class with type hints for instance variables and methods
class Dog:
    def __init__(self, name: str, age: int):
        """Initialize a new Dog instance."""
        self.name: str = name  # The dog's name
        self.age: int = age    # The dog's age
    
    def bark(self) -> None:
        """Make the dog bark."""
        print(f"{self.name} says woof!")
    
    def get_age(self) -> int:
        """Get the dog's age."""
        return self.age

# Example of a static method
class MyClass:
    @staticmethod
    def my_static_method() -> None:
        """Static method that does not access the class or instance."""
        print("This is a static method.")

# Example of a class method
class MyClassWithClassMethod:
    class_variable: str = "class variable"

    @classmethod
    def my_class_method(cls) -> None:
        """Class method that accesses class variables."""
        print(f"This is a class method accessing {cls.class_variable}")
