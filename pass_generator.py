import random
import string

# ask user for password length
length = int(input("Enter password length: "))

# create a pool of characters to choose from
characters = string.ascii_letters + string.digits + string.punctuation

# Start with an empty password
password = ""

# generate password by randomly selecting characters
for i in range(length):
    password += random.choice(characters)

# print the generated password
print("Generated Password:", password)

