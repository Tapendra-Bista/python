class ExampleClass:
    def __init__(self):
        self.name = 'example'  # Use self.name to assign to the object
    def someFunction(self, a):
        if a > 5:
            return True  # Indent the return statement
        else:
            return False  # Indent the return statement

e = ExampleClass()  # Correct way to create an instance
result = e.someFunction(3)  # Call the function and store the result
print(result)  # Print the result

"""Indentation in Python is the whitespace at the beginning of a line of code. Unlike many other programming languages that use braces or keywords to define code blocks, Python uses indentation to define the structure and scope of code blocks (e.g., within functions, loops, conditional statements, and classes)."""
"""Here's why indentation is crucial in Python:

Defines Code Blocks: Indentation is how Python groups statements together. Lines with the same indentation level are considered part of the same block.
Enforces Readability: Consistent indentation makes Python code highly readable and forces programmers to structure their code in a clear and organized way.
Syntax Requirement: Indentation is not just a style choice; it's a syntax requirement. Incorrect indentation will lead to syntax errors."""
"""def my_function(x):
    if x > 5:
        print("x is greater than 5")  # Part of the 'if' block
        return True                   # Still part of the 'if' block
    else:
        print("x is not greater than 5") # Part of the 'else' block
        return False                    # Still part of the 'else' block

print("This is outside the function")  # Not part of the function"""

def checkAvaibility(myList):
    for index, i in enumerate(myList):
        if i == 1:
            print("value of i:", i, "at index:", index)
            return True
    return False

myList = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
result = checkAvaibility(myList)
print(result)