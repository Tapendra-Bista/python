# tuple are element -wise  hashable and equatable

print(hash((1,2))) # ok

print(hash(([],{},2))) # not ok
# Error : Unhashable type: 'list'