# 1. raise the power 
#Let's suppose we want to raise x to a number y
# function


def raise_number(x,y):
    return x**y

print('The power of 5 raised to 2 is:', raise_number(5,2))    


# valid user input 


def raise_number_two(x,y):
    if y in [0,1,2,3]:
        return x**y
    else : raise ValueError('y must be 0,1,2 or 3')  

print(raise_number_two(5,1))    


