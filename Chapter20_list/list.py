# '''The Python List is a general data structure widely used in Python programs. They are found in other languages,
# often referred to as dynamic arrays. They are both mutable and a sequence data type that allows them to be indexed
# and sliced. The list can contain different types of objects, including other list objects'''

# # Example
# my_list = [1,2,3]
# print(my_list)

# # append(value) – appends a new element to the end of the list.

# my_list.append(4)
# my_list.append(5)

# print(my_list)

# # extend(enumerable) – extends the list by appending elements from another enumerable

# second_list = [9,8,5]
# my_list.extend(second_list)

# print(my_list)

# '''index(value, [startIndex]) – gets the index of the first occurrence of the input value. If the input value is3.
# not in the list a ValueError exception is raised. If a second argument is provided, the search is started at that
# specified index'''


# print(my_list.index(3))


# """nsert(index, value) – inserts value just before the specified index. Thus after the insertion the new4.
# element occupies position index"""
# my_list.insert(0,999)
# print(my_list)

# '''pop([index]) – removes and returns the item at index. With no argument it removes and returns the last5.
# element of the list'''
# print(my_list.pop(0))
# print(my_list)

# #reverse() – reverses the list in-place and returns None 
# my_list.reverse()

# print(my_list)

# my_list.sort()

# print(my_list)

# print(my_list[2])



# # ch3cking  list is empty or not 
# if  my_list:
#     print(("List is not empty "))
# else :
#     print("Empty")


# # iteratig 
# for item in my_list:
#     print(item)    




# ''' Checking whether an item is in a list'''  

# '''Note: the in operator on sets is asymptotically faster than on lists. If you need to use it many times on
# potentially large lists, you may want to convert your list to a set, and test the presence of elements on
# the set'''


# my_set = set(my_list)

# print(
# 1 in my_set )

# print(90 in my_list)
        

#         #You can use all() to determine if all the values in an iterable evaluate to True
# print(all(my_list))        
#  # Likewise, any() determines if one or more values in an iterable evaluate to True

# print(any(my_list))


# # reverse  list

# my_list.reverse()

# print(my_list)

# merged = my_list + my_list

# print(merged)

# print(len(my_list))

# # we can remove dupliate elements using  set

# new_list =  list(set(merged))

# print(new_list)


# my_listx=[{1}] * 10
# print(my_listx)

import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

data = {
    'Name': ['Tom', 'Jerry', 'Spike', 'Tyke'],
    'Age': [20, 21, None, 19],
    'Gender': ['M', 'M', 'M', 'M'],
    'Salary': [20000, 21000, 19000, None]
}
df = pd.DataFrame(data)

df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Salary'].fillna(df['Salary'].mean(), inplace=True)

le = LabelEncoder()
df['Gender'] = le.fit_transform(df['Gender'])

scaler = StandardScaler()
df[['Age', 'Salary']] = scaler.fit_transform(df[['Age', 'Salary']])

print(df)
