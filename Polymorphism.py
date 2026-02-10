# OOP using python 
"""Polymorphism = same interface, different behavior.  
    It allows different classes to define methods with 
    the same name but different implementations."""

class Animal:
    def sound(self):
        print("This animal make a sound.")

class Dog(Animal):
    def sound(self):
        print("Woof!")

class Cat(Animal):
    def sound(self):
        print("Meaw!")

animals = [Dog(), Cat(), Animal()]
for a in animals:
    a.sound()
print("******************************")
"""All objects respond to sound()"""

# Quiz
class shapes:
    def area(self):
        print("Area of shapes can be obtained")

class Circle(shapes, ):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        PI = 3.142
        if self.radius > 0:
            circle_area= PI * (self.radius ** 2)
            print(f"Area of a circle is {circle_area}")
        else: 
            print("Enter a natural number")

class Rectangle(shapes):
    def __init__(self, length, width):
        self.length= length
        self.width = width
        
    def area(self):
        rect_area = self.length * self.width 
        if self.length > 0 and self.width > 0:
            print(f"Area of a rerctangle is {rect_area}")
        else :
            print("Enter natural numbers")

sh  = [Circle(5), Rectangle(4,6), shapes()]
for s in sh:
    s.area()