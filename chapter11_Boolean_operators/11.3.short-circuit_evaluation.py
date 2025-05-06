# python minimally evaluates Boollean expressions.

def fun_true():
    print("fun_true()")
    print("True")

def fun_false():
    print("fun_false()")
    print("False")

"""
1 OR O
1 OR 1
0 OR O
0 OR 1

1 & O
1 & 1
0 & O
0 & 1
"""
# OR
print("OR",end="\n\n\n\n")

print(fun_true() or fun_false())
print(fun_false() or fun_true() )
print(fun_false() or fun_false())
print(fun_true() or fun_true() )

# AND
print(end="\n\n")
print("AND",end="\n\n\n\n",)
print(fun_true() and fun_false())
print(fun_false() and fun_true() )
print(fun_false() and fun_false())
print(fun_true() and fun_true() )