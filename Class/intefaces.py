from interface import implements, Interface

class MyInterface(Interface):

    def method1(self, x):
        pass

    def method2(self, x, y):
        pass

    # def method3(self, x, y):
    #     pass


class MyClass(implements(MyInterface)):

    def method1(self, x):
        return x * 2

    def method2(self, x, y):
        return x + y


def InterfaceTest():
    obj = MyClass()
