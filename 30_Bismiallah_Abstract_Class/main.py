from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass
        #print('Running')

class Laptop(Computer):
    def process(self):
        print("Its Running")


class Whiteboard(Computer):
    def write(self):
        print("Its Writing")

class Programmer:
    def work(self,com):
        print("Solving Bugs")
        com.process()


com1 = Laptop()
com1.process()
com2 = Whiteboard()
prog1 = Programmer()
prog1.work(com1)

