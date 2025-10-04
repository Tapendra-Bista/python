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

from ast import arg, arguments
from itertools import count
from math import factorial
from re import L, X
import sys
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

#  This can be written as lambda function as follow

greeting_me = lambda:"This is a lambda function "
print(greeting_me())


# lambda function to make upper case 
 
upper_word = lambda  s : s.upper()

print(upper_word("hello, tapendra bista"))


# can be used with arbitary number 

my_arbitary_number = lambda *args : print(args)

my_arbitary_number({1,2,3,4,5,6})

# This is mainly used for short function like sort, map , filter


# sorted 

# number 
print(sorted([1,4,7,8,9,3,10,20,33],key=lambda s : abs(s)))

# another 
print(sorted([-1,-99,3,44,66,100], key= lambda value : abs(value)))

# String example 
print(sorted(['tapendra','ram','','abhishek','hari'], key= lambda value : value.strip().upper()))
# This will make  list without empty elements and  with  upper case 

# filter in list
print(*list(filter(lambda value : value%2==0,[1,2,8,6,99,80,3,4,100])))





# one can call other functions (with/without arguments) from inside a  lambda function.

def foo(msg):
    print(msg) 

greet_new = lambda x = "Tapendra Bista" : foo(x) 


greet_new()


# NOTE  :  According to the python  style guide  doesnot recommand assigning  lamddas to  variabooles 

# Always use a def statement instead of  an assigment statement 
# that binds a lambda expression directly to an indentifier.


# YES / RIGHT 
def f(x): return 2*x

# NO / WRONG 
f = lambda x: 2*X



# Section 33.4 : Defining a function with optional arguments 

# Optional arguments  can be defined by assigning  a defualt value to the argument-name 

# Example
def make(action = 'nothing'):
    return print(action)

# This can be called in two different  form like 
    
#  with arguments 

make("This is an example of function with arguments")    

# without arguments 
make()



# NOTE : Mutable  types (list,dict,set,etc)(Which can be edit later) should be treated with care when given as default atrribute. Any mutation  of the default arguments will change it permanently. see defining a function with optional mutable arguments.


# Section 33.5: Defining a funtion with optional mutable arguments 

#
# There is a problem when using optional arguments with a mutable default type which can potentially lead to unexpected  behaviour.
#

def fx(a,b=42,c=[]):
    pass

print(fx.__defaults__)


# for  immutable 

# append function

def append(element, to=[]):
     to.append(element)
     return to


print(*append(1))
print(*append(2))
print(*append(3))
print(*append(4))
print(*append(5))
print(*append(6))
print(*append(7))
print(*append(8))
print(*append(9))
print(*append(10))

# Argument passing  and  mutability

#
# First Terminology 
# 
# argument (actual parameter ) : The actual variable being passed to a function 
# parameter (formal parameter ): the receiving variable that is used in a function #

# In Python, arguments are passed by assignment(as opposed to other langauges, where arguments can be passed by value/reference/ pointer).
# 
# 
# 
# 
##

def arg_example(x): # here x is the paramter 
    x[0] = 99  #  This mutates the list labelled by both x and y
    print(*x)

y =[1,2,3,4,5]
print(*y)
arg_example(y) # call func with y as  argument


#
# In Python, we don't assign value to the varible, instead we bind variables to objects
# 
# Immuatble : integers, strings, tuples, and so on . All operations make copies 
# Mutable : Lists, dictionaries, sets,  and so on . Operations  may or may not  mutate
# 
# 
# 
#    #

#Section  33.7: Returning values from functions 



# Functions can return  a value thay you cau use directly :
def give_me_five():
    return 5 
print(give_me_five()) # Print the returned value 


# or save the value for later use:

num = give_me_five()
print(num)


# oe use the value for any operations 

print(give_me_five()+ 10)

# If return is encountered in the function the  function will be exited immendiately and be evaluated :

def return_example ():
    return 5
    print("This statement will not be printed. Ever. ") # not excute

    
print(return_example())    
#You can also return multiple  values (in the form of a tuple)

def  multiple_return_example ():
    return 1,2,3,4,'Tapendra Bista',99.45  # act as tuples

one,two,three,four,name,age = multiple_return_example()

print(age)
print(name)




# A function without return can return None implicitly  so default  fun return None if we donot return any things 

def testing():
    print("Hello, tapsss") # without return 
    # return None , testing act as it 

print(testing())    

def return_none_example ():
    return None # Explicitly 


def return_none_implicitly() :
    value = 9    
    # No need to do any thing 


# Check Output 

print(return_none_example())
print(return_none_implicitly())

#  Section 33.8: Closure
# 
# 
#  Closure in python is created by calling  funnction. 
# Python 3 offers the nonlocal statement (Nonlocal Variables ) for realizing a full closure with nested functions
# 
# 

def makeInc (x):
    def inc(y):
        nonlocal x
        # Now assigning  a value to  x is allowed 
        
        x +=  y
        return x 
        
    return inc
    
incOne = makeInc(1)        #     #
incFive = makeInc(5)
print(incOne(2))  # 3   
print(incFive(10)) 



#Section 33.9 : Forcing the use of Named parameters
# 
# All parameter  specified after  first asterisk  in the function  signatures  are keyword-only 
#   For example 
# 
# 
def demo (*args,a,b):
    pass

demo(1,2,3,a=4,b=5)  # Correct
# demo(1,2,3,4,5)  # This will raise an error, because a and b are keyword-only parameters 1 to 5 all argmunts act as for *args and a,b empty 
 #  So, Named parameter is imp to avoid this types of problems #


#Section 33.10 : Nested Functions   
# 
#   Functions in Python are first-class objects . They are  defined in any scope 


def fibonaccic(n):
    def step (a,b):
        return b, a+b
    a,b = 0,1
    for i in range(n):
        print(f'value of i :{i}')
        a, b  = step(a,b)   

    return a


print("Fibonaccic of 5 : " ,fibonaccic(5))       


# Section 33.11 Recursion limit 
#   when the limit reach , we will get  Run Time Exception


def cursing (depth):
    try:
        cursing(depth +1)
    except RuntimeError as RE:
        print(f"I recursed {format(depth)} times!")
        print("I recursed {} times!".format(depth))

cursing(0)



# Recursion limit change be changed or increase by using  sys.getRecursionLimt 


print(f'Checking  limit of recursion {sys.getrecursionlimit()}')



#  Increasing limit 
sys.setrecursionlimit(2000)
cursing(0)
print(f'Checking  limit of recursion {sys.getrecursionlimit()}')
#
# 
# 
# Recursive  lambda  using  assigned  variable 
# 
# 
# 
# 
# 
# Example 
# 
# 

lambda_factorial = lambda i : 1 if i==0  else   i*lambda_factorial(i-1)

print(lambda_factorial(5))

# lambda   function are not  suggest by  official python guide  
# 

# Normal
# recurisve function 

# Recursive function is a  function  that calls  in its  definition. For example  the mathematical  function , factorial,
# defined by factorial (n) =  n * (n-1) * (n-2) * 3*2*1

def factorial (n):
    if n == 0:
        return 1
    else :
        return n*factorial(n-1)    

n= 5
print(f'factorial of {n} is ',factorial(n))


# section 33.14 function with arguments


def  divide (dividend, divisor):
    print(dividend/divisor)

divide(10,3)
divide(dividend=100,divisor=24)    


# Section  33.16:  Defining function  with  multiple arguments

def multi_argu(a,b,c,d,e,f,g,h,i,k,):
    print(a,b,c,d,e,f,g,h,i,k)


multi_argu(1,2,3,4,5,6,7,8,9,9)

