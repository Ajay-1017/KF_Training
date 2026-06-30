# Duck Typing:
# Duck typing is a Python concept where the type of an object doesn't matter.
# If an object has the required method or behavior, it can be used.
# In other words, Python checks "what an object can do" instead of "what it is".

class Pycharm:
    def execute(self):
        print("compiling")
        print("running")


class MyEditor:
    def execute(self):
        print("spell check")
        print("compiling")
        print("running")

class Laptop:
    def code(self, ide):
        # Any object passed here is accepted as long as it has an execute() method.
        # This is Duck Typing in Python.
        ide.execute()


lap1 = Laptop()

py = Pycharm()
my = MyEditor()

lap1.code(py)
print("*" * 50)
lap1.code(my)