"""There are two functions that can be used to obtain a readable representation of an object.
repr(x) calls x.__repr__(): a representation of x. eval will usually convert the result of this function back to the
original object.
str(x) calls x.__str__(): a human-readable string that describes the object. This may elide some technical detail"""
import datetime
normal_string = "Tapendra bista"
print(str(normal_string))
print(repr(normal_string))
s = """w'o"w"""
print(str(s))
print(repr(s))

today = datetime.datetime.now()
print(str(today))
print(repr(today))

# str show human readable form
# repr show  original object