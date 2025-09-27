# Built-in Tuple Functions



tuple_one = (1,2,3,4,5)
tuple_two = (1,2,3,4,5)
# Comparison
result =  tuple_one == tuple_two
print(result)


# length of tuple
print(len(tuple_one))

# Max element in tuple 
print(max(tuple_two))

# min element in tuple 
print(min(tuple_two))

# conervt list into tuple 
my_list = [1,2,3,4,5,6,7,8,9,9,0,99,8,7,6]
my_tuple = tuple(my_list)
print(my_tuple)

# concatenate two tuples
print(tuple_one + tuple_two + my_tuple)