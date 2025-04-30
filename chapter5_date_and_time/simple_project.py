from datetime import datetime

def getDob ():

    dobYear = int(input("Enter your birth year :"))
    currentYear = int(datetime.now().year)
    return currentYear- dobYear


result = getDob()
print("Your age is :",result)


