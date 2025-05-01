print("\t\t\t\t\tSimple project regading set operation!")
Option = {
    "1" : "Union",
    "2" : "Intersection",
    "3" : "Difference"
}

def operations(userChoice,set1,set2):
    match userChoice:
        case 1:
            result = set1.union(set2)
            print("Set one :",set1)
            print("Set two :",set1)
            print("Union :",result)
        case 2: 
            result= set1.intersection(set2)
            print("Set one :",set1)
            print("Set two :",set1)
            print("Intersection :",result)
        case 3: 
            result = set1.difference(set2)
            print("Set one :",set1)
            print("Set two :",set1)
            print("Difference :",result)
        case _:
            print("Invalid choice")
            


print("\t\t\t\t")

set1 = set(input("Enter elements of set number one :").split())
set2 = set(input("Enter elements of set number two :").split())

print("\t\t\t\t")

for key,value in Option.items():
    print(key,value)

userInput = int(input("Chose operation from above: "))

operations(userChoice=userInput,set1 = set1,set2=set2)