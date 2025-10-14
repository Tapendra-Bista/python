# class
# Python offers itself not only as a popular scripting language,but
# also supports object oriented programming language paradigm.
# Classes describe data and provide methods to manipulate that data, all encompassed under a single object.
# FotherMore, classes allow for abstraction by separating concrete implementation details from
# abstract representations of data.


#! Code  utilizing classes easier to read, understand, and maintain.

#! 1. Introduction to classes

from print_color_text import color_print

from email.policy import default
from mimetypes import init
import string
from tokenize import String
from turtle import color


class Person(object):
    '''A Simple clsss.''' #* docstring
    species = 'Home sapiens' #* class atttribute

    def __init__(self,name):  #* special method
       '''This is the initializer. It's a special method (see below)'''
       self.name = name  #* instance attribute

    def __str__(self) : #* special function
        '''This is the initializer . It's a special method (see below).'''
        return self.name   

    def rename (self,renamed):  #* regular method
        '''Reassign and print the name attribute.'''     
        self.name = renamed
        print('Now my name is ',format(self.name))

#! There are a few things to note when looking at the above example.

#* 1.The class is made up of attributes (data) and methods (functions).1.
#* 2.Attributes and methods are simply defined as normal variables and functions.2.
#* 3.As noted in the corresponding docstring, the __init__() method is called the initializer. It's equivalent to the3.
#* constructor in other object oriented languages, and is the method that is first run when you create a new
#* object, or new instance of the class.
#* 4.Attributes that apply to the whole class are defined first, and are called class attributes.4.
#* 5.Attributes that apply to a specific instance of a class (an object) are called instance attributes. They are5.
#* generally defined inside __init__(); this is not necessary, but it is recommended (since attributes defined
#* outside of __init__() run the risk of being accessed before they are defined).
#* 6.Every method, included in the class definition passes the object in question as its first parameter. The word6.
#* self is used for this parameter (usage of self is actually by convention, as the word self has no inherent
#* meaning in Python, but this is one of Python's most respected conventions, and you should always follow it).
#* 7.Those used to object-oriented programming in other languages may be surprised by a few things. One is that7.
#* Python has no real concept of private elements, so everything, by default, imitates the behavior of the
#* C++/Java public keyword. For more information, see the "Private Class Members" example on this page.
#* 8.Some of the class's methods have the following form: __functionname__(self, other_stuff). All such8.
#* methods are called "magic methods" and are an important part of classes in Python. For instance, operator
#* overloading in Python is implemented with magic methods. For more information, see the relevant
#* documentation  


# Instances
ram = Person('Ram')
shyam = Person('shyam')

print(ram.species)
print(shyam.species)
print(ram.name)

# Methods
ram.rename('Tapendra')


#! 2. Bound, unbound, and static methods

#The idea of bound and unbound methods was removed in Python 3.
# In Python 3 when you declare a methood within a class, you are using a def keyword, thus creating a function object. This is regular function, and the surrounding
# class works as its namespace. In the following example we declare method f within class A, and it becomes a function A.f:#

class A():
    def f(self,x):
        return 2*x


a = A()
print(a.f(2))

#In Python 2 the behavior was different: function objects within the class were implicitly replaced with objects of type
# instancemethod, which were called unbound methods because they were not bound to any particular class instance.
# It was possible to access the underlying function using .__func__ property.
# Python 2.x Version ≥ 2.3
# A.f


# # <unbound method A.f> (in Python 2.x)
# A.f.__class__
# # <type 'instancemethod'>
# A.f.__func__
# # <function f at ...>
# The latter behaviors are confirmed by inspection - methods are recognized as functions in Python 3, while the
# distinction is upheld in Python 2


# Python has class methods and static methods - special  kinds of methods. Class methods work the same
#way as regular methods, except that when invoked on an object they bind to the class of
# the object instead of to the object. Thus m.__self__ = type(a).
# When you call such bound method, it passes the class of a as the first
# arguments. Static methods are even simpler: they don't bind anything at all,
# and simply return the underlying function without any transformations.
# 
# #

class D(object):
    value_of_a = 2

    @classmethod  # similar to static they are bind to class rather then class objects
    def f(self,x):
        return self.value_of_a*x

    @staticmethod #  they don't bind anything at all,
    def my_static_method(name):     
      return  print(f"value of x  and value of name {name}")    

# Note that class methods are bound to the class even when accessed on the instance:


d = D()
d.value_of_a = 1
print(d.f(99))

print(d.my_static_method(name='Tapendra'))


# It is worth nothing that at the lowest level, functions, methods, staticmethods, etc. are actually descriptors that
# invoke __get__, __set__ and optionally __del__ special methods.

#! 3. Basic inheritance
# Inheritance in Python is based on similar ideas used in other object oriented languages like java, c++ etc.
# A new class can be derived from an existing class as follows

