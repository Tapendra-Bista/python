#Functional programming decomposes a problem into a set of  function
#Ideally, functions only take inputs and produce outputs#

# 1. lambda functions
# inline anonymous functions 
# An anonymous, inlined function defined with lambda. The parameters of the lambda are defined to the left of the
# colon. The function body is defined to the right of the colon. The result of running the function body is (implicitly)
# returned.

# Example: A lambda function that adds two numbers
from ast import List
from functools import reduce
from itertools import filterfalse


add = lambda x,y : "Less than 10" if x+y<10 else 'Greater than or equal to 10'
print(add(3,4)) # Output: Less than 10
print(add(5,6)) # Output: Greater than or equal to 10


# 2. map function
# Map takes a function and a collection of items. It makes a new, empty collection, runs the function on each item in
# the original collection and inserts each return value into the new collection. It returns the new collection.

# Eaxmple : Using map make a new list of len of words
words_len = map(len,['hello','world','python','its','great','to','learn','python'])
print(list(words_len)) #! Output: [5, 5, 6, 3, 5, 2, 5, 6]  

def match_test(words_len):
    for i in words_len:
      match i :
        case 2 : print(f'Length is {i}, which is the smallest')
        case 3 : print(f'Length is {i}, which is the second smallest')
        case 4 | 5 : print(f'Length is {i}, which is a medium length')
        case _ : print(f'Length is {i}, which is a large length')

match_test(words_len)        

# 3. Reduce Function
# Reduce takes a function and a collection of items.
#  It returns a value that is created by combining the items.

total = reduce(lambda a, x: a * x, [1,2,3,4,5])
print(total)

# 4. Filter function 

#Filter takes a function and a collection. It returns a collection of every item for which the function return 
# True #

filter_list = [i for i in filter(lambda x: x>9,[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19])]
print(*filter_list)

addition_by_filter = [i for i in filter(lambda a: a+a,[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19])]
print(*addition_by_filter)

prime_number = [i for i in filter(lambda x: x%2==0,[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19])]
print(*prime_number)

odd_number = [i for i in filter(lambda x: x%2 !=0,[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19])]
print(*odd_number)