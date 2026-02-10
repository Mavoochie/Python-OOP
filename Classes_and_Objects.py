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

# Exercise
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old")
s1 = Student("Alice", 20)
s2 = Student("Bob", 22)

s1.introduce()
s2.introduce()