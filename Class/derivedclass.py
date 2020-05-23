from baseclass import Base

class Derived(Base):

    count = 10
    def __init__(self):
        super().__init__()
        # print("in derived")
        self.count = 100

    def fun(self):
        print("infunction")
    
    def display(self):
        print("Derived display")

a = Derived()
a.display()



