# You can compare multiple items with multiple comparison operators with chain comparison. For example

x=10
y=13
z =15

result = x<y<z
print(result)

# this is the short form of this
res = x<y and y <z
print(res)

# There is no theoretical limit on how many items and comparison operations you use as long you have proper syntex

print(1 > -1 < 2 > 0.5 < 100 != 24)


# As soon as one comparison returns False, the expression evaluates immediately to False, skipping all remaining
#comparisons

sideEffect =  x<30 and y <z
print(sideEffect)