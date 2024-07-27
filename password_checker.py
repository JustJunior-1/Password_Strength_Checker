import re

def check_password_strength(password):
    """Function to check the strength of a given password."""
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[ @#$%^&+=]", password) is None
    
    password_ok = not (length_error or digit_error or uppercase_error or lowercase_error or symbol_error)
    return {
        'password_ok': password_ok,
        'length_error': length_error,
        'digit_error': digit_error,
        'uppercase_error': uppercase_error,
        'lowercase_error': lowercase_error,
        'symbol_error': symbol_error
    }

if __name__ == "__main__":
    password = input("Enter a password to check its strength: ")
    result = check_password_strength(password)
    
    if result['password_ok']:
        print("Your password is strong.")
    else:
        print("Your password is weak. Please address the following issues:")
        if result['length_error']:
            print(" - Password should be at least 8 characters long.")
        if result['digit_error']:
            print(" - Password should contain at least one digit.")
        if result['uppercase_error']:
            print(" - Password should contain at least one uppercase letter.")
        if result['lowercase_error']:
            print(" - Password should contain at least one lowercase letter.")
        if result['symbol_error']:
            print(" - Password should contain at least one special character (e.g., @, #, $, etc.).")
