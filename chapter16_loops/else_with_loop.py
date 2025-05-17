"""The for and while compound statements (loops) can optionally have an else clause (in practice, this usage is fairly
rare).
The else clause only executes after a for loop terminates by iterating to completion, or after a while loop
terminates by its conditional expression becoming false"""


#--------------- when we used use else with loop both run ------------------------

for i in range(9):
    print(i)
else:
    print("Done")    


i =0

while i<5:
    print(i)
    i += 1

else:
    print("Done")    