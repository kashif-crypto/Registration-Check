import random
import string

def generate_reference_number():
    """Generate a unique reference number consisting of 8 random alphanumeric characters."""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

def register_user(username, users):
    """
    Register a user by checking if the username is unique and adding a check mark with a reference number.
    Args:
        username (str): The username to register.
        users (dict): Dictionary of registered users.
    Returns:
        str: Success message with tick mark and reference number, or error message if username is taken.
    """
    if username in users:
        return f"Error: The username '{username}' is already registered."
    else:
        ref_number = generate_reference_number()
        users[username] = ref_number
        return f"Registration successful! ✓ Reference Number: {ref_number}"

# Sample usage
if __name__ == "__main__":
    # Dictionary to store registered users
    registered_users = {}

    # User registration
    username = input("Enter your username to register: ")
    result = register_user(username, registered_users)
    print(result)

    # Print all registered users (for testing purposes)
    print("\nRegistered Users:")
    for user, ref in registered_users.items():
        print(f"{user}: {ref}")
