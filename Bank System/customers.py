def customer_main():
    print("Welcome, Customer!")

    def deposit_cash():
        account_number = input("Enter account number: ")
        amount = float(input("Enter the amount to deposit: "))

        if account_number in bank_app.accounts:
            bank_app.deposit(account_number, amount)
        else:
            print("Account does not exist!")

    def withdraw_cash():
        account_number = input("Enter account number: ")
        amount = float(input("Enter the amount to withdraw: "))

        if account_number in bank_app.accounts:
            bank_app.withdraw(account_number, amount)
        else:
            print("Account does not exist!")

    def transfer_amount():
        sender_account_number = input("Enter sender account number: ")
        reciever_account_number = input("Enter reciever account number: ")
        amount = float(input("Enter the amount to transfer: "))

        if sender_account_number in bank_app.accounts and reciever_account_number in bank_app.accounts:
            bank_app.transfer(sender_account_number, reciever_account_number, amount)
        else:
            print("One or both accounts do not exist!")

    def check_balance():
        account_number = input("Enter account number: ")
        if account_number in bank_app.accounts:
            bank_app.check_balance(account_number)
        else:
            print("Account does not exist!")

    bank_app = BankApp()

    while True:
        print("\nCustomer Menu:")
        print("1. Deposit Cash")
        print("2. Withdraw Cash")
        print("3. Transfer Amount")
        print("4. Check Balance")
        print("5. Exit Customer")

        choice = input("Enter your choice: ")

        if choice == "1":
            deposit_cash()
        elif choice == "2":
            withdraw_cash()
        elif choice == "3":
            transfer_amount()
        elif choice == "4":
            check_balance()
        elif choice == "5": 
            print("Exiting Customer: ")
            break
        else:
            print("Invalid choice!")