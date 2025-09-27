# file read and write 

##
# we have to use  With  open file name ##
# write 

with open ("python.txt",'w') as obj:
    obj.writelines("This is an example of file write")
    

with open("python.txt",'r')  as obj:
    result = obj.readlines()
    print("String from file",result)
