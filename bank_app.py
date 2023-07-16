import tkinter as tk
class Account:
    def __init__(self, account_number, account_type):
        if len(str(account_number)) != 9:
            raise ValueError("Account number must be nine digits")
        self.account_number = account_number
        self.balance = 0
        self.account_type = account_type

    window = tk.Tk()
    window.title()
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds!")

# Main banking app
while True:
    print("Welcome to my Banking App!")
    account_type = input("Enter account type (current or savings, account: ")
    account_number = input("Enter your nine digit account number: ")

    if len(account_number) != 9:
        print("Invalid account number format")
        continue

    if account_type.lower() == "current":
        current_account = Account(account_number, "current")
        selected_account = current_account
    elif account_type.lower() == "savings":
        savings_account = Account(account_number, "savings")
        selected_account = savings_account
    else:
        print("Invalid account type!")
        continue

    while True:
        print("\nPlease select an option:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Exit")

        option = input("Enter your choice (1-3): ")

        if option == "1":
            amount = float(input("Enter the deposit amount: "))
            selected_account.deposit(amount)
            print("Deposit successful!")
        elif option == "2":
            amount = float(input("Enter the withdrawal amount: "))
            selected_account.withdraw(amount)
            print("Withdrawal successful!")
        elif option == "3":
            print("Thank you for using the Python Banking App!")
            break
        else:
            print("Invalid option!")

window.mainloop()