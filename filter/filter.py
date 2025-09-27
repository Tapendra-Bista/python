# filter 

# basic filter like we can elimates items from list in easy way 

# example

example = ['a','Tapendra','ram','popma','khagendra']

def long_name(name):
   if  len(name)>3 : print(" yes length is greater than 3",name)

   else:
      print("no")


for name in  example:
   long_name(name)


 # filter without function
before = (None,[1,2,3,5],[],'')
after = list(filter(None, before))
print(after)