class BaseClass (object):
    pass

# way to inheritance in python
class DerivedClass(BaseClass):
    pass

# The BaseClass is the already existing (parent) class, and the DerivedClass is the new (child) class that inherits (or
# subclasses) attributes from BaseClass. Note: As of Python 2.2, all classes implicitly inherit from the object class,
# which is the base class for all built-in types.

# We define a parent Rectangle class in the example below, which implicitly inherits from object:

class Rectangle ():
    def __init__(self,l,b) -> print('Initialized...'):
        self.l = l
        self.b = b

    def area(self):
        return print(f'The area of rectangle is {self.l*self.b} with length {self.l} units and breadth {self.b} units')

    def  perimeter (self):
        return print(f'The perimeter of rectangle is {2*(self.l+self.b)} with length {self.l} units and breadth {self.b} units')      


rectangle = Rectangle(10,10)
rectangle.area()
rectangle.perimeter()


# The rectangle class can be used as a base class for defining a Square class, as a square is a special case of rectangle

#* way to inheritance in python
class Square(Rectangle):
    def __init__(self,side) -> print('Initialized Square...') :
        super().__init__(side,side)  #* super() function is used to give access to methods and properties of a parent or sibling class.
         
    def areaInheritanceCase(self):
        return print(f'The area of square is {self.l*self.b} with length {self.l} units' )


square = Square(10)
square.area()
square.areaInheritanceCase()
square.perimeter()   


# Built-in functions that work with inheritance
# checking instance 
print(isinstance(square, Square))
# checking subclass
print(issubclass(Square,Rectangle))



# Example 

class Animal :
    def __init__(self,animalName) -> print('Initialized'):
        self.animalName = animalName

    def sound (self):
        match(self.animalName):
            case 'cat' : return print('Meow Meow !')
            case 'dog' : return print('Bhow Bhow !')
            case  'goat' : return print('may may !')
            case _: return print('Somethings went wrong !')


# inheritance

class Cat(Animal) :
    def __init__(self, animalName) -> print('Initialized'):
        super().__init__(animalName)



# instance 

cat = Cat('cat')
cat.sound()


#---------------Monkey Patching------------
# In this case, 'Monkey Patching' means adding a new variable or method to a class after it's been defined. For
# instance, say we defined class Demo as

class Demo(object):
    def __init__(self,num) -> None:
        self.num = num


    def __add__(self,other):
        return self.num+ other   


# suppose, we want to add another function later in the code. like this
# But how we want to add another function later in  the code. Suppose this function is as follows  

def get_num(self):
    return self.num        

# But how do we add this as a method in A? That's simple we just essentially place that function into Demo with an assignment statement.



# instance 
demo = Demo(99)
Demo.get_num = get_num(demo)
print(demo.__add__(other=99))
print(get_num(demo))

# Note that, unlike some other langauge, this technique does not work for certain built-in types, and it is not considered good style.


#------ ----------- 5: New-style vs old-style classes---------------

# New-style classes were introduced in python 2.2 to unify classes and types.
# They inherit from the top-level object type.
#  A new-styles class is a user-defined type, and is very to built-in types.

# new-style class

class New (object):  # new style class like fun style with parameter object
    pass

# new-style instance
new = New()

new.__class__
type(new)
print(issubclass(New,object))


# old-style classes do not inherit from object.
# Old-style instances are always implemented with a built-in instance type.

# old-style class
class Old:
    pass

# only-style instance

old = Old()

print(old.__class__)
print(type(old))
print(issubclass(Old, object))



# In Python 3, all classes are new-style classes, and the distinctintion be 
# tween new-style and old-style classes is no longer relevant.

class MyClass:  # this is also new style class
    pass
my_instance = MyClass()
print(isinstance(my_instance, MyClass))
print(isinstance(my_instance, object))
print(issubclass(MyClass, object))
print(issubclass(MyClass, MyClass))
print(my_instance.__class__)
print(MyClass.__class__)
print(MyClass.__bases__)
print(object.__class__)
print(object.__bases__)
print(type(my_instance))
print(type(MyClass))


# 6: Class methods: alternate initializers

# Class methods present alternate ways to build  instances of classes.
# Example

class Person:
    def __init__(self,first_name,last_name,age) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.full_name  = first_name + ' ' + last_name

    def greet(self):
        return print(f'Hello, my name is {self.full_name} and I am {self.age} years old.')



person = Person('Ram','Shrestha',24)
person.greet()


# Suppose  user does not have full name 

