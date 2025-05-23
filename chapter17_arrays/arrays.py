'''Parameter Details
b Represents signed integer of size 1 byte
B Represents unsigned integer of size 1 byte
c Represents character of size 1 byte
u Represents unicode character of size 2 bytes
h Represents signed integer of size 2 bytes
H Represents unsigned integer of size 2 bytes
i Represents signed integer of size 2 bytes
I Represents unsigned integer of size 2 bytes
w Represents unicode character of size 4 bytes
l Represents signed integer of size 4 bytes
L Represents unsigned integer of size 4 bytes
f Represents floating point of size 4 bytes
d Represents floating point of size 8 bytes
"Arrays" in Python are not the arrays in conventional programming languages like C and Java, but closer to lists. A
list can be a collection of either homogeneous or heterogeneous elements, and may contain ints, strings or other
lists'''

import array

# Individual elements can be accessed through indexes. Python arrays are zero-indexed
my_array =  array.array('i',[1,2,3,4,5])
print(my_array[0])
print(my_array[1])
print(my_array[2])
print(my_array[3])

#---------------second example--------------------
my_array2 = array.array('d',[98.57495797,5756.4564,45.3566])
print(my_array2[0])
print(my_array2[1])
print(my_array2[2])


#An array is a data structure that stores values of same data type. In Python, this is the main difference between
#arrays and lists

arrayString  = array.array('i',[1,2,3,4,5,6,7,8,9,10])
for i in arrayString:
    print(i)


# : Append any value to the array using append() method

example = array.array('i',[1,2,3,4])
print(example)
example.append(9)
print(example)

# We can use the insert() method to insert a value at any index of the array. Here is an example

example.insert(0,0)
print(example)

# A python array can be extended with more than one value using extend() method.

example2 = array.array('i',[10,11,23,25,55])
example.extend(example2)
print(example)

# : Add items from list into array using fromlist() method
myList = [66,77,88,99,100]
example.fromlist(myList)
print(example)


# : Remove any array element using remove() method
example.remove(99)
print(example)


#--------------pop removes the last element from the array.-------------------
example.pop()
print(example)

#--------------index() returns first index of the matching value. Remember that arrays are zero-indexed-----------------
result=    example.index(55)
print(result)

# The reverse() method does what the name says it will do - reverses the array
print(example)
example.reverse()
print(example)

# This method provides you the array buffer start address in memory and number of elements in array.
example.buffer_info()

#-----------------count() will return the number of times and element appears in an array-----------------
print(example.count(55))

# tostring() converts the array to a string
my_String = array.array('b',[ord('a'),ord('a'),ord('r')])
print(my_String.tobytes())
#When you need a Python list object, you can utilize the tolist() method to convert your array to a list.
print(example.tolist())


# You are able to append a string to a character array using fromstring()   
my_char_array = array('c', ['g','e','e','k'])
my_char_array.fromstring("stuff")
print(my_char_array)
#array('c', 'geekstuff')
