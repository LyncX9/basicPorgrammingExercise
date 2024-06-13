from bank_account import BankAccount

class BankingSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number):
        if account_number in self.accounts:
            raise ValueError("Account already exists")
        self.accounts[account_number] = BankAccount(account_number)
        print(f"Account {account_number} created successfully")

    def deposit_money(self, account_number, amount):
        if account_number not in self.accounts:
            raise ValueError("Account does not exist")
        try:
            self.accounts[account_number].deposit(amount)
            print(f"Deposit of {amount} successful")
        except ValueError as e:
            print(e)

    def withdraw_money(self, account_number, amount):
        if account_number not in self.accounts:
            raise ValueError("Account does not exist")
        try:
            self.accounts[account_number].withdraw(amount)
            print(f"Withdrawal of {amount} successful")
        except ValueError as e:
            print(e)

    def check_balance(self, account_number):
        if account_number not in self.accounts:
            raise ValueError("Account does not exist")
        print(f"Balance: {self.accounts[account_number].get_balance()}")