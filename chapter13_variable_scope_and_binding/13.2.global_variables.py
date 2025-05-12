"""In Python, variables inside functions are considered local if and only if they appear in the left side of an assignment
statement, or some other binding occurrence; otherwise such a binding is looked up in enclosing functions, up to
the global scope. This is true even if the assignment statement is never executed"""





# Global variables are access  every where 

# Example 

x = 'String'
y = 19

def read_x():
    print(x)


read_x()


def read_y():
    print(y)


read_y()

def changeValue ():
    x = "Tapendra Bista"
    print(x)

changeValue()


def change_global_y():
    global y
    y = 99
    print(y) 
    
change_global_y()

"""The global keyword means that assignments will happen at the module's top level, not at the program's top level.
Other modules will still need the usual dotted access to variables within the module"""

