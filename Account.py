import json

DB_PATH = "database/users.json"

def save_all(users):
    with open(DB_PATH, "w") as f:
        json.dump(users, f, indent=4)

def update_user(updated_user):
    with open(DB_PATH, "r") as f:
        users = json.load(f)

    for i, user in enumerate(users):
        if user["username"] == updated_user["username"]:
            users[i] = updated_user
            break

    save_all(users)

def check_balance(user):
    print(f"Current Balance: ₹{user['balance']}")

def deposit(user, amount):
    user["balance"] += amount
    user["transactions"].append(f"Deposited ₹{amount}")
    update_user(user)
    print("Deposit successful!")

def withdraw(user, amount):
    if amount > user["balance"]:
        print("Insufficient balance!")
        return

    user["balance"] -= amount
    user["transactions"].append(f"Withdrew ₹{amount}")
    update_user(user)
    print("Withdrawal successful!")
