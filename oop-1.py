# Object Oriented programming in Python 
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        print(f"{self.brand}{self.model} is driving")

car1 = Car("Toyota", "Corolla")
car2 = Car("Mazda","CX-7")

car1.drive()
car2.drive()

