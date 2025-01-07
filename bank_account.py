# bank_account.py - Class definition for the BankAccount class

class BankAccount:
    def __init__(self, account_number):
        """Initializes the bank account with the account number and an initial balance of 0 PLN."""
        self.account_number = account_number
        self.balance = 0.0

    def deposit(self, amount):
        """Deposits the specified amount into the account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited: PLN {amount:.2f}")
        else:
            print("Deposit amount must be greater than 0.")

    def withdraw(self, amount):
        """Withdraws the specified amount from the account if sufficient funds are available."""
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: PLN {amount:.2f}")
        else:
            print("Insufficient funds on the account")

    def show_account_details(self):
        """Displays the account number and the balance in the specified format."""
        print(f"Bank Account No: {self.account_number[:2]} {self.account_number[2:8]} {self.account_number[8:14]} {self.account_number[14:20]} {self.account_number[20:26]}")
        print(f"Balance: PLN {self.balance:.2f}")
