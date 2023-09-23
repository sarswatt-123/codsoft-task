import random
import string

# Function to generate a random password
def generate_password(length):
    # Define character sets for complexity
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine character sets based on desired complexity
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Generate the password by randomly selecting characters
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

# Prompt the user for the desired password length
try:
    length = int(input("Enter the desired password length: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit()

# Check if the length is valid
if length <= 0:
    print("Password length must be a positive integer.")
else:
    # Generate and display the password
    password = generate_password(length)
    print("Generated password:", password)
