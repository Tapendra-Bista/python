from operator import add
a,b = 1,2
# using the  "+" operator
print(a+b)
a +=  b
print(a)
print(add(a,b))

"""a, b = 1, 2
# Using the "+" operator:
a + b                  # = 3
GoalKicker.com – Python® Notes for Professionals 59
# Using the "in-place" "+=" operator to add and assign:
a += b                 # a = 3 (equivalent to a = a + b)
import operator        # contains 2 argument arithmetic functions for the examples
operator.add(a, b)     # = 5  since a is set to 3 right before this line
# The "+=" operator is equivalent to:
a = operator.iadd(a, b)    # a = 5 since a is set to 3 right before this line
Possible combinations (builtin types):
int and int (gives an int)
int and float (gives a float)
int and complex (gives a complex)
float and float (gives a float)
float and complex (gives a complex)
complex and complex (gives a complex)
Note: the + operator is also used for concatenating strings, lists and tuples:
"first string " + "second string"    # = 'first string second string'
[1, 2, 3] + [4, 5, 6] """