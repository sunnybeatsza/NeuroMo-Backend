from config.database import file_based_db
from features.auth.auth_service import authenticate

# Create a file based database if does not exist.
file_based_db()

print("Hello")
print("Welcome to NeuroMo!\n")

#Authenticate user credentials
authenticate()
