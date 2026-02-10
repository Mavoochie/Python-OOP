# Encapsulation using python
"""Encapsulation is bundling data and methods while restricting
    direct access to some parts of the Object"""

class BankAccount:
    def __init__(self, Owner, Balance):
        self.Owner = Owner
        self._Balance = Balance

    def deposit(self, amount):
        if amount > 0:
            self._Balance += amount
        else:
            print("Balance must be positive")
    
    def withdraw(self, amount):
        if amount < self._Balance:
            self._Balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self._Balance

account = BankAccount("Marvin", 1000)
account.deposit(500)
print(f"Your account balance is ", account.get_balance() )
account.withdraw(2000)

"""Never expose sensitive attributes directly. Always control access through methods. If you allow direct modification, you risk breaking the logic of the program"""

# Quiz
class Person:
    def __init__(self, name, age=0):
        self.name = name
        self._age = age

    def set_age(self, age ):
        if age > 0:
            self._age = age 
        else:
            print("\n Age must be greater than 0")
        
    def get_age(self):
        return self._age
    
p = Person("Sean")
p.set_age(10)
print(p.get_age())
p.set_age(-5)

# quiz 2

class Account:
    def __init__(self, owner, pin):
        self.owner = owner
        self._pin = pin

    def set_pin(self, pin):
        pin_str = str(pin)
        if len(pin_str) == 4:
            self._pin = pin
        else: 
            print("\n Invalid PIN")
    def get_pin(self):
        return self._pin

a = Account("Dick", 1234)
print("__________________________")
a.set_pin(1234)
print(a.get_pin())
a.set_pin(123)

        