class A:

    def feature1(self):
        print("Feature1 is working")

    def feature2(self):
        print("Feature2 is working")

class B:

    def feature3(self):
        print("Feature3 is working")

    def feature4(self):
        print("Feature4 is working")

class C(A,B):

    def feature5(self):
        print("Feature5 is working")

    def feature6(self):
        print("Feature6 is working")

a1 = A()
b1 = B()
c1 = C()

a1.feature1()
a1.feature2()

b1.feature3()
b1.feature4()

c1.feature5()
c1.feature6()
c1.feature3()
c1.feature2()

#b1.feature1()
#b1.feature2()
