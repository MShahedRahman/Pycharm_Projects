
class A:

    def __init__(self):
        print("Print in A INIT")
    def feature1(self):
        print("Feature1 is working")

    def feature2(self):
        print("Feature2 is working")

class B:

    def __init__(self):
        print("Print in B INIT")
    def feature3(self):
        print("Feature3 is working")

    def feature4(self):
        print("Feature4 is working")

class C(A,B):

    def __init__(self):
        print("Print in C INIT")
        super().__init__()


a1 = A()
#b1 = B()

c1 = C()
a1.feature1()


