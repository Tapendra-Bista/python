# Math Module 

# 1 : Rounding: round, floor, ceil, trunc
# In addition to the built-in round function, the math module provides the 
# floor, ceil, and trunc functions.

import math
import sys

x = 1.55
y = -1.55

# round to the nearest integer 
print(round(x))  # Output: 2
print(round(y))  # Output: -2

# get the largest integer less than x
print(math.floor(x))  # Output: 1
print(math.floor(y)) # Output: -2

# get the smallest integer greater than x
print(math.ceil(x))  # Output: 2
print(math.ceil(y)) # Output: -1


# truncate  the decimal part 
# equivalent to math.floor for positive numbers
# equivalent to math.ceil for negative numbers 

print(math.trunc(x))  # Output: 1
print(math.trunc(y)) # Output: -1


#  floor, ceil, round and trunc always return a float value

# 2 : Trigonometry
# Calculating the length of the hypotenuse of a right trianhle

print(math.hypot(3,4))  # Output: 5.0  

# converting degrees to radians and vice versa
print(math.radians(90))  # Output: 1.5707963267948966
print(math.degrees(math.pi/2)) # Output: 90.0

# Sine, Cosine, Tangent
print(math.sin(math.pi/2)) # Output: 1.0
print(math.cos(0)) # Output: 1.0
print(math.tan(math.pi/4)) # Output: 0.9999999999999999
print(math.asin(1)) # Output: 1.5707963267948966
print(math.acos(1)) # Output: 0.0
print(math.atan(1)) # Output: 0.7853981633974483
print(math.atan2(1,1)) # Output: 0.7853981633974483
print(math.sinh(0)) # Output: 0.0
print(math.cosh(0)) # Output: 1.0
print(math.tanh(0)) # Output: 0.0
print(math.asinh(0)) # Output: 0.0
print(math.acosh(1)) # Output: 0.0
print(math.atanh(0)) # Output: 0.0
print(math.copysign(1, -5)) # Output: -1.0


# 3 : Pow for faster  exponentiation
print(math.pow(2,3)) # Output: 8.0
print(math.pow(9,9)) # Output: 387420489.0
print(math.pow(4,4)) # Output: 256.0

# 4 : Infinity and NaN (Not a Number)
# In all versions of pyhton, we can represent infinity and NaN as follows:

pos_inf = float('inf')
neg_inf = float('-inf')
not_a_number = float('nan')

print(pos_inf)  # Output: inf
print(neg_inf)  # Output: -inf
print(not_a_number)  # Output: nan

# we can alos use the math module to represent infinity and NaN
pos_inf1 = math.inf
neg_inf1 = -math.inf
not_a_number1 = math.nan


# We can c test for positive or negative  infinity using the math.isinf method

print(math.isinf(pos_inf))  # Output: True
print(math.isinf(neg_inf))  # Output: True
print(math.isinf(10))  # Output: False
print(math.isnan(not_a_number))  # Output: True
print(math.isnan(10))  # Output: False


sys.float_info # provides information about the float type in Python]


# 5 : Logarithms 

# math.log(x) gives the natural logarithm of x.

print(math.log(math.e))  # Output: 1.0
print(math.log(1))  # Output: 0.0
print(math.log(10))  # Output: 2.302585092994046
print(math.log(100))  # Output: 4.605170185988092

# 6 : Constants 
# math modules include two commonly used  mathematical constants

from math import pi ,e

print(pi)
print(e)

# Imaginary and complex numbers
# Imaginary numbers  in Python are represented by a "j" or "J" suffix.
# Complex numbers are represented as a pair of real and imaginary parts,

# 1j is the imaginary unit]
#  1J * 1J  # Output: (-1+0j)
#  (3 + 4j) * (1 - 2j)  #


#  8 : Copying signs 
# In python, we can use  the math.copysign(x,y) return x with the sign of y.
# returned value is  walys float 

print(math.copysign(3,-2)) # Output: -3.0
print(math.copysign(-3,2)) # Output: 3.0
print(math.copysign(-3,-2)) # Output: -3.0
