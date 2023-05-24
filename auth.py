import csv

def signup(username, password):
    if len(username) == 0:
        raise ValueError("Please enter a valid username with characters")
    elif len(username) > 30:
        raise ValueError("The username has to be less than 30 characters")
    elif username == "username" or username == "admin":
        raise ValueError("Don't use a forbidden username")

    with open("database.json", "r") as database:
        reader = csv.reader(database)
        for u, _ in reader:
            if username == u:
                raise ValueError("This username has already been taken")

    if len(password) < 4:
        raise ValueError("Please make sure your password is more than 4 characters")
    if password == "Password" or password == "password":
        raise ValueError("Choose a stronger password")

    with open("database.json", "a", newline="") as database:
        writer = csv.writer(database)
        writer.writerow([username, password])

    return "Your username and password have been successfully saved"


def login(username, password):
    with open("database.json", "r") as database:
        reader = csv.reader(database)
        for u, p in reader:
            if username == u:
                if password == p:
                    return "Login successful"
                else:
                    return "The password is incorrect"

    return "Sorry, username or password doesn't exist"

# Example usage when the library is imported
if __name__ == "__main__":
    username_input = input("What is your username: ")
    password_input = input("Enter your password: ")
    signup_result = signup(username_input, password_input)
    print(signup_result)

    username_input = input("What is your username: ")
    password_input = input("Enter your password: ")
    login_result = login(username_input, password_input)
    print(login_result)
