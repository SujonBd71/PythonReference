class Base:

    class inner:
        def __init__(self):
            self.data = 100

    def __init__(self):
        self.id = 100
        self.s = self.inner()
        # print("in base")

    def display(self):
        print("Base display")
        print(str(self.s.data))
    
def TestRun():
    b = Base()
    b.display()
TestRun()
