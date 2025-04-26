#  dictionary is similar to  Maop (dart)
# it consist of  key-values pairs. it enclose by curly braces {}

personDetails = {
"name":"Tapendra Bista",
"age":23,
"address":"Kailali",
"phone" : 98704633911,
"education" :"Bsc csit"
}

# print all
print(personDetails)

personDetails.pop("name")
print(personDetails)
print(personDetails.get("phone"))
print(personDetails["education"])
print(personDetails.values())
print(personDetails.keys())