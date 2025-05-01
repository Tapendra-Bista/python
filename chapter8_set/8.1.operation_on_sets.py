# operation
x = {1,2,3,4,5,6,7}
y = {2,4,6,7,5,4,9}

# intersection
print(x.intersection(y))
#  using &  intersection also possible
# union , |
print(x.union(y))

# difference ,-
print(x.difference(y))

# Symmetric difference with
print(x.symmetric_difference(y))
# subset check
print(x.issubset(y))

# with single elements

# Existance check
print(2 in {1,2,3}) # true

print(3 in {2,5}) # false

print(9 not in {2,4}) # true


# add and remove
s = {1,2,3,4,5}
s.add(9)
print(s) # 1,2,3,4,5,9
s.discard(1)
print(s)  # 2,3,4,5,9
s.remove(3)
print(s) # 2,4,5,9

# Set operations return new sets, but have the corresponding in-place versions:
"""
method     in-place operation     in-place method
union          s |= t               update
intersection   s &= t           intersection_update
difference     s -= t           difference_update
symmetric_difference  s ^= t     symmetric_difference_update

"""

z = {1,2}
z.update({3,4,5})
print(z)