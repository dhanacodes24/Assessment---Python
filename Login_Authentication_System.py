# Improved Login Authentication System

def validate_login(username, password):
    # Validation 1: Username length must be at least 5 characters
    if len(username) < 5:
        print("Error: Username must be at least 5 characters")
        return False

    # Validation 2: Password length must be at least 8 characters
    if len(password) < 8:
        print("Error: Password must be at least 8 characters")
        return False

    # Validation 3: Password must contain at least one digit
    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
            break
    if not has_digit:
        print("Error: Password must contain at least one digit")
        return False

    # If all validations pass
    print("Login successful")
    return True


# Accept input from user
username = input("Enter username: ")

# Check username first before asking for password
if len(username) < 5:
    print("Error: Username must be at least 5 characters")
    print("Return: False")
else:
    password = input("Enter password: ")
    result = validate_login(username, password)
    print("Return:", result)