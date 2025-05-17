#------------To print list elements---------------

for i in ['tapendra',"bista","hari","ram"]:
    print(i)


    #-----------------T0 print index and   elements
for index,items in enumerate( ['tapendra',"bista","hari","ram"]):
    print(index," : ",items)




"""Iterate over a list with value manipulation using map and lambda, i.e. apply lambda function on each element in the
list"""    


x =  map(lambda e : e.upper(),['tapendra',"bista","hari","ram"])
print(list(x))