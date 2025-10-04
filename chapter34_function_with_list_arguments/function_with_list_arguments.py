# Function  and call 

# list as argument are just another  variable 

def func(myList):
    for item in myList:
        print(item)

# calling the function with a list as argument
func([1,5,6,9,5,4,7,9,2])

# or as a varible 
myVarible = ['apple', 'banana', 'cherry']
func(myVarible)

#! Output:
