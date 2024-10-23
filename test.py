class Account:
    def _init_(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

class AccountManager:
    def _init_(self):
        self.accounts = {}

    def create_account(self, username, password, email):
        if username in self.accounts:
            print("Username already exists.")
            return
        self.accounts[username] = Account(username, password, email)
        print("Account created successfully.")

    def login(self, username, password):
        if username not in self.accounts:
            print("Username does not exist.")
            return
        if self.accounts[username].password != password:
            print("Incorrect password.")
            return
        print("Login successful.")

    def delete_account(self, username):
        if username not in self.accounts:
            print("Username does not exist.")
            return
        del self.accounts[username]
        print("Account deleted successfully.")

    def update_account(self, username, new_password=None, new_email=None):
        if username not in self.accounts:
            print("Username does not exist.")
            return
        if new_password:
            self.accounts[username].password = new_password
        if new_email:
            self.accounts[username].email = new_email
        print("Account updated successfully.")

    def display_accounts(self):
        for username, account in self.accounts.items():
            print(f"Username: {username}")
            print(f"Password: {account.password}")
            print(f"Email: {account.email}")
            print()

def main():
    account_manager = AccountManager()

    while True:
        print("1. Create Account")
        print("2. Login")
        print("3. Delete Account")
        print("4. Update Account")
        print("5. Display Accounts")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            email = input("Enter email: ")
            account_manager.create_account(username, password, email)
        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            account_manager.login(username, password)
        elif choice == "3":
            username = input("Enter username: ")
            account_manager.delete_account(username)
        elif choice == "4":
            username = input("Enter username: ")
            new_password = input("Enter new password (optional): ")
            new_email = input("Enter new email (optional): ")
            account_manager.update_account(username, new_password, new_email)
        elif choice == "5":
            account_manager.display_accounts()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

# if _name_ == "_main_":
#     main()