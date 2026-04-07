import json
import hashlib

DB_PATH = "database/users.json"

def load_users():
    with open(DB_PATH, "r") as f:
        return json.load(f)

def save_users(users):
    with open(DB_PATH, "w") as f:
        json.dump(users, f, indent=4)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register(username, password):
    users = load_users()

    for user in users:
        if user["username"] == username:
            print("User already exists!")
            return False

    new_user = {
        "username": username,
        "password": hash_password(password),
        "balance": 0,
        "transactions": []
    }

    users.append(new_user)
    save_users(users)

    print("Registration successful!")
    return True

def login(username, password):
    users = load_users()
    hashed = hash_password(password)

    for user in users:
        if user["username"] == username and user["password"] == hashed:
            print("Login successful!")
            return user

    print("Invalid credentials!")
    return None
