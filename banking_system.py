# Base class representing a general bank account
class BankAccount:
    def __init__(self, account_number, owner_name, balance=0.0):
        self.__account_number = account_number  # Private variable (encapsulation)
        self.owner_name = owner_name
        self.__balance = balance  # Private variable (encapsulation)

    # Getter for balance (encapsulation)
    def get_balance(self):
        return self.__balance

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    # Method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount.")

    # Private method (encapsulation)
    def __show_account_number(self):
        print(f"Account Number: {self.__account_number}")

    # Method to access private account number method
    def display_account_info(self):
        self.__show_account_number()
        print(f"Owner Name: {self.owner_name}")
        print(f"Balance: {self.__balance}")

# Derived class for a Savings Account with added functionality
class SavingsAccount(BankAccount):
    def __init__(self, account_number, owner_name, balance=0.0, interest_rate=0.01):
        super().__init__(account_number, owner_name, balance)
        self.interest_rate = interest_rate

    # Method to apply interest to balance
    def apply_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        print(f"Interest applied at rate {self.interest_rate * 100}%. Balance after interest: {self.get_balance()}")

# Derived class for a Checking Account with added functionality
class CheckingAccount(BankAccount):
    def __init__(self, account_number, owner_name, balance=0.0, overdraft_limit=500.0):
        super().__init__(account_number, owner_name, balance)
        self.overdraft_limit = overdraft_limit

    # Overriding the withdraw method to include overdraft limit
    def withdraw(self, amount):
        if 0 < amount <= (self.get_balance() + self.overdraft_limit):
            super().withdraw(amount)
        else:
            print(f"Overdraft limit exceeded. Max withdrawal allowed: {self.get_balance() + self.overdraft_limit}")

# Test the banking system
if __name__ == "__main__":
    # Create a savings account
    savings = SavingsAccount("SA12345", "John Doe", balance=1000.0, interest_rate=0.02)
    savings.display_account_info()
    savings.apply_interest()

    # Create a checking account
    checking = CheckingAccount("CA54321", "Jane Smith", balance=500.0, overdraft_limit=200.0)
    checking.display_account_info()
    checking.deposit(200)
    checking.withdraw(800)
    checking.withdraw(200)  # This should exceed the overdraft limit
