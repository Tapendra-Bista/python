'''Parameter Details
key The desired key to lookup
value The value to set or return'''


'''A dictionary is an example of a key value store also known as Mapping in Python. It allows you to store and retrieve
elements by referencing a key. As dictionaries are referenced by key, they have very fast lookups. As they are
primarily used for referencing items by key, they are not sorted'''

from collections import defaultdict,ChainMap
# creating 

my_dictionary = {'name' : 'tapedra' , 'class': 'Bachlor', 'age' :25, 'height':5.8}

for i,j in my_dictionary.items():
    print(i ," : ",j)


# only key 
for key in my_dictionary.keys():
    print(key)

# only value
for value in my_dictionary.values():
        print(value)    


# another way 
second_dictionary = dict(key='value',value = 10)

print(second_dictionary['value'])


# modifying  
my_dictionary['age'] = 99

print(my_dictionary['age'])



# Avoiding KeyError Exceptions

'''One common pitfall when using dictionaries is to access a non-existent key. This typically results in a KeyError
exception'''

#example

test = {} # empty dictionary
# getting error here (Key error) print(test['not things']) 


'''One way to avoid key errors is to use the dict.get method, which allows you to specify a default value to return in
the case of an absent key'''

test.setdefault('not things', 'Hello value')

print(test['not things']) 



#An alternative way to deal with the problem is catching the exception

# test2= {}

# try:
#   value = test2['hello']
# except KeyError :
#      value = test2.setdefault['hello','This is an example' ]  

# print(value)      





'''
If you use a dictionary as an iterator (e.g. in a for statement), it traverses the keys of the dictionary. For example:
GoalKicker.com – Python® Notes for Professionals 110
d = {'a': 1, 'b': 2, 'c':3}
for key in d:
    print(key, d[key])
# c 3
# b 2
# a 1
The same is true when used in a comprehension
print([key for key in d])
# ['c', 'b', 'a']
Python 3.x Version ≥ 3.0
The items() method can be used to loop over both the key and value simultaneously:
for key, value in d.items():
    print(key, value)
# c 3
# b 2
# a 1
While the values() method can be used to iterate over only the values, as would be expected:
for key, value in d.values():
    print(key, value)
    # 3
    # 2
    # 1
Python 2.x Version ≥ 2.2
Here, the methods keys(), values() and items() return lists, and there are the three extra methods iterkeys()
itervalues() and iteritems() to return iterators'''


d = {'a': 1, 'b': 2, 'c':3}
for key in d:
    print(key, d[key])



for key, value in d.items():
    print(key, value) 

    # Dictionary with default values

x = defaultdict(int)
x['key']=0
x['key']=5

for i in x.values():
     print(i)

xx ={}

xx.setdefault('key',[]).append("This worked!")

print(xx['key'])


# merging dictionary
fish = {'name': "Nemo", 'hands': "fins", 'special': "gills"}
dog = {'name': "Clifford", 'hands': "paws", 'color': "red"}

fishDog = {**fish,**dog}
print(fishDog)

dogFish = dict(ChainMap(dog,fish))

print(dogFish)

#Accessing keys and values
'''When working with dictionaries, it's often necessary to access all the keys and values in the dictionary, either in a
for loop, a list comprehension, or just as a plain list'''


example3 ={'1': 'one', '2' :'two' ,'3' :'three'}
print(example3.keys())
print(example3.values())
print(example3.items())