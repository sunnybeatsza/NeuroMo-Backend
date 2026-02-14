def authenticate():
    user_response = input("Have you created a username and password?: ")
    if user_response == "yes":
        user_username = input("Please enter your username: ")
        user_password = input("Please enter your password: ")

    else:
        new_username = input("Please enter user name that has 8 characters: ")
        new_password = input("Please enter a password that has 8 characters and a symbol: ")

