'''validate username
username is no more than 12 characters long
username must not contain any spaces
username must not contain digits and any special characters
'''
username = input("Enter your username: ")

if len(username) > 12 or not username.isalpha():

    print("Invalid username. It must be 12 characters or less, contain no spaces, and have no digits.")
else:

    print(f"Valid Username {username}")
