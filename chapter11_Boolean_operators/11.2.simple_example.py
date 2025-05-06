# in python we can compare one elements using  two binary operators --one on either side

# example
def demo(x):
    if 3.141<x>3.140:
        print("yes : ",x)
    else :
        print("Not")

       
demo(3.142)      
"""In many (most?) programming languages, this would be evaluated in a way contrary to regular math: (3.14 < x) <
3.142, but in Python it is treated like 3.14 < x and x < 3.142, just like most non-programmers would expect."""

