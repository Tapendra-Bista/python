# we can provide input in two way in python 
# raw_input
#input




name = input("Enter Your name : ")
print("Name is ",name)

# Note raw_input isn't  available in python version > 2.x
age = int(input("Enter your age : "))
print("Age is ",age)

if age is int:
    print ("This is a integer")