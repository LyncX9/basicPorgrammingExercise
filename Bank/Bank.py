from banking_system import BankingSystem

def main():
    banking_system = BankingSystem()
    while True:
        print("Banking System Menu:")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            account_number = input("Enter account number: ")
            banking_system.create_account(account_number)
        elif choice == "2":
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to deposit: "))
            banking_system.deposit_money(account_number, amount)
        elif choice == "3":
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to withdraw: "))
            banking_system.withdraw_money(account_number, amount)
        elif choice == "4":
            account_number = input("Enter account number: ")
            banking_system.check_balance(account_number)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()