class PersonExample:
    def __init__(self, first_name, age, last_name=None) -> None:
        if last_name is None:
            parts = first_name.split(maxsplit=1)  # split on whitespace once
            if len(parts) == 2:
                self.first_name, self.last_name = parts
            else:
                self.first_name = first_name
                self.last_name = ""
        else:
            self.first_name = first_name
            self.last_name = last_name

        self.age = age
        self.full_name = f"{self.first_name} {self.last_name}".strip()

    def greet(self):
        return print('Hello, my name is {} and I am {} years old.'.format(self.full_name, self.age))        


p2 = PersonExample('Ram', 24)   # works; last_name becomes empty
# None last name
p2.greet()

# However, there are two main problems with this bit of code:
# The parameters first_name and last_name are now misleading, since you can enter a full name for1.
# first_name. Also, if there are more cases and/or more parameters that have this kind of flexibility, the
# if/elif/else branching can get annoying fast.
# Not quite as important, but still worth pointing out: what if last_name is None, but first_name doesn't split2.
# into two or more things via spaces? We have yet another layer of input validation and/or exception
# handling...
# Enter class methods. Rather than having a single initializer, we will create a separate initializer, called
# from_full_name, and decorate it with the (built-in) classmethod decorator.


class PersonWithClassMethod:
    def __init__(self,name ,age , cast)-> None:
        self.name = name
        self.age = age 
        self.cast = cast
        self.full_name = name + ' ' + cast

    @classmethod
    def from_full_name(cls,full_name,age):
        if " " not  in full_name:
         raise ValueError('Full name must contain at least a first name and a last name') 
        name,cast = full_name.split(' ',1)
        return cls(name,age,cast)  # cls refers to the class itself



    def    greet(self):
        return print('Hello, my name is {} and I am {} years old. '.format(self.full_name,self.age))
# 💡 What is self?
# self refers to the current instance (object) of the class that is calling the method.


p3 = PersonWithClassMethod('Ram',24,'Brahmin')
p3.greet()

p4 = PersonWithClassMethod.from_full_name('Ram Shrestha',24)
p4.greet()

# 7: Multiple Inheritance

# Python uses the C3 linearization algorithm to determine the order in which to resolve class attributes, including
# methods. This is known as the Method Resolution Order (MRO).

#  Example 
class Foo:
    foo = 'attr foo of Foo'



class Bar:
    foo = 'attr foo of Bar'  # we won't see this 
    bar = 'attr bar of Bar'  # 



class FooBar(Foo,Bar):
    foobar = 'attr foobar of FooBar'

    # Now if we instantiate FooBar, if we look up the foo attribute, we see that Foo's attribute is found first


foobar = FooBar()

print(foobar.foo)  # prints 'attr foo of Foo'
print(foobar.bar)  # prints 'attr bar of Bar'
print(foobar.foobar)  # prints 'attr foobar of FooBar'
print(foobar.foo)

# 
# Here's the MRO of FooBar:

print(FooBar.__mro__)


# It can be simply stated that Python's MRO algorithm is
# Depth first (e.g. FooBar then Foo) unless1.
# a shared parent (object) is blocked by a child (Bar) and2.
# no circular relationships allowed.3.
# That is, for example, Bar cannot inherit from FooBar while FooBar inherits from Bar.
# For a comprehensive example in Python, see the wikipedia entry.

# Another powerful feature in inheritance is super. super can fetch parent classes features.



class Foo1:
    def foo_method(self):
        return print('Called foo_method')


class Bar1:
    def bar_method(self):
        return print('Called bar_method')




class FooBar1(Bar1,Foo1):
    def foobar_method(self):
        super().foo_method()
        super().bar_method()
        return print('Called foobar_method')


foobar1 = FooBar1()

foobar1.foobar_method()

print(FooBar1.__mro__)


# Multiple inheritance with init method of class, when every class has own init method then we try for multiple
# inheritance then only init method get called of class which is inherit first.
# for below example only Foo class init method getting called Bar class init not getting called

class Foo2:
    def __init__(self) -> None:
        print('Initialized Foo2')

class Bar2:
    def __init__(self) -> None:
        print('Initialized Bar2')


class FooBar2(Foo2,Bar2):
    def __init__(self) -> None:
        super(FooBar2,self).__init__()
        print("Initialized FooBar2")                


foobar2 = FooBar2()

# But it doesn't mean that Bar class is not inherit. Instance of final FooBar class is also instance of Bar class and Foo
# class.

print ( isinstance(a,FooBar))
print (isinstance(a,Foo))
print (isinstance(a,Bar))

print(isinstance(foobar2, FooBar2))
print(isinstance(foobar2, Foo2))
print(isinstance(foobar2, Bar2))


# 8: properties
# Python classes support properties, which look like regular object variables, but with the possibility of attaching
# custom behavior and documentation.

class Myclass:
    def __init__(self) -> None:
        self.my_string = ''


    @property
    def string(self):
        '''A profoundly  important string.'''
        return self._my_string

    @string.setter
    def string(self,value):
        if not isinstance(value,str):
            raise ValueError('my_string must be a string')
        self._my_string = value

    @string.deleter
    def string(self):
        self.my_string = None


