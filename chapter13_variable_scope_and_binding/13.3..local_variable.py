"""If a name is bound inside a function, it is by default accessible only within the function"""


def addition ():
    a= 10  # local
    b = 20 # local
    print(a+b)
    
addition()


class Display:
    name = "Tapendra Bista" # local

    def name_display(self):
       
        print(self.name)

d = Display()
d.name_display()


