class BankAccount:
    # Private attribute

    def __init__(self, __balance = 0):
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
    




acc = BankAccount(1000)
acc.deposit(500)
acc.withdraw(300)
print(acc.get_balance())  # Expected: 1200
acc.withdraw(2000)  # Should print an error
