import string
import random

# Function to generate a random password
def generate_password(length):
    if length < 4:  # Ensure the password length is sufficient for complexity
        return "Password length should be at least 4 characters."

    # Define the possible characters in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Main function to handle user input and display the password
def main():
    try:
        length = int(input("Enter the desired length of the password: "))
        password = generate_password(length)
        print(f"Generated Password: {password}")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
