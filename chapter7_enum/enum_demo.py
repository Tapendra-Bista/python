from enum import Enum

# enum in other language 
# in dart 
# enum { red,back,whiite}
# in python need to make class and pass enum in parameter


# creating
class Color(Enum):
    red =1
    green =2
    blue =3


print(Color.red)
print(Color.green)
print(Color.blue)
print(Color(2))
print(Color['blue'])
print(Color.blue.name)


# iteration

for c in Color:
    print(c.name)