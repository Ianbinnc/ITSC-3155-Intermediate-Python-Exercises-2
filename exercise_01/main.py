# Main file for exercise 1
from BankAccount import BankAccount

# Creates new bank account
print("Creating a new bank account...")
newAccount = BankAccount("John Smith", 1000)
print("Account created. Account name: " + newAccount.account_name + ", Balance: " + str(newAccount.balance))

# Deposits $7654 and prints new balance
print("Depositing $7654...")
newAccount.deposit(7654)
print("New balance: " + str(newAccount.balance))

# Withdraws $423 and prints new balance
print("Withdrawing $423...")
newAccount.withdraw(423)
print("New balance: " + str(newAccount.balance))

