# LIST : mix, added, remove possible,square bracket
# TUPLES : never add,remove ,small bracket
# DICTIONARY : key-value pairs, curly bracket,mix
# SET : no duplicate value , never add,remove , curley bracket

from collections import defaultdict




# there are a number of collection types in python.
# Lists type is probably the most commonly used collection type in python.
# A list can be created by enclosing values, separated by commas,
#  in square brackets

# string list
String_lists = ["tapendra","ramesh","kamal","hari"]
print(String_lists)
# integer list
Integer_lists = [1,2,3,4,5,6,7,8,9,10]
print(Integer_lists)
# empty list
empty_list = []
print(empty_list)
#The elements of a list are not restricted
#  to a single data type, which makes sense given that
#  Python is a dynamic language

mixed_list = [1,"string",True,99.90,None]
print(mixed_list)
# a list can contain another list
#  as its element

nested_list = ["first","list",["nested","list"]]
print(nested_list)
"""The elements of a list can be accessed
 via an index, or numeric
   representation of their position. 
Lists in Python are
zero-indexed meaning that the first 
element in the list is at index 0,
 the second element is at 
 index 1 and so on"""

names =["ram","hari","laxman","sita"]
print(names[1])
print(names[2])
# indices can be negative in python
# negative index start from -1 which indicates last element of the list 
# and Lists are mutable its  means value can be change later in list.

"""
methods in list
> append to add new onject to end of list
> insert to add new object at specific index
>  remove to remove objects which first occurance in list 
> index to return index of an object
> len to counts size of list
> count to count repeated onjects in list
> reverse to reverse a list
> pop to remove last object of a list
You can iterate over the list elements like below:
for element in my_list:
    print (element)
"""
myList = [1,2,3,4,5,6,7,8,9,1,1,1,1,1,1,1000]
print(myList)
myList.append(10)
print(myList)
myList.insert(5,99)
print(myList)
myList.remove(1)
print(myList)
myList.index(1)
print(myList)
len(myList)
print(myList)
myList.reverse()
print(myList)
myList.pop()
print(myList)
myList.count(1)
print(myList.count(1))
myList.clear()
print("All clear ")

# Tuples
# A tuples is similar to a list except that is fixed - length and immutable (never change) and
#  also never added to new objects
# also never remove objects from tuples
ip_adress = ('10.20.30.40',8080)
print("ip adress is :",ip_adress)
# index is same as list 
print(ip_adress[1])
# print 8080

# when there is one member in tuples , we must use  comma (,)
# or without  use of bracket
# example
oneMemberTuples = ('Tapendra',)
# or
one_Member_Tuples = 'tuples two',
print(oneMemberTuples)
print(one_Member_Tuples)
# or just using tuple syntax 
another_tuples = tuple(['only one member'])
print(another_tuples)

# Dictionaries
# A dictionary in python is a collection of key-pairs. 
#  The dictionary is surronded by curely bracket and each key-pairs is separated by comma (,)
# key is always in left side and value at right side
# in between key and value there is a colon (:)
# for example of Dictionary

personDetails = {
    'name': "Tapendra Bista",
    'age': 23,
    'phone': 9804633911,
    'address': "Kailai"
    ,'email': "tapendrabista01@gmail.com",
    'college': "Amrit Campus",
    'Hubby': "Touring",
    'subject' : {
        'sub1':"data warehousing and data mining",
        'sub2': "Advanced java"
        ,'sub3' : "Project management"
    }
}

# Dictionaries strongly resemble 
# JSON syntax
print(personDetails)
print(personDetails['name'])
print(personDetails["subject"])
for k in personDetails.keys():
    print(k,": ",personDetails[k])
    # SET
    # A set is a collection of elements without no repeats and without insertion order  but without sorted order

    """
    A set is a collection of elements with no repeats and without insertion order but sorted order. They are used in
situations where it is only important that some things are grouped together, and not what order they were
included. For large groups of data, it is much faster to check whether or not an element is in a set than it is to do
the same for a list

    """

    # defining set is similar to dictionary
    # things to need to known 
    # there must not be repeated elements or object
    # we use curley bracket in Set


fullName = {"Tapendra","Bahadur","Bista"}
print(fullName)
 #print(fullName[1]) not possible in SET
# we can also convert list to set
list_to_set = [1,2,3,4,5]
my_set = set(list_to_set)
print(my_set)
#print(my_set[2]) NOT POSSIBLE IN SET
name = "Tapendra"
if name in fullName:
    print("Name is available ",name)

    # defaultDic 
    # in this, we don't get any error if there is no key because we can set default for non existing key in dictionaries

print(personDetails)
personDetails = defaultdict (lambda: "Not available")
print(personDetails['mobile'])

