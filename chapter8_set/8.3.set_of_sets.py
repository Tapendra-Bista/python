# set inside set

# {{1,2,3},{4,6,7},7}
# this type of  nested set not allowed
# typeError : unshable type : set

# instead frozenset to include set  inside set
example = {frozenset({1,2,3}), frozenset({4,5,6,7,8})}

for element in example:
    print(element)