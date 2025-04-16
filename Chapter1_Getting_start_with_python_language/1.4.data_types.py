# Built-in Types
#Booleans
#boolean value be either true or false
# logical operaton like and ,or,not can be performed on booleans.
# a boolean is also an int
# 1 for true and 0 for false
# case of it is when we use boolean in arithmetric operation
a = False
b = True
c= 1
d=0

if (a==True):
    print("a is true as True")
elif (b==False  ): 
     print("b is false as False")
elif (c==True):
 print("c is true as 1")
elif(d== False):
   print("d is False as 0")      

print(type(a),type(b),type(c),type(d))
# Numbers
# int: integer number
# int in python are of arbitrary sizes.
k= 10
phone = 9804633911
age =9999999999999999
print("k:",k," phone:",phone," age:",age)
# Float
# float:Floating point number
m= 9.99
s = 29.e0
f = 49.e2
print(m,s,f)
# complex:Complex numbers
a = 2 + 1j
b = 100 + 10j
# The <, <=, > and >= operators  will raise a TypeError exception when any operand is a complex number

# String 
string1  = "StringONE"
string2 = 'STRING2'
print(string1,string2)
# unicode string
unicode_string = "This is a unicode_string , normal string known as unicode_string"
print(unicode_string)
# bytes string
bytes_string = b"This is a bytes_string"
print(bytes_string)
# Sequences and collection
# list: An ordered collection of n values (n>=0)
 
m = [1,2,3]
pp = ['string',m,(1,2),[9,8,7,6,5,4,3,2,1]]
print(pp)
pp[2] = 'new string'
# Not hashable; mutable
print(m)
print(pp)
print(pp[2])
print(pp)

"""An object is hashable if it has a hash value that remains constant during its lifetime. This hash value is an integer that is used to quickly compare dictionary keys
 during a dictionary lookup.
Examples of Hashable Types:
Integers (int)
Floats (float)
Strings (str)
Tuples (tuple) (if all elements within the tuple are also hashable)
Frozen sets (frozenset)
"""

"""
An object is not hashable if it does not meet the requirements for being hashable (as described above).
Examples of Not Hashable Types:
Lists (list)
Dictionaries (dict)
Sets (set)
"""

# set : unorder collection of unique values. items must be hashable
myset = {1,2,'tapendra'}
# inside this  another list ,dictionaries and set allowed
# dic:an unorder colllection of unique key value pairs. items must be hashable value
# this like a mapping key value pairs left side is key and right side is value
# example : for person details
my_dict = {
   'name' : "Tapendra bista",
   'address' : "Kathmandu",
 'age' : 19,
 'phone' : 9804633911

}
print(my_dict)
none_Variable = None # No value will be assigned. Any valid datatype can be assigned later
# None is always less than number
if none_Variable is None:
   print("True ")
else : 
   print("Not")

print(type(none_Variable),isinstance(my_dict,set))

# type() and isinstance()
# type() is used to find  dataType
# isInstance() is used to compare whether it is which type 
# it take to 2 arguments object and class_or_tuple

# Converting between datatypes
string_a = '123'
int_a = int(string_a)
float_a = float(string_a)
print(string_a,int_a,float_a)

# Mutable and immutable types
#An object is called mutable if it can be 
# changed. For example, when you pass a 
# list to some function, the list can be changed.
# example
my_list = [1,2,3,4]
def display(m):
   m.append(5)
   print("List :",m)

display(my_list)
#An object is called immutable if it cannot be
#  changed in any way. For example, integers are
#  immutable, since there's
#no way to change them
# Variables are themselves are mutable

"""
Examples of immutable Data Types:
int, long, float, complex
str
bytes
tuple
frozenset

Examples of mutable Data Types:
bytearray
list
set
dict
"""
# You can also convert sequence or collection types
# Example 
converting_String = "Tapednra"
print(list(converting_String),set(converting_String),tuple(converting_String))

"""
Tuples:

Definition: Tuples are ordered, immutable sequences of elements.
Syntax: Created using parentheses ().
Ordering: Elements have a specific order, and the order is preserved.
Mutability: Tuples are immutable, meaning you cannot change their elements after creation.
Duplicates: Tuples can contain duplicate elements.
Hashable: Tuples are hashable (if all their elements are hashable), so they can be used as dictionary keys or elements in sets.


Sets:

Definition: Sets are unordered collections of unique elements.
Syntax: Created using curly braces {} or the set() constructor.
Ordering: Sets are unordered, meaning the elements don't have a specific order.
Mutability: Sets are mutable, meaning you can add or remove elements after creation.
Duplicates: Sets cannot contain duplicate elements. If you try to add a duplicate, it will be ignored.
Hashable: Sets themselves are not hashable (because they are mutable), but their elements must be hashable.


Tuple:
When you need an ordered sequence of elements that should not be changed.
When you need to use a collection as a key in a dictionary (since keys must be hashable).
For representing fixed collections of items, like coordinates (x, y).
Set:
When you need to store a collection of unique elements, and the order doesn't matter.
When you need to perform set operations like union, intersection, difference, etc.
For efficiently checking if an element is present in a collection.
"""