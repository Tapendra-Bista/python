"""As one of the most basic functions in programming, loops are an important piece to nearly every programming
language. Loops enable developers to set certain portions of their code to repeat through a number of loops which
are referred to as iterations. This topic covers using multiple types of loops and applications of loops in Python"""




"""break statement

When a break statement executes inside a loop, control flow "breaks" out of the loop immediately"""
# example  of its

i=0
while i<7:
    print(i)
    if i==4:
        print("Breaks")
        break
    i+=1
# I have used breaks at i ==4 so it doesnot print 5,6

"""The loop conditional will not be evaluated after the break statement is executed. Note that break statements are
only allowed inside loops, syntactically. A break statement inside a function cannot be used to terminate loops that
called that function"""

# break statements can also be used inside for loops, the other looping construct provided by Python

for  i in range(9):

    print(i)
    if i==4:
        break

    # if a loop has an else clause, it does not execute when the loop is terminated through a break statement
x = 10

for i in range(15):
    if i==9:
        print(i)
        break
    else:
        print(i)
 

"""continue statement
A continue statement will skip to the next iteration of the loop bypassing the rest of the current block but
continuing the loop. As with break, continue can only appear inside loops:"""

z=0
while z<10:
    print(z)
    if z==6:
        continue
    z+=1
    

"""break and continue only operate on a single level of loop. The following example will only break out of the inner
for loop, not the outer while loop"""

for i in range(11):
    if i==6:
        for x in range(10):

            if x == 7:
                break
        print(x)    

    print(i)        



    """Use return from within a function as a break
The return statement exits from a function, without executing the code that comes after it.
If you have a loop inside a function, using return from inside that loop is equivalent to having a break as the rest of
the code of the loop is not executed (note that any code after the loop is not executed either):
def break_loop():
    for i in range(1, 5):
        if (i == 2):
            return(i)
        print(i)
    return(5)
If you have nested loops, the return statement will break all loops:
def break_all():
    for j in range(1, 5):
        for i in range(1,4):
            if i*j == 6:
                return(i)
            print(i*j)"""