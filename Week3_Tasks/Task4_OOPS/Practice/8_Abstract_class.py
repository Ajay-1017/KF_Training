from abc import ABC,abstractmethod

class Computer(ABC):

    @abstractmethod
    def process(self):
        pass
    
class Laptop(Computer):
    
    def process(self):
        print("running....")

class Desktop(Computer):
    # The abstract method 'process()' must be implemented in this class
    # because it inherits from the abstract class 'Computer'.

    def process2(self):
        print("running....")

l1 = Laptop()
d1 = Desktop()

l1.process()
d1.process2()



