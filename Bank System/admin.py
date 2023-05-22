def admin_main():
    print("Welcome, Admin!")

    def create_user():
        user_type = input("Enter user type (Admin/Banker/Customer): ")
        account_number = input("Enter account number: ")
        account_holder = input("Enter account holder name: ")

        if user_type.lower() == "admin" or user_type.lower() == "banker" or user_type.lower() == "customer":
            bank_app.create_account(account_number, account_holder)
        else:
            print("Invalid user type!")

    def change_user_password():
        account_number = input("Enter account number: ")
        new_password = input("Enter new password: ")

        if account_number in bank_app.accounts:
            bank_app.change_password(account_number, new_password)
        else:
            print("Account does not exist!")

    def create_backup():
        bank_app.save_data()
        print("Backup created successfully!")

    bank_app = BankApp()

    while True:
        print("\nAdmin Menu:") 
        print("1. Create User")
        print("2. Change User Password")
        print("3. Create Backup")
        print("4. Exit Admin")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_user()
        elif choice == "2":
            change_user_password()
        elif choice == "3":
            create_backup()
        elif choice == "4":
            print("Exiting Admin.")
            break
        else:
            print("Invalid choice!")


