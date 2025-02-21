"""Modify the BankAccount class:

Add a class method set_bank_name(cls, name) to change the bank name for all accounts.
Add a static method bank_info() that prints: "Welcome to our bank!"""

class BankAccount:    

    bank_name = ""

    def __init__(self, __balance = 0):# Private attribute
        self.__balance = __balance

    def deposit(self, amount=0):
         self.__balance += amount
         print(self.__balance)

    def withdraw(self, amount=0.0):
        if amount <= self.__balance:
            self.__balance -= amount
        elif amount > self.__balance:
            print("Not enough funds")
    
    def get_balance(self):
        return f"Current Balance {self.__balance}"
    
    @classmethod
    def set_bank_name(cls, name):
        cls.bank_name = name

    @staticmethod
    def bank_info():
        print("Welcome to our bank")

    



BankAccount.set_bank_name("BigBank")
print(BankAccount.bank_name)  # Should print "BigBank"
BankAccount.bank_info()  # Should print "Welcome to our bank!"