# The object's of class MyClass will appear to have a property .string, however it's behavior is now tightly controlled:

my_instance = Myclass()
my_instance.string = "Hello, World!"  # calls the setter
print(my_instance.string)
del my_instance.string  # calls the deleter
print(my_instance.string)


# Section 38.9: Default values for instance variables
# If the variable contains a value of an immutable type (e.g. a string) then it is okay to assign a default value like this

class Rectangle :
    def __init__(self,width,length,color='blue') -> None:
        self.width = width
        self.length = length
        self.color = color

    def area(self):
        return color_print(f'Area :{self.width* self.length}', color=self.color)    


# Create some instances of the class

r1 = Rectangle(10,20)
print(r1.color)
r1.area()

r2 = Rectangle(5,5,'red')
print(r2.color)
r2.area()


# One needs to be careful when initializing mutable objects such as lists in the constructor. Consider the following
# example:


class Rectangle2D:
    def __init__(self,width,length,pos=[0,0]) -> None:
        self.width = width 
        self.legth = length
        self.pos = pos 



rec = Rectangle2D(10,20)
rec1 = Rectangle2D(5,5)
rec.pos[0] = 100
print(rec.pos)
print(rec1.pos)

# Both printed [100,0], but wee have set only for instance rec.


# This behavior is caused by the fact that in Python default parameters are bound at function execution and not at
# function declaration. To get a default instance variable that's not shared among instances, one should use a
# construct like this:

class Rectangle2DExample:
    def __init__(self,length,width,pos= None) -> None:
        self.length = length 
        self.width = width 
        self.pos = pos if pos is not None else [0,0]


rec2 = Rectangle2DExample(10,20)
rec2.pos[0] = 99
print(rec2.pos)
rec3 = Rectangle2DExample(5,5)
print(rec3.pos)
# Now the two instances have independent pos attributes.


# Section 38.10: Class and instance variables


# Instance variables are unique for each instance, while class variables are shared by all instances.

class C:
    X = 2 # class variable 
    
    def __init__(self,y) -> None:
        self.y = y # instance variable 


print(C.X)  # prints 2
c1 = C(3)

print(c1.y) # prints 3

# Class variables can be accessed on instances of this class, but assigning to the class attribute will create an instance
#  variable which shadows the class variable

c1.X = 99
print(c1.X)  # prints 99 


# Section 38.11: Class composition


# Class composition allows explicit relations between objects. In this example, people live in cities that belong to
# countries. Composition allows people to access the number of all people living in their country:

class Country(object):
    def __init__(self) -> None:
        self.cities = []

    def add_city(self,city):
        self.cities.append(city)    



class City(object):
    def __init__(self,numPeople) -> None:
        self.numpeople = numPeople
        self.people = []

    def add_person(self,person):
        self.people.append(person)

    def join_country(self,country):
        # Link city to country; do not call self.people(...)
        self.country = country
        country.add_city(self)



class Person(object):
    def __init__(self,ID) -> None:
        self.ID = ID 

    def join_city(self,city):
        self.city = city
        city.add_person(self)    

    def people_in_my_country(self):
        return sum(len(c.people) for c in self.city.country.cities)
# Create instances OUTSIDE the class body
Us = Country()
NYC = City(1000)
NYC.join_country(Us)
for i in range(NYC.numpeople):
    Person(i).join_city(NYC)

print(Us.cities[0].people[0].people_in_my_country())  # prints 1000





# 12: Listing All Class Members 
# the dir () function can be used to  get a list of the member of a class:
print(dir(Country))





# Section 38.14: Descriptors and Dotted Lookups


# Descriptors are objects that are (usually) attributes of classes and that have any of __get__, __set__, or
# __delete__ special methods.
# Data Descriptors have any of __set__, or __delete__
# These can control the dotted lookup on an instance, and are used to implement functions, staticmethod,
# classmethod, and property. A dotted lookup (e.g. instance foo of class Foo looking up attribute bar - i.e. foo.bar)
# uses the following algorithm:
# bar is looked up in the class, Foo. If it is there and it is a Data Descriptor, then the data descriptor is used.1.
# That's how property is able to control access to data in an instance, and instances cannot override this. If a
# Data Descriptor is not there, then
# bar is looked up in the instance __dict__. This is why we can override or block methods being called from an2.
# instance with a dotted lookup. If bar exists in the instance, it is used. If not, we then
# look in the class Foo for bar. If it is a Descriptor, then the descriptor protocol is used. This is how functions3.
# (in this context, unbound methods), classmethod, and staticmethod are implemented. Else it simply returns
# the object there, or there is an AttributeError