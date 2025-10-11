#       parameter                   Details 
#!         f                  the function to be decorated


#Decorator function are software design patterns
#Decorators augments the behavior of  other functions or methods.
#? Any function that takes  a function as a parameter and 
#? returns an augmented function can be used as a decorator 
#  

        
import re
from unittest import result


def super_secret_function(f):
    return f


@super_secret_function
def f():
    print("This is my secret function.")

f()    

#The @-notation is syntactic sugar that is equivalent to the following:
# f = super_secret_function(f)  
# It is important to bear this in mind in order to understand how the decorators work. This "unsugared" syntax makes
#it clear why the decorator function takes a function as an argument, and why it should return another function. It
#also demonstrates what would happen if you don't return a function
#   

def disabled(f):
    '''This function returns nothings, and  hence removes the decorated function from the local scope.'''
    pass    

@disabled
def my_function():
    print('This function can no longer be called...')

# my_function()    

# Another Example math 

def math_func(my_func):
    def print_value(a,b):
        print('Addition :',a+b)
        return my_func(a,b)

    return print_value    

@math_func
def operation(a,b):
     pass 


operation(5,5)


#For class  we have to  used __call__  method

# Example 

class Decorator(object):
    '''Simple decorator class.'''

    def __init__(self,func):
        self.func = func

    def  __call__(self, *args, **kwds):
        print('Before the function call.')
        res = self.func(*args,**kwds)
        print('After the function call.')
        return res

@Decorator
def testfunc():
    print('Inside the function.')    
        
testfunc()


# .5 : Using  a decorator  to time a function

import time

def timer(func):
    def inner(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'Time taken to excecute {func.__name__}: {end - start} seconds')
        return result
    return inner


@timer
def example_function(n):
    total = 0
    for i in range(n):
        total += i
    return total

 
example_function(1000000)        

# .6 :  Create singleton class   using decorator 
# A  Singleton is a pattern that restricts the instantiation of a class to one single instance/object.
# Using a decorator, we can define a class as a singleton by forcing  the class to either  return an existing instance of  the class or create a new instance (if one does not already exist).

def singleton(cls):
    instance = [None]
    def wrapper(*args, **kwargs):
        if instance[0] is None:
            instance[0] = cls(*args, **kwargs)
        return instance[0]
    return wrapper        


#  This decorator can be added to any class  declaration and will make sure that at most one instance of the class  is created.
# Any subsequent calls will return the first instance created.
@singleton
class MyClass:
    x = 2
    def __init__(self):
        print('Initializing MyClass instance')

instance = MyClass()
print(instance.x) 

