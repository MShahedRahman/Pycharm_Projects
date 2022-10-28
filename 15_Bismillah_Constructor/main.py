class Car:
    wheels=4
    def __init__(self):
        self.milage=10
        self.company= 'BMW'


c1 = Car()
c2 = Car()
print(c1.company, c1.milage, c1.wheels)
print(c2.milage, c2.company, c2.wheels)

c1.milage = 8
print(c1.company, c1.milage, c1.wheels)

c1.wheels = 5
print(c1.company, c1.milage, c1.wheels)
print(c2.milage, c2.company, c2.wheels)

Car.wheels = 5
print(c1.company, c1.milage, c1.wheels)
print(c2.milage, c2.company, c2.wheels)