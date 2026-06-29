# 2) Create a Vehicle → Car and Bike inheritance example.

# Classes :

# Vehicle
# Car
# Bike

# Requirements :

# Vehicle should store:
# Brand
# Model
# Year

# Car should additionally store:
# Number of doors
# Fuel type

# Bike should additionally store:
# Engine CC
# Has gear (Yes/No)

# Methods:

# Display vehicle details.
# Display car details.
# Display bike details.

class Vehicle:
    def __init__(self,Brand,Model,Year):
        self.Brand = Brand
        self.Model = Model
        self.Year = Year
    
    def display_vehicle_details(self):
        print("Brand :",self.Brand)
        print("Model :",self.Model)
        print("year :",self.Year)

class Car(Vehicle):
    def __init__(self,Brand,Model,Year,no_of_doors,fuel_type):
        super().__init__(Brand,Model,Year)
        self.no_of_doors = no_of_doors
        self.fuel_type = fuel_type
    
    def display_car_details(self):
        self.display_vehicle_details()
        print("No of doors :",self.no_of_doors)
        print("Fuel_type :",self.fuel_type)

    def start(self):
        print(f"{self.Brand} starts with car key ")
        


class Bike(Vehicle):
    def __init__(self,Brand,Model,Year,Engine_CC,gear):
        super().__init__(Brand,Model,Year)
        self.Engine_CC = Engine_CC
        self.gear = gear
    
    def display_Bike_details(self):
        self.display_vehicle_details()
        print("Engine CC :",self.Engine_CC)
        print("gear :",self.gear)

    def start(self):
        print(f"{self.Brand} starts with self start ")


v1 = Vehicle("audi","q5",2012)
v1.display_vehicle_details()
print('*'*50)

c1 = Car("audi","q5",2012,4,"petrol")
c1.display_car_details()
c1.start()
print('*'*50)

b1 = Bike("royal enfield","classic 350",2012,350,"Yes")
b1.display_Bike_details()  
b1.start()
print('*'*50)
