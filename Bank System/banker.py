def banker_main():
    print("Welcome, Banker!")

    def view_account_details():
        account_number = input("Enter account number: ")
        if account_number in bank_app.accounts:
            account = bank_app.accounts[account_number]
            print(f"Account Number: {account_number}")
            print(f"Account Holder: {account.account_holder}")
            print(f"Balance: {account.balance:.2f} units")
        else:
            print("Account does not exist!")

    def check_balance():
        account_number = input("Enter account number: ")
        if account_number in bank_app.accounts:
            account = bank_app.accounts[account_number]
            print(f"Account {account_number} balance: {account.balance:.2f} units.")
        else:
            print("Account does not exist!")

    def view_bank_statement():
        account_number = input("Enter account number: ")
        if account_number in bank_app.accounts:
            bank_statement = bank_app.get_bank_statement(account_number)
            print(f"Bank statement for Account {account_number}")
        else:
            print("Account does not exist!")

    bank_app = BankApp()

    while True:
        print("\nBanker Menu:")
        print("1. View Account Details")
        print("2. Check Balance")
        print("3. View Bank Statement")
        print("4. Exit Banker")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_account_details()
        elif choice == "2":
            check_balance()
        elif choice == "3":
            view_bank_statement()
        elif choice == "4":
            print("Exiting Banker.")
            break
        else:
            print("Invalid choice!")


