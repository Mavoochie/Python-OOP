# OOP using python
"""Inheritance = creating new classes from 
    existing ones to reuse and extend functionality."""
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    
    def info(self):
        print(f"This is a {self.brand} vehicle.")

class Bike(Vehicle): # Bike inherits from vehicle
    def ride(self):
        print(f"Riding {self.brand} bike")

b = Bike("Yamaha")
b.info()
b.ride()
print("________________________________")

# Quiz

class Animal:
    def __init__(self, species):
        self.species = species
class Bird(Animal): 
    def fly(self):
        print(f"The {self.species} is flying" )
b = Bird("Eagle") 
b.fly()
print("________________________________")