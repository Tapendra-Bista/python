#Section 9.3: Exponentiation
a, b = 2, 3
(a ** b)               # = 8
pow(a, b)              # = 8
import math
math.pow(a, b)         # = 8.0 (always float; does not allow complex results)
import operator
operator.pow(a, b)     # = 8
#Another difference between the built-in pow and math.pow is that the built-in pow can accept three arguments:
a, b, c = 2, 3, 2
pow(2, 3, 2)           # 0, calculates (2 ** 3) % 2, but as per Python docs,
                       #    does so more efficiently
#Special functions
#The function math.sqrt(x) calculates the square root of x.
import math
import cmath
c = 4
math.sqrt(c)           # = 2.0 (always float; does not allow complex results)
cmath.sqrt(c)          # = (2+0j) (always complex)
#To compute other roots, such as a cube root, raise the number to the reciprocal of the degree of the root. This
#could be done with any of the exponential functions or operator.
#GoalKicker.com – Python® Notes for Professionals 60
import math
x = 8
math.pow(x, 1/3) # evaluates to 2.0
x**(1/3) # evaluates to 2.0
# The function math.exp(x) computes e ** x.
math.exp(0)  # 1.0
math.exp(1)  # 2.718281828459045 (e)
# The function math.expm1(x) computes e ** x - 1. When x is small, this gives significantly better precision than
math.exp(x) - 1.
math.expm1(0)       # 0.0
math.exp(1e-6) - 1  # 1.0000004999621837e-06
math.expm1(1e-6)    # 1.0000005000001665e-06
# exact result      # 1.000000500000166666708333341666...
# Section 9.4: Trigonometric Functions
a, b = 1, 2
import math
math.sin(a)  # returns the sine of 'a' in radians
# Out: 0.8414709848078965
math.cosh(b)  # returns the inverse hyperbolic cosine of 'b' in radians
# Out: 3.7621956910836314
math.atan(math.pi)  # returns the arc tangent of 'pi' in radians
# Out: 1.2626272556789115
math.hypot(a, b) # returns the Euclidean norm, same as math.sqrt(a*a + b*b)
# Out: 2.23606797749979
# Note that math.hypot(x, y) is also the length of the vector (or Euclidean distance) from the origin (0, 0)
# to the point (x, y).
# To compute the Euclidean distance between two points (x1, y1) & (x2, y2) you can use math.hypot as
# follows
# math.hypot(x2-x1, y2-y1)
# To convert from radians -> degrees and degrees -> radians respectively use math.degrees and math.radians
math.degrees(a)
# Out: 57.29577951308232
math.radians(57.29577951308232)
# Out: 1.0
# GoalKicker.com – Python® Notes for Professionals 61
# Section 9.5: Inplace Operations
# It is common within applications to need to have code like this:
a = a + 1
# or
a = a * 2
# There is an effective shortcut for these in place operations:
# a += 1
# and
a *= 2
# Any mathematic operator can be used before the '=' character to make an inplace operation:
# -= decrement the variable in place
# += increment the variable in place
# *= multiply the variable in place
# /= divide the variable in place
# //= floor divide the variable in place # Python 3
# %= return the modulus of the variable in place
# **= raise to a power in place
# Other in place operators exist for the bitwise operators (^, | etc)
# Section 9.6: Subtraction
a, b = 1, 2
# Using the "-" operator:
b - a                  # = 1
import operator        # contains 2 argument arithmetic functions
operator.sub(b, a)     # = 1
# Possible combinations (builtin types):
# int and int (gives an int)
# int and float (gives a float)
# int and complex (gives a complex)
# float and float (gives a float)
# float and complex (gives a complex)
# complex and complex (gives a complex)
# Section 9.7: Multiplication
a, b = 2, 3
a * b                  # = 6
import operator
# GoalKicker.com – Python® Notes for Professionals 62
operator.mul(a, b)     # = 6
# Possible combinations (builtin types):
# int and int (gives an int)
# int and float (gives a float)
# int and complex (gives a complex)
# float and float (gives a float)
# float and complex (gives a complex)
# complex and complex (gives a complex)
# Note: The * operator is also used for repeated concatenation of strings, lists, and tuples:
3 * 'ab'  # = 'ababab'
3 * ('a', 'b')  # = ('a', 'b', 'a', 'b', 'a', 'b')
# Section 9.8: Logarithms
# By default, the math.log function calculates the logarithm of a number, base e. You can optionally specify a base as
# the second argument.
import math
import cmath
math.log(5)         # = 1.6094379124341003
# optional base argument. Default is math.e
math.log(5, math.e) # = 1.6094379124341003
cmath.log(5)        # = (1.6094379124341003+0j)
math.log(1000, 10)   # 3.0 (always returns float)
cmath.log(1000, 10)  # (3+0j)
# Special variations of the math.log function exist for different bases.
# Logarithm base e - 1 (higher precision for low values)
math.log1p(5)       # = 1.791759469228055
# Logarithm base 2
math.log2(8)        # = 3.0
# Logarithm base 10
math.log10(100)     # = 2.0
cmath.log10(100)    # = (2+0j)
# Section 9.9: Modulus
# Like in many other languages, Python uses the % operator for calculating modulus.
3 % 4     # 3
10 % 2    # 0
6 % 4     # 2
# Or by using the operator module:
import operator
operator.mod(3 , 4)     # 3
