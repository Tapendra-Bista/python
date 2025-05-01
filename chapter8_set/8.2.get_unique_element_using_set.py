 # suppose
# we have a list
myList = ['q','w','e','r','q','e']
print(myList) # all
unique =      set(myList)

print(unique) # remove all duplicate data

# convert  into list again
newList = list(unique)
print(newList)
#It's also common to see this as one line
print(list(set(myList)))

"""Let's say you've got a list of restaurants -- maybe you read it from a file. You care about the unique restaurants in
the list. The best way to get the unique elements from a list is to turn it into a set:
restaurants = ["McDonald's", "Burger King", "McDonald's", "Chicken Chicken"]
unique_restaurants = set(restaurants)
print(unique_restaurants)
# prints {'Chicken Chicken', "McDonald's", 'Burger King'}
Note that the set is not in the same order as the original list; that is because sets are unordered, just like dicts.
This can easily be transformed back into a List with Python's built in list function, giving another list that is the
same list as the original but without duplicates"""