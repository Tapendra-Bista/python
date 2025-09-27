'''A linked list is either:
the empty list, represented by None, or
a node that contains a cargo object and a reference to a linked list'''



class Node:
    def __init__(self, Cargo=None, next=None):
        self.car = Cargo
        self.cdr = next

    def __str__(self):
        return str(self.car)

    @staticmethod
    def display(lst):
        if lst:
            print("%s " % lst, end="")
            Node.display(lst.cdr)
        else:
            print('nil')
