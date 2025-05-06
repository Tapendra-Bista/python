"""Evaluates to the second argument if and only if both of the arguments are 
truthy. Otherwise evaluates to the first
falsey argument"""

# AND
print("and ",end="\n\n\n")
print(True and True)
print(True and False)
print(False and False)
print(False and True,end="\n\nor \n\n\n")




"""Evaluates to the first truthy argument if either one of the arguments is truthy.
 If both arguments are falsey,
evaluates to the second argument"""

# OR
print(True or True)
print(True or False)
print(False or False)
print(False or True,end="\n\nnot \n\n\n")


"""It returns the opposite of the following statement"""
print(not True)
print(not False)
