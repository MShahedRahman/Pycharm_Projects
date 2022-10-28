
class A:
    def show(self):
        print("In A SHOW")

class B(A):
    pass

a = B()
a.show()