import csv


class BankAccount:
    def __init__(self, account_number, account_holder, balance = 0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance


class BankApp:
    def __init__(self):
        self.accounts = {}
        self.load_data () #it will load data from backup file

    def load_data(self):
        try:
            with open ('backup.txt', 'r') as file:
                reader = csv.Dictreader(file)
            for row in reader:
                account_number = row["Account Number"]
                account_holder = row["Accountholder"]
                balance = float(row["Balance"])
                account = BankAccount(account_number, account_holder, balance)
                self.accounts[account_number] = account
        except FileNotFoundError:
            print("No backup file found")

    def save_data(self):
            with open ('backup.txt', 'w') as file:
                fieldnames = ["Account Number", "Account Name", "Balance"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for account_number, acount_number in self.accounts.items():
                    writer.writerow(
                        {
                            "Account Number": account_number,
                            "Account Name": acount_number.account_holder,
                            "Balance": acount_number.balance
                        }
                    )

    def create_account(self, account_number, account_holder):
        if account_number in self.accounts:
            print("Account already exists")
        else:
            accounts = BankAccount(account_number, account_holder)
            self.accounts[account_number] = accounts
            print("Account created successfully")

    def change_password(self, account_number, new_password):
        if account_number in self.accounts:
            self.accounts[account_number].account_holder = new_password
            print("Password changed successfully")
        else:
            print("Account does not exist")

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number].balance += amount
            print("Deposited successfully")
        else:
            print("Account does not exist")

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number].balance -=amount
            print("Withdrawn successfully")
        else:
            print("Account does not exist")

    def transfer(self, account_number, amount):
        if source_account_number in self.accounts and target_account_number in self.accounts:
            source_account_number = self.accounts[source_account_number]
            target_account_number = self.accounts[target_account_number]
            if source_account.balance >= amount:
                source_account.balance -= amount
                target_account.balance += amount
                print("Transferred successfully")
            else:
                print("Insufficient balance in the source account")
        else:
            print("one or both accounts does not exist")

    def check_balance(self, amount_number):
        if amount_number in self.accounts:
            print(self.accounts[amount_number].balance)
        else:
            print("Account does not exist")

    def display_display_screen():
        print("Welcome to the Bank App!") 
        username = input("Enter your username:")
        password = input("Enter your password:")
        
        return username


    def main():
        username = display_welcome_screen()
        print("Login successful")

        user_type = input("Select usertype from the list of users is Admin/ Banker/ Customer: ")

        if user_type.lower() == "Admin":
            from admin import admin_main
            admin_main()
        elif user_type.lower() == "Banker":
            from banker import banker_main
            banker_main()
        elif user_type.lower() == "Customer":
            from customer import customer_main
            customer_main()
        else:
            print("Invalid user type")

if __name__ == "__main__":
    main()


    

             
        



                
                