import operator
from operator import truediv
# division operation
a,b,c,d = 3,4,5,-1
# using / operator
print(a/b)
print(c/d)

# using  module
# Operator.div() removed in python version 3

print(truediv(a,b))

"""Python does integer division when both operands are integers. The behavior of Python's division operators have
changed from Python 2.x and 3.x (see also Integer Division ).
a, b, c, d, e = 3, 2, 2.0, -3, 10
Python 2.x Version ≤ 2.7
In Python 2 the result of the ' / ' operator depends on the type of the numerator and denominator.
a / b                  # = 1
a / c                  # = 1.5
d / b                  # = -2
b / a                  # = 0
d / e                  # = -1
Note that because both a and b are ints, the result is an int.
The result is always rounded down (floored).
Because c is a float, the result of a / c is a float.
You can also use the operator module:
import operator        # the operator module provides 2-argument arithmetic functions
operator.div(a, b)     # = 1
operator.__div__(a, b) # = 1
Python 2.x Version ≥ 2.2
What if you want float division:
Recommended:
GoalKicker.com – Python® Notes for Professionals 58
from __future__ import division # applies Python 3 style division to the entire module
a / b                  # = 1.5
a // b                 # = 1
Okay (if you don't want to apply to the whole module):
a / (b * 1.0)          # = 1.5
1.0 * a / b            # = 1.5
a / b * 1.0            # = 1.0    (careful with order of operations)
from operator import truediv
truediv(a, b)          # = 1.5
Not recommended (may raise TypeError, eg if argument is complex):
float(a) / b           # = 1.5
a / float(b)           # = 1.5
Python 2.x Version ≥ 2.2
The ' // ' operator in Python 2 forces floored division regardless of type.
a // b                # = 1
a // c                # = 1.0
Python 3.x Version ≥ 3.0
In Python 3 the / operator performs 'true' division regardless of types. The // operator performs floor division and
maintains type.
a / b                  # = 1.5
e / b                  # = 5.0
a // b                 # = 1
a // c                 # = 1.0
import operator            # the operator module provides 2-argument arithmetic functions
operator.truediv(a, b)     # = 1.5
operator.floordiv(a, b)    # = 1
operator.floordiv(a, c)    # = 1.0
Possible combinations (builtin types):
int and int (gives an int in Python 2 and a float in Python 3)
int and float (gives a float)
int and complex (gives a complex)
float and float (gives a float)
float and complex (gives a complex)
complex and complex (gives a complex)"""