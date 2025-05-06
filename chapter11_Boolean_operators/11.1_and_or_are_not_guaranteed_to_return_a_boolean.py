# when you use or , it will either return the first value in the expression if its true or , else it will blindly return value
# i.e or is equivalent to:
def or_(a,b):
    if a:
        return a
    else : 
        return b
    

result = or_(9,5)
print(result)
 
 # for and it will return first value if it's false , else it returns the last value:

def and_(a,b):
    if not a:
        return a
    else:
        return b

resut2 =and_(9,5)
print(resut2)