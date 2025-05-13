"""Conditional expressions, involving keywords such as if, elif, and else, provide Python programs with the ability to
perform different actions depending on a boolean condition: True or False. This section covers the use of Python
conditionals, boolean logic, and ternary statements"""



# The ternary operator is used for inline conditional 
# expressions. It is best used in simple, concise operations
#  that are
#easily read


# example in dart
number =5

# number==5? print("Number is equal to Five") : print("number is not equal to five.")

# example in python

print("Number is greater than 2" if number>2 else "Number is less than 5")


"""The result of this expression will be as it is read in English - if the conditional expression is True, then it will evaluate
to the expression on the left side, otherwise, the right side.


Ternary operations can also be nested, as here"""
number =2
print("Number is greater than 5" if number>6 else "Number is less than 5"  if number>3  else "Number is less than 3")

"""In Python you can define a series of conditionals using if for the first one, elif for the rest, up until the final
(optional) else for anything not caught by the other conditionals"""

value = 1
if value>4 :
    print("Value is greater than four")
elif value>2 :
    print("Value is greater two")
else : print("Value is less than 2")    

# The following values are considered falsey, in that they evaluate to False when applied to a boolean operator.
"""
None
False
0, or any numerical value equivalent to zero, for example 0L, 0.0, 0j
Empty sequences: '', "", (), []
Empty mappings: {}
User-defined types where the __bool__ or __len__ methods return 0 or False



All other values in Python evaluate to True
"""

# example 
x = None
y = False
z = 0

print(x)
print(y)
print(z)

if x == False:
    print("X is False")
else :
    print("True")


if y == False:
    print(" y is False")
else :
    print("True")


if z == False:
    print(" Z is False")
else :
    print("True")



    """Boolean logic expressions, in addition to evaluating to True or False, return the value that was interpreted as True
or False. It is Pythonic way to represent logic that might otherwise require an if-else test.
And operator
The and operator evaluates all expressions and returns the last expression if all expressions evaluate to True.
Otherwise it returns the first value that evaluates to False:
>>> 1 and 2
2
>>> 1 and 0
0
>>> 1 and "Hello World"
"Hello World"
>>> "" and "Pancakes"
""
Or operator
The or operator evaluates the expressions left to right and returns the first value that evaluates to True or the last
value (if none are True).
>>> 1 or 2
1
>>> None or 1
1
>>> 0 or []
[]
Lazy evaluation
When you use this approach, remember that the evaluation is lazy. Expressions that are not required to be
evaluated to determine the result are not evaluated. For example:
GoalKicker.com – Python® Notes for Professionals 82
>>> def print_me():
        print('I am here!')
>>> 0 and print_me()
0
In the above example, print_me is never executed because Python can determine the entire expression is False
when it encounters the 0 (False). Keep this in mind if print_me needs to execute to serve your program logic"""





# Testing for multiple conditions

a = 10 
b = 20
c = 15
if   c>a and c<b :
    print("Yes")
else:
    print("No")



if c>a or c>b :
    print("Yes") 
else :
    print("No")






if a in (10, 20, 30, 40, 50):
    print("Yes")
else :
    print("No")
# The else statement will execute it's body only if preceding conditional statements all evaluate to False

if a>50 :
    print("")
else :
    print("Yes, now it will excutes")


# The if statements checks the condition. If it evaluates to True, it executes the body of the if statement. If it
#evaluates to False, it skips the body    

myList = []
if not myList :
    print("This List is empty")
else :
    print("This List isn't empty")
