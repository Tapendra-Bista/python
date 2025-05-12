"""Python 3 added a new keyword called nonlocal. The nonlocal keyword adds a scope override to the inner scope.
You can read all about it in PEP 3104. This is best illustrated with a couple of code examples. One of the most
common examples is to create function that can increment:"""

def counter ():
    num = 0
    def incrementer():
        num += 1
        return num
    return incrementer

"""f you try running this code, you will receive an UnboundLocalError because the num variable is referenced before
it is assigned in the innermost function. Let's add nonlocal to the mix"""

print(counter())

 # using  nonlocal

def counter2 ():
    num = 0
    def incrementer ():
        nonlocal num # nonLocal
        num +=  1
        return num
    return incrementer


c = counter2()
print(c())
print(c())
print(c())
print(c())