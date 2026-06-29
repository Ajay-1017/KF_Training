# 2) Create a Car class with start and stop methods.

class Car:
    def __init__(self,car_owner,car_name):
        self.car_owner = car_owner
        self.car_name = car_name

    def start(self):
        return f"{self.car_owner}'s {self.car_name} car started"
    
    def stop(self):
        return f"{self.car_owner}'s {self.car_name} car stopped"
    
owner1 = Car("Ajay","BMW")
owner2 = Car("Balu","Bugati")

print(owner1.start())
print(owner2.stop())