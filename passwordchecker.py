import re

def check_password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None
    
    if length_criteria and uppercase_criteria and lowercase_criteria and number_criteria and special_char_criteria:
        return "Strong password"
    elif length_criteria and (uppercase_criteria or lowercase_criteria) and number_criteria:
        return "Moderate password"
    elif length_criteria:
        return "Weak password"
    else:
        return "Very weak password"

# Example usage:
password = input("Enter a password to check its strength: ")
strength = check_password_strength(password)
print(f"Password strength: {strength}")
