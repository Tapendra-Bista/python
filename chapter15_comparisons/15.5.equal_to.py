"""This expression evaluates if x and y are the same value and returns the result as a boolean value. Generally both
type and value need to match, so the int 12 is not the same as the string '12"""

print(9==9)
print('k'=='k')
print(9.9 == 9.9)
print(True == True)
print([1,2,3]==[1,2,3])

#Section 15.6: Comparing Objects


"""In order to compare the equality of custom classes, you can override == and != by defining __eq__ and __ne__
methods. You can also override __lt__ (<), __le__ (<=), __gt__ (>), and __ge__ (>). Note that you only need to
override two comparison methods, and Python can handle the rest (== is the same as not < and not >, etc.)"""

class Foo(object):
    def __init__(self, item):
        self.my_item = item
    def __eq__(self, other):
        return self.my_item == other.my_item
   
a = Foo(5)
b = Foo(5)
print(a == b)
a == b     # True
print(a != b )
a != b     # False
a is b     # False

print(a is b )