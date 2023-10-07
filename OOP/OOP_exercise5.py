from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, balance=0):
        self.balance = balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

class SavingsAccount(BankAccount):
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")

class CheckingAccount(BankAccount):
    def deposit(self, amount):
        self.balance += amount

        def withdraw(self, amount):
            if self.balance - amount >= 0:
                self.balance -= amount
            else:
                print("Insufficient funds")



savings_account = SavingsAccount(1000)
print( savings_account.balance)
