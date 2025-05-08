"""Python operators have a set order of precedence, which determines what operators are evaluated first in a
potentially ambiguous expression. For instance, in the expression 3 * 2 + 7, first 3 is multiplied by 2, and then the
result is added to 7, yielding 13. The expression is not evaluated the other way around, because * has a higher
precedence than +.
Below is a list of operators by precedence, and a brief description of what they (usually) do."""



"""Python follows PEMDAS rule. PEMDAS stands for Parentheses, Exponents, Multiplication and Division, and Addition
and Subtraction"""

# () Parenthesis
# ** Exponents
# *  Multiplication
# /  Division
# +  Addition
# -  Subtraction

print((1+3)*3)
print(4**2 + 3 * 3)
print((3*4)**4*3/8+4-10)