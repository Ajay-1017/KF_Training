
# 2) Implement Multiple Payment Methods

# What to do :

# Create a common parent class:
# Payment

# Create child classes:
# UPI
# CreditCard
# Cash

# Requirements:

# Each payment method should process payment differently.
# Use the same method name in all classes.
# Display a success message after payment.


# 1) Method Overriding 
class Payment:
    def pay_method(self):
        pass
    
class UPI(Payment):
    def pay_method(self):
        return "UPI payment is successfully completed"

class CreditCard(Payment):
    def pay_method(self):
        return "Credit Card payment is successfully completed"

class Cash(Payment):
    def pay_method(self):
        return "Cash payment is successfully completed"
    

upi = UPI()
credit = CreditCard()
cas = Cash()

print(upi.pay_method())
print(credit.pay_method())
print(cas.pay_method())


print('='*50)


# 2) Duck Typing 

class Payment:
    def calculate(self,obj):
        print(obj.pay_method())
    
class UPI:
    def pay_method(self):
        return "UPI payment is successfully completed"

class CreditCard:
    def pay_method(self):
        return "Credit Card payment is successfully completed"

class Cash:
    def pay_method(self):
        return "Cash payment is successfully completed"

pay = Payment()
upi = UPI()
credit = CreditCard()
cas = Cash()

pay.calculate(upi)
pay.calculate(credit)
pay.calculate(cas)