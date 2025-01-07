# main.py - Main program to interact with the BankAccount class

from bank_account import BankAccount  # Import the BankAccount class from the bank_account.py file

def main():
    # Create a bank account with a specified number
    account = BankAccount("12345655559090111100007722")
    
    # Display initial account details
    account.show_account_details()

    # Deposit an amount
    account.deposit(25.30)

    # Display account details after deposit
    account.show_account_details()

    # Try to withdraw an amount that exceeds the balance
    account.withdraw(31.70)

    # Display account details after attempted withdrawal
    account.show_account_details()

    # Withdraw a valid amount
    account.withdraw(14.00)

    # Display account details after valid withdrawal
    account.show_account_details()

if __name__ == "__main__":
    main()
