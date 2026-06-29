# 5) Build an Online Shopping hierarchy with Product, Electronics, and Clothing classes.

# Classes :

# Product
# Electronics
# Clothing

# Requirements :

# Product:
# Product name
# Price
# Brand

# Electronics:
# Warranty period
# Power consumption

# Clothing:
# Size
# Material

# Methods:
# Display product details.
# Calculate discounted price.
# Override the discount calculation in each child class if the discount rules differ.

class Product:
    discount_price = 0
    def __init__(self,product_name,brand,price):
        self.product_name=product_name
        self.price=price
        self.brand=brand

    def Product_details(self):
        print("Product_name :",self.product_name)
        print("Price :",self.price)
        print("Brand :",self.brand)
    

class Electronics(Product):
    discount_price = 0.10
    def __init__(self,product_name,brand,price,power_consumption,warranty): 
        super().__init__(product_name,brand,price)
        self.warranty = warranty
        self.power_consumption=power_consumption

    def discount_caluculation(self):
        return self.price - (self.price * self.discount_price)

    def details(self):
        self.Product_details()
        print("warranty :",self.warranty)
        print("power_consumption :",self.power_consumption)
        print("discount percentage :",str(self.discount_price*100) + "%")
        print("discount: ",self.discount_caluculation())


class Clothing(Product):
    discount_price = 0.05
    def __init__(self,product_name,brand,price,size,material): 
        super().__init__(product_name,brand,price)
        self.size = size
        self.material=material

    def discount_caluculation(self):
        return self.price - (self.price * self.discount_price)
    
    def details(self):
        self.Product_details()
        print("size :",self.size)
        print("material :",self.material)
        print("discount percentage :",str(self.discount_price*100) + "%")
        print("discount: ",self.discount_caluculation())


e1 = Electronics("TV","Sony",50000,"10w","5 years") 
e1.details()     
    
print('*'*50)

c1 = Clothing("T-shirt","Jockey",3000,"L","slim fit") 
c1.details()
        

    


    



    


