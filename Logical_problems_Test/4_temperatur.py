
class Temperature:
    def __init__(self,celsius):
        self.celsius= celsius

    @property
    def fahrenheit(self):
        return self.celsius * (9/5 + 32)
        
t = Temperature(25)
print(t.fahrenheit) 
t.celsius = 100
print(t.fahrenheit)

    