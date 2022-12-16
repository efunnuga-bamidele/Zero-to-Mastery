
print("This is an App that collects username and password, encrypt the password and greets the user with the length of password\n")

username = input("Enter username: ")
password = input("Enter password: ")

hashPassword = ('*' * len(password))
password_length = len(password)

print(f"Hello {username}, your password {hashPassword} is {password_length} letters long!\n")