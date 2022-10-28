
class Student:

    school= 'BUET'
    def __init__(self, m1,m2,m3):
        self.m1=m1
        self.m2 =m2
        self.m3 = m3

    def average(self):
        return (self.m1 + self.m2 + self.m3)/3

    @classmethod
    def info(cls):
        return cls.school
    @staticmethod
    def information():
        print("This is Student Class ")

s1=Student(34,45,56)
s2=Student(32,45,67)

x= s1.average()
print(x)
y= s2.average()
print(y)

print(Student.info())
print(Student.information())
