class A():

    # class scope variable
    __instance = 0

    def __init__(self):
        print("in init")
        self.mine = 0
        self.secret = 1000
        A.__instance = A.__instance + 1

    # cls is used to say class scope,
    #self is used to specify instance scope
    @classmethod 
    def get_instance_count(cls):
        print("its a class method, it can access class state")

    @staticmethod
    def StaticMethod():
        print("its a static method like free function in C")
        print("total instance = " + str(A.__instance))

    def testPrivateMethod(self):
        print("in instance method")
        A.get_instance_count()

a= A()
a.mine = 10
print(a.mine)

print("total instance = " + str(A.get_instance_count()))
a= A()
print("total instance = " + str(A.get_instance_count()))

A.StaticMethod()
a.testPrivateMethod()
print(a.secret)

A.outsideClassMethod()
