import getpass
import bcrypt
import re
import os

DB_FILE = "demo_db.txt"

def is_valid_password(password):
    return len(password) >= 8 and re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

def load_users():
    users = {}
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            for line in f:
                username, hashed = line.strip().split(":")
                users[username] = hashed.encode()  # stored as bytes
    return users

def save_user(username, hashed_password):
    with open(DB_FILE, "a") as f:
        f.write(f"{username}:{hashed_password.decode()}\n")  # store hashed password as string

def register(users):
    username = input("Enter a username (min 8 chars): ")
    while True:
        password = getpass.getpass("Enter a password (min 8 chars, 1 symbol): ")
        if is_valid_password(password):
            break
        print("Password does not meet criteria.")
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    users[username] = hashed
    save_user(username, hashed)
    print("Registration successful!")

def login(users):
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    hashed = users.get(username)
    if hashed and bcrypt.checkpw(password.encode(), hashed):
        print("Login successful!")
    else:
        print("Invalid username or password.")

def authenticate():
    users = load_users()
    choice = input("Do you have an profile? (yes/no): ")
    if choice.lower() == "yes":
        login(users)
    else:
        register(users)
