def ProperWay():
    class inch(float):
        # "Convert meter to CM"
        def __new__(cls, arg=0.0):
            return float.__new__(cls, arg*100)

    print(inch(10))

#This willn't work since init returns immediately
# top keep immutablity

def InCorrect():
    class inch(float):
        def __init__(self, arg=0.0):

            # doesn't work
            float.__init__(self,arg*100)
            pass
    
    print(inch(10))

ProperWay()
InCorrect()