# Reversing elements 

# Reversing elements in the following way
my_tuples = ("apple","orange","banana","dragon")
print(my_tuples[::-1])
rev = my_tuples[::-1]

rev_tuples = tuple(rev)
print(rev_tuples)
 

# by using reversed fun
print(tuple(reversed(my_tuples)))