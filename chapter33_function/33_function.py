# Functions

# parameter          Details 
# arg1.............. argN Regular arguments 
# *args.............. unnamed positional arguments
# KW1, ...KWN         ........... keyboard-only arguments
# **KWargs               The rest of keyword arguments 

###
# Function in python provide organized, 
# resuable and modular code to perform a set of specific
#  actions, Funtions simplify the coding process, prevent
#  redundant loogic, and make the code easier to follow. 
# This topic describes the declaration and utilization of 
# functions in python
#
# Python has many built-in functions like print(), 
# input(), len().
#  Besides built-ins you can also create your own 
# functions to do more specific jobs--
#  these are called use-defined functions
#
#   ###

# Section 33.1 Defining and calling simple functions 
# Using the def statement  is the most commom way to define a functon in python
# This statement is a so called single 
# clause compund statement with the following syntax :

from tracemalloc import start


def  function_name (name,address ):
    print(f"Name of user is {name} and live in {address}") # statements 


# Statements -- also known as the function body -- are a non empty 
#Squence of statement executed each time the function is called. This means a function body cannot be empty   #
function_name("John","New York")

# Simple example of greeding 

def greet ():
    print("Hello")

# Now let's call the defined greet () function:
greet()


def greet_two(greeting):
    print(greeting)

greet_two("Hello, Tapendra Bista")


# FUN with default arguments 

def fun_with_default(value= "Tapendra Bista") :
    print(f"Value of argument {value}")


# with default argument
fun_with_default()

# with  non deafult argument
fun_with_default("Ramesh Basnet")

# We donot need to explicitly  return any  type  via  return 
# one function can return different types of number 

# Example  

def many_types(user_input) :
    if user_input> 5:
        return f"The user input is {user_input}"
    else :
        return user_input


# calling function

print(many_types(10)) # output be String 
print(many_types(3)) # output be integer 

# Section 33.2: Defining a function with an arbitrary number of
#arguments

# defining a function capable to take arbitary number is done by using * at prefix of arguments
def func(*args):
#Func
    for x in args:
        print(f"Value printed {x}",end="\n")


func(1,2,3,4,5,6,7,8,9)

# collection 
collection =[1,2,3,4,5,6]

func(collection)
func(*collection)

# set 
my_set = {1,2,2,3,5,7,9,40,40}
func(my_set)
func(*my_set)       


# without arguments 
func()  # No print or output 


# You cannot provide a default for args, for example 
# func(*args=[1,2,3,4,5,6,7])
# will raise a syntax error 


# You can take an arbitrary number  of arguments with a name by defining an arguments in the dfinition with two * in prefix or front of it 


def fun_with_kwarg(**kwargs):
    for key, value in kwargs.items():
        print(f"Key is {key} and value is {value}")

# calling function
fun_with_kwarg(name="Tapendra",address="Kathmandu",country="Nepal")

my_dict ={'gender':'Male','height':5.9}
fun_with_kwarg(**my_dict)


# Section 33.3: Lambda (Inline/Anonymous) Functions
# Lambda keyboard create a inline function which have only one  line of code 
# For example consider
def greeting ():
    return "Hello"
    # which when called as 

print(greeting())     # Hello 

