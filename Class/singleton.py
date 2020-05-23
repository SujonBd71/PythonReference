

def singleToneWith__New__():
    class A(object):
        __instance = None
        def __new__(cls, val):
            if A.__instance == None:
                A.__instance = object.__new__(cls)
                A.__instance.val = val
            return A.__instance

        #class shouldn't have __init_ method

    a = A(10)
    print(a.val)

    a = A(20)
    print(a.val)


def singletone_with_hasAtrribute():
    class Singleton:
        def __new__(self, val):
            if not hasattr(self, 'instance'):
                self.instance = super().__new__(self)
                self.instance.val = val
            return self.instance

    s = Singleton(10)
    print("Object created:", s.val)

    s1 = Singleton(20)
    print("Object created:", s1.val)

singletone_with_hasAtrribute()

