# 1. Custom exception and base Account class
class InsufficientFundsError(Exception):
    pass


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


# 2. SavingsAccount with minimum balance constraint
class SavingsAccount(Account):
    def __init__(self, owner: str, balance: float = 0, min_balance: float = 500):
        super().__init__(owner, balance)
        self.min_balance = min_balance

    def withdraw(self, amount: float):
        if self.balance - amount < self.min_balance:
            raise InsufficientFundsError(
                f"Insufficient funds: balance {self.balance}, requested {amount}"
            )
        self.balance -= amount
        print(f"{self.owner} withdrew {amount} -> balance {self.balance}")


# 3. Test scenario: Priya with 1500, withdraw 1200, then 800
priya = SavingsAccount("Priya", 1500)

for amount in [1200, 800]:
    try:
        priya.withdraw(amount)
    except InsufficientFundsError as e:
        print(f"Error: {e}")

# 4. Check isinstance and explain
print(isinstance(priya, Account))
# Explanation: Returns True because SavingsAccount is a child class that inherits from the Account parent class.
