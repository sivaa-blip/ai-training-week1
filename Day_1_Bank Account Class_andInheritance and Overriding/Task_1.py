# 1. Custom exception
class InsufficientFundsError(Exception):
    pass


# 2. Account class
class Account:
    def __init__(self, owner: str, balance: float = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float):
        self.balance += amount
        print(f"{self.owner} deposited {amount} -> balance {self.balance}")

    def withdraw(self, amount: float):
        if amount > self.balance:
            raise InsufficientFundsError(
                f"Insufficient funds: balance {self.balance}, requested {amount}"
            )
        self.balance -= amount
        print(f"{self.owner} withdrew {amount} -> balance {self.balance}")

    def show(self):
        print(f"Owner: {self.owner}, Balance: {self.balance}")

    # Bonus Challenge: __str__ method
    def __str__(self):
        return f"Account(Owner: {self.owner}, Balance: {self.balance})"


# 3. Test scenario with try/except/finally
account = Account("Arun", 1000)

try:
    account.deposit(500)
    account.withdraw(2000)
except InsufficientFundsError as e:
    print(f"Error: {e}")
finally:
    print("Transaction finished")
