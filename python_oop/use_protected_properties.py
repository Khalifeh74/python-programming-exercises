# 7
# Using protected properties:
# Create a class called "BankAccount" that has protected properties for the account balance.
# Then define methods for depositing and withdrawing funds.

class BankAccount:
    def __init__(self, account_balance):
        self._account_balance = account_balance

    def deposit(self, amount):
        self._account_balance += amount
        print(f"Deposited ${amount}.")

    def withdraw(self, amount):
        self._account_balance -= amount
        print(f"Withdrew ${amount}.")


account = BankAccount(1500)
print(f"Your initial account balance is: ${account._account_balance}")

account.deposit(300)
account.withdraw(200)

print(f"Your final account balance is: {account._account_balance}")
