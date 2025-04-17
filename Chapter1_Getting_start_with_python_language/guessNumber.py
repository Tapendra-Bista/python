import random as rdm




def Game(userInput):
    number = rdm.randint(1,10)
    if userInput==number:
        print("You , guess the right number !")
    else: print("Better luck next time.")
    

def display ():
    number = int(input("Enter any number between 1 to 10 :"))
    Game(number)

display()