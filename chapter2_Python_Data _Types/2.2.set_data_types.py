# seets are the unodered collections of unique objects, there are  two of set
# sets
# Frozenset

# set are mutable and new  elements  can be added once sets are defined
# it can include duplicate data

basket = {"tapendra",2,3,3.33,"bista " , 'k','bista'}
# data can be any type
print(basket)

# add new element
basket.add("new add")
print(basket)

# clear all
basket.clear()

print("clear all ",basket)

# frozon sets
# they are imutable and new elements cannot added after its defined
cities = frozenset (["A",1,3.3,"A",1])
# frozenset  never contain dplicate data
print(cities)

# add
print("new print",cities)
# another 

names = (["Tapendea","Hari","Laxman", "ramesh","satish"])