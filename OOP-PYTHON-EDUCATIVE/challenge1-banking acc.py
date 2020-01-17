# Problem Statement #
#
# Implement a basic structure of a parent class, Account, and a child class, SavingsAccount.
# Task 1 #
#
# Implement properties as instance variables and set them to None or 0.
#
# Account has the following properties:
#
#     title
#     balance
#
# SavingsAccount has the following properties:
#
#     interestRate
#
# Task 2 #
#
# Create an initializer for Account class. The order of parameters should be the following:
#
# Account("Mark", 5000)
#
# where Mark is the title and 5000 is the account balance.
# Task 3 #
#
# Implement properties as instance variables and set them to None or 0.
#
# Create an initializer for SavingsAccount class using the initializer of the Account class in the order below:
#
# Account("Mark", 5000, 5)
#
#paent class
class Account():

    def __init__(self, title =None, balance=0):
        self.title = title
        self.balance = balance
    def getBalance(self):
        return self.balance
    def deposit(self, amount):
      self.balance=  self.balance + amount
    def withdrawal(self, amount):
       self.balance= self.balance - amount


class SavingsAccount(Account):
    def __init__(self, title=None, balance=0,  interestRate=0):
        super().__init__(title,balance)
        self.interestRate = interestRate
    def interestAmount(self):
        return (self.interestRate * self.balance)/100
demo1 = SavingsAccount("Mark", 2000, 5) #initializing a SavingsAccount object