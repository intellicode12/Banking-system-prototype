from src.auth import register, login
from src.account import check_balance, deposit, withdraw
from src.transaction import show_transactions

def menu(user):
    while True:
        print("\n--- Banking Menu ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transaction History")
        print("5. Logout")

        choice = input("Enter choice: ")

        if choice == "1":
            check_balance(user)

        elif choice == "2":
            amount = float(input("Enter amount: "))
            deposit(user, amount)

        elif choice == "3":
            amount = float(input("Enter amount: "))
            withdraw(user, amount)

        elif choice == "4":
            show_transactions(user)

        elif choice == "5":
            print("Logged out.")
            break

        else:
            print("Invalid choice!")

def main():
    while True:
        print("\n--- Welcome to Banking System ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            username = input("Username: ")
            password = input("Password: ")
            register(username, password)

        elif choice == "2":
            username = input("Username: ")
            password = input("Password: ")
            user = login(username, password)

            if user:
                menu(user)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()
