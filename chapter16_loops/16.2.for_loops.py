"""for loops iterate over a collection of items, such as list or dict, and run a block of code with each element from
the collection.
for i in [0, 1, 2, 3, 4]:
    print(i)
The above for loop iterates over a list of numbers.
Each iteration sets the value of i to the next element of the list. So first it will be 0, then 1, then 2, etc. The output
will be as follow:
0
1
2
3
4
range is a function that returns a series of numbers under an iterable form, thus it can be used in for loops:
for i in range(5):
    print(i)
gives the exact same result as the first for loop. Note that 5 is not printed as the range here is the first five
numbers counting from 0.
Iterable objects and iterators
for loop can iterate on any iterable object which is an object which defines a __getitem__ or a __iter__ function.
The __iter__ function returns an iterator, which is an object with a next function that is used to access the next
element of the iterable"""

#-------------for loop in list------------------    
for i in [0,1,2,3,4,5,6,7,8,9,10]:
    print(i)

#----------------for loop in range-------------------------


for x in range(1,100):
    print(x)


    """for loop can iterate on any iterable object which is an object which defines a __getitem__ or a __iter__ function.
The __iter__ function returns an iterator, which is an object with a next function that is used to access the next
element of the iterable"""