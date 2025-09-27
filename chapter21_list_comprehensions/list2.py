'''A list comprehension creates a new list by applying an expression to each element of an iterable. The most basic
form is:
[ <expression> for <element> in <iterable> ]
There's also an optional 'if' condition:
[ <expression> for <element> in <iterable> if <condition> ]'''


# example

squares = [x * x  for x in (1,2,3,4)]
print(squares)


#a list comprehension is roughly equivalent to the following for-loop

squaresTwo  = []

for x in (2,3,4,5):
    squaresTwo.append(x*x)

print(squaresTwo)    

# # Get a list of uppercase characters from a string

SquareUpperCase = [ s.upper()  for  s in    'Hello world']

print(SquareUpperCase)


#Sort list

print([  sorted(x) for x in [[3,5,7,8,4,2,10]]])


#--------------Print----------------
[print(value)  for value in (1,4,6,7,9,22)]



# reversed

print([ list(reversed(x))  for x in [[1,6,9,0,5,3]]])


# even 

print([ x for x in range(20) if  x % 2 ==0])

# odd 

print([x  for x in range(100) if x % 2 != 0])