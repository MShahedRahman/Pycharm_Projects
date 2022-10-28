#DUCK_Typing

class PyCharm:
    def execute(self):
        print("Compiling")
        print("Running")

class MyEditor:
    def execute(self):
        print("Compiling")
        print("Running")
        print("Spell Check")
        print("Convertion Check")

class Laptop:
    def code(self,ide):
        ide.execute()

ide= MyEditor()
lap1 = Laptop()
lap1.code(ide)