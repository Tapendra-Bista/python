"""
1.There is no need  to declare in advance in python
2.You can assign a value without Type declaration
3. You can assign a value to a variable using the assignment operator (=).
syntax : <variable_name> = <value>
 value assign work from from lift to right 
 so following give error
 0 = x , "tapendra" =z

 Suppose X = 99
 X is a name  for  an object 99
Rules for naming variables:
1.names must be start from a letter or underscore.
for example _name = "Ram ", Name = "ram"
not 3name = "Tapendra " and Special symbol like $name = "Tapendra"
2.Includes any this if prifix is letter or underscore

"""
# integer
x=10
# double
y = 19.99
# string
z= "Tapendra Bista"
# boolean 
is_ram = False

print(x,y,z,is_ram)

# We can find the type of variable using the type function type()
print(type(x),type(y),type(z),type(is_ram))
"""
You can  assign multiple values to multiple variables in a single line.
Note : there must be same  number of argumenst on both sides lift and right after operator =
"""
#a,b,c = 9,9,9
#print (a,b,c)

#d,e = 1,2,3
#print(d,e) # this will give error
#f,g,h = 3,33
#print(f,g,h) # this will give error
# Above two lines will give error beacaue left and right 
# sides does not have same number of arguments
# in this case we can use _ (underscore) to make equal number of arguments
a,b,_ =3,33,333
print(a,b)
_,c = 69,99
print(c)
# You can  assign same value to multiple variables simultaneously.
# For example:

x=y=z=f=k="Same value"
print(x,y,z,f,k)
# You can change later too
# for example
z = "New value of Z  is Tapendra Bista"
print(x,y,z,f,k)
# this is alos true for all data types like
# int , string,double,boolean,list and etc.

# Nested also possible in python
# it's means we can used list inside list
# Example
# variable can start with lowercase as well as Uppercase
NestedList = [1,2,3,[4,5,[6,7,8,9]]]          
print(NestedList)
print (x[3])
print (x[1])
# change can be done in variable type even after declare in different type.

This_is_a_integer = 10
print(This_is_a_integer)
This_is_a_integer = "Now become String "
print(This_is_a_integer)
