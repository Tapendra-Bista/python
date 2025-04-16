# python uses indentation to define control and loop constructs
# in python whitespace need to give carefully because it may impact in syntax of python  
# colon (:) instead of curly bracket {}

# Example 
def displayName(): # this is a function and we use colon (:) from where function block start

    name = "Tapendra Bista" # belongs to function because it just below of fun name
    return name # this also belongs to function
print(displayName()) # doesn't belongs because it is OUTSIDE the function block

# start from leftmost area (without space) then it become newline or independent code line
# if start from just down of declare of fun,loop,etc than it belongs to it
# it includes space  just above , you can see name is inside fun

a =1
b= 9
if a>b:
    print("A is greater than B.")
else:
    print("B is greater than A.") 

    # Blocks that contain exactly one single-line statement may be put on the same line, though this form is generally not
#considered good stlye
if a>b:print("A is greater than B. ${a}")
else:print("B is greater than A. ${b}")
# if there is multiple line than it not work
# space vs tabs
print(" This include space")
print("\tThis include tabs")
# 1 tab equal  to 4   normal spaces
# always use 4 spaces for indentation
# mixing of both (tabs and space) not allow in version above 3.0 but in below possible