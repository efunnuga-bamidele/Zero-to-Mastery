print("This is a Password Checker Application")

user_name = input("Enter a username: ")
password = input("Enter a password: ")

hashed_password = '*' * len(password)

print(f"{user_name}, your password : {hashed_password} is {len(password)} characters long")
