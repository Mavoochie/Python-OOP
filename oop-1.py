# # Object Oriented programming in Python 

# string = "Hello"
# print(string.upper()) # Object upper acting on type string in the string variable  

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def set_age(self, age):
        self.age = age

d = Dog("Bosco", 15)
d.set_age(5)
print(d.get_age())

