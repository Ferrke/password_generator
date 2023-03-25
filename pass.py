import string
import secrets

def generate_password(length):
    # Define the set of characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password 
    password = ''.join(secrets.choice(characters) for i in range(length))

    return password

number = input("How long do you want your password to be?\ntype a number between 1 and and a 1000 :")
password = generate_password(int(number))
print(password)
