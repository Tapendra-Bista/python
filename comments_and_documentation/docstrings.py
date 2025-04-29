"""
DocStrings are -unlike regular comments -stored as an attributes of the function they docments  , meaning that you can access them programmatically."""

# Example 
def greating():
    """This is a docStrings and can be access as a programma using __doc__"""
    return   # space before return is consider as intentardation in python which help to manage to be part of function , loop and etc like return is a part of function greatting

print(greating.__doc__) # it will print above comment
print(help(greating))
