# email validation using regex
import re

pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zZ-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
pattern2 = re.compile(r"[a-zA-Z0-9$%#@]{8,}\d")


input_email = input("Enter your email address: ")
input_password = input("Enter a password not less than 8 characters and ends with a number: ")

hash_pass = '*' * len(input_password)

a = pattern.search(input_email)
b = pattern2.fullmatch(input_password)

print(f"Email entered is: {input_email} and the regex output : {a}")
print(f"Password entered is: {hash_pass} and the regex output : {b}")
