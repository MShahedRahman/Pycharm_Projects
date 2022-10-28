
class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()
    def show(self):
        print(self.name, self.rollno)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = '8gb'
        def show(self):
            print(self.brand, self.cpu, self.ram)

s1 = Student('Shahed', 18)
s2 = Student('Dristy', 3)

s1.show()
