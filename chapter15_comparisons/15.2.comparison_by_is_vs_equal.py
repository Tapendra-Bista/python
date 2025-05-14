"""
A common pitfall is confusing the equality comparison operators is and ==.
a == b compares the value of a and b.
a is b will compare the identities of a and b"""

a = ' this is a string ! A common pitfall is confusing the equality comparison operators is and ==.'
b = ' this is a string ! A common pitfall is confusing the equality comparison operators is and ==.'

print(a==b)
print(a is b)

a = 'Python is fun!'
b = 'Python is fun!'
print(a is b)

"""Beyond this, there are quirks of the run-time environment that further complicate things. Short strings and small
integers will return True when compared with is, due to the Python machine attempting to use less memory for
identical objects"""
print(id(a) is id (b))


