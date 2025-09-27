# Iterable
# an iterable is an object that can return an iterator
# Any object with state that has an __iter__ method   and returns an iterator 
# is an iterable
# it may be any object without state that implements the __getitem__ method.


# Iterator
# An iterator is an object that produces the next value 
# in a sequence when you call the next (*object*)  on some object


# Example of Iterable

# Iterable  classes define an __iter__ method and a __next__ method 

class MyIterable:
    def __iter__(self):
        return self


    def __next__(self):
        return print("next value")  


MyIterable_obj = MyIterable()
MyIterable_obj.__iter__()
MyIterable_obj.__next__()  # next value        

# Classic iterable object in older versions of python ,
# __getitem_ method is used to make an object iterable

class MySequence:
    def __getitem__(self, index):
        if index < 5:
            return print(f"Value at index {index}")
        else: 
            raise IndexError("Index out of range")

MySequence_obj = MySequence()
MySequence_obj.__getitem__(0)  # Value at index 0
MySequence_obj.__getitem__(1)  # Value at index 1       
#MySequence_obj.__getitem__(19) # IndexError: Index out of range

# Example of Iterator   
class MyIterator:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.limit:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration

MyIterator_obj = MyIterator(3)
print(next(MyIterator_obj))  # 0    

print(next(MyIterator_obj))  # 1

# Section 32.2: Extract values one by one using iter() and next()
my_list = [10, 20, 30]
my_iter = iter(my_list)  # Get an iterator from the list            
print(next(my_iter))  # 10
print(next(my_iter))  # 20
print(next(my_iter))  # 30      
# next(my_iter)  # StopIteration

# Section 32.3: Iterating over entire iterable
for value in my_list:
    print(value)


# Section 32.4: Verify only one element in iterable
a = [1,2,3,4,5]    
def foo():
    yield from a

b =foo()

print(next(b))
print(next(b))
print(next(b))
print(next(b))



# Section 32.5: What can be iterable
# Iterable can be anything for which  items  are received one by one,
# forward only . Built-in pyhton collections are  iterable

my_tuple = (1,2,3)
for item in my_tuple:
    print(item)


# Section 32.6: Iterator isn't reentrant!
def gen():
    yield 1
    yield 2
    yield 3
iterable  = gen()    
for a in iterable:
    print(a)


gen()