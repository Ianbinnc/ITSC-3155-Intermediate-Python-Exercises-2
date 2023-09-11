# Ian Boyd ITSC 3155 Intermediate Python Exercises 2
# Resources Used: https://docs.python.org/3/tutorial/classes.html

class BankAccount:
    #Constructor for the BankAccount class
    def __init__(self, account_name, starting_balance):
        self.account_name = account_name
        self.balance = starting_balance

    # Deposit function
    def deposit(self, amount):
        self.balance += amount
    
    #Withdraw function
    def withdraw(self, amount):
        self.balance -= amount