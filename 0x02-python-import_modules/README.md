To import functions from another file:

Use the import statement followed by the name of the file (module) containing the functions you want to import.
Syntax: import module_name
To use imported functions:

After importing the module, you can access its functions using the dot notation.
Syntax: module_name.function_name()
To create a module:

Create a new Python file with a .py extension and define your functions or variables inside it.
Other files can then import this module and use its contents.
To use the built-in function dir():

The dir() function returns a list of names in the current local scope or the names of an object's attributes.
Syntax: dir([object])
Example: dir() or dir(module_name)
To prevent code in your script from being executed when imported:

Use the if __name__ == '__main__': condition to check if the script is being run directly or imported as a module.
Place the code that should only run when the script is executed directly under this condition.
Syntax:
python
Copy
if __name__ == '__main__':
    # Code to be executed when the script is run directly
To use command line arguments with your Python programs:

Access the command line arguments using the sys.argv list from the sys module.
sys.argv[0] contains the name of the Python script, and sys.argv[1:] contains the additional arguments.
Syntax:
python
Copy
import sys

# Accessing command line arguments
argument1 = sys.argv[1]
argument2 = sys.argv[2]
