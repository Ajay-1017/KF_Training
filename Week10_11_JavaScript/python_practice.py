
class Age:

    def __init__(self,age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,a):
        if a < 0:
            print("invalid age")
        else:
            self._age = a
        

ajay = Age(21)

print(ajay.age)
ajay.age = -31
print(ajay.